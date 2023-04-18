# Written by dot arc for Ultroid!

"""
**Get Answers from Chat GPT (Open AI)**

> `{i}gpt` (-i = for image) (query)

**• Examples: **
> `{i}gpt How to fetch a url in javascript`
> `{i}gpt -i Cute Panda eating bamboo` 

• It needs OpenAI api key to function! ☠️
"""

from os import system, remove
from io import BytesIO

try:
    import openai
except ImportError:
    system("pip install -q openai")
    import openai

from . import ultroid_cmd, check_filename, udB, LOGS, fast_download, run_async


@run_async
def get_gpt_answer(gen_image, question, api_key):
    openai.api_key = api_key
    if gen_image:
        x = openai.Image.create(
            prompt=question,
            n=1,
            size="1024x1024",
            user="arc",
        )
        return x["data"][0]["url"]
    x = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": question}],
    )
    LOGS.debug(f'Token Used on ({question}) > {x["usage"]["total_tokens"]}')
    return x["choices"][0]["message"]["content"].lstrip("\n")


@ultroid_cmd(
    pattern="a ?(.*)",
)
async def openai_chat_gpt(e):
    api_key = udB.get_key("OPENAI_API")
    gen_image = False
    if not api_key:
        return await e.eor("`OPENAI_API` key missing..")

    args = e.pattern_match.group(1)
    reply = await e.get_reply_message()
    if not args:
        if reply and reply.text:
            args = reply.message
    if not args:
        return await e.eor("`Gimme a Question to ask from ChatGPT`")

    moi = await e.eor(f"`getting response...`")
    if args.startswith("-i"):
        gen_image = True
        args = args[2:].strip()
    try:
        response = await get_gpt_answer(gen_image, args, api_key)
    except Exception as exc:
        LOGS.warning(exc, exc_info=True)
        return await moi.edit(f"**Error:** \n> `{exc}`")
    else:
        if gen_image:
            path, _ = await fast_download(
                response, filename=check_filename("dall-e.png")
            )
            await e.client.send_file(
                e.chat_id,
                path,
                caption=f"**{args[:1020]}**",
                reply_to=e.reply_to_msg_id,
            )
            await moi.try_delete()
            return remove(path)
        if len(response + args) < 4095:
            answer = f"<b>Query:</b>\n~ <i><code>{args}</code></i>\n\n<b>ChatGPT:</b>\n~ <code>{response}</code>"
            return await moi.edit(answer, parse_mode="html")
        with BytesIO(response.encode()) as file:
            file.name = "gpt_response.txt"
            await e.client.send_file(
                e.chat_id, file, caption=f"`{args[:1020]}`", reply_to=e.reply_to_msg_id
            )
        await moi.try_delete()
