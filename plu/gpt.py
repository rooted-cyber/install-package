# Provided By :- @NovaXMod
# Made by :- @ImmortalsXKing
# API Credits :- @ImSafone
#
# ported to ultroid by dot arc (@moiusrname)

"""
**Get Answers from Chat GPT**

> No need of any API key.

**• Examples: **
> `{i}/p How to get a url in Python`
"""

from io import BytesIO
from pyUltroid.startup.loader import load_addons



from . import async_searcher, LOGS, ultroid_cmd, eor, get_string


@ultroid_cmd(pattern="p( ([\s\S]*)|$)",manager=True)
async def chatgpt2(e):
    query = e.pattern_match.group(2)
    reply = await e.get_reply_message()
    if not query:
        if reply and reply.text:
            query = reply.message
    if not query:
        return await e.eor("`Gimme a Question to ask from ChatGPT`")

    eris = await e.eor("__Generating answer...__")
    payloads = {
        "message": query,
        "chat_mode": "assistant",
        "dialog_messages": "[{'bot': '', 'user': ''}]"
    }
    try:
        response = await async_searcher(
            "https://api.safone.me/chatgpt",
            post=True,
            json=payloads,
            re_json=True,
            headers = {"Content-Type": "application/json"},
        )
        if not (response and "message" in response):
            LOGS.error(response)
            raise ValueError("Invalid Response from Server")

        response = response.get("message")
        if len(response + query) < 4080:
            to_edit = (
                f"<b>Query:</b>\n~ <i><code><b>Question</b>: {query}</code></i>\n<b>Answer: </b><i><code>{response}</code></i>"
            )
            await eris.edit(to_edit, parse_mode="html")
            return
        with BytesIO(response.encode()) as file:
            file.name = "gpt_response.txt"
            await e.client.send_file(
                e.chat_id, file, caption=f"`{query[:1020]}`", reply_to=e.reply_to_msg_id
            )
        await eris.try_delete()
    except Exception as exc:
        LOGS.exception(exc)
        await eris.edit(f"**Ran into an Error:** \n`{exc}`" )


@ultroid_cmd(pattern="m( (.*)|$)",manager=True)
async def msg(event):
 inp = event.pattern_match.group(1)
 reply = await event.get_reply_message()
 if not reply:
  await event.eor("**Reply forward/any message**")
  return
 try:
  await event.client.send_message(reply.fwd_from.from_id, f"{inp}")
  a = reply.fwd_from.from_id.user_id
  b = await event.client.get_entity(a)
  c = b.username
  u = (f"@{c}")
  await event.reply(f"Your message sent {u}")
 except :
     await event.client.send_message(reply.sender_id, f"{inp}")
     await event.reply("**Your message sent**")

@ultroid_cmd(pattern="l( (.*)|$)",manager=True)
async def ch(event):
    q = event.pattern_match.group(1).strip()
    await event.eor(get_string("com_1"))
    load_addons(f"plugins/{q}.py")
    await event.reply(f"loaded **{q}**")


@ultroid_cmd(pattern="s( (.*)|$)",manager=True) 
async def _(e): 
  await e.eor(get_string("com_1"))
  try: qr =e.text.split(None, 1)[1]
  except IndexError: await e.respond("No.")
  await e.respond(file="plugins/{}".format(qr))
