from . import eor, ultroid_cmd
from os import getcwd as pwd

@ultroid_cmd(pattern="pwd")
async def sshe_ed(e):
  await e.reply(f"Your directory : **{pwd()}**")

"""
commands

$wb -- reply or type
"""
@ultroid_cmd(pattern="lst")
async def shshe_ed(e):
  r = await e.get_reply_message()
  a = r.text
  await e.reply(f"{list(a)}")

import aiohttp
from io import BytesIO

from . import ultroid_cmd, check_filename, udB, LOGS, run_async, get_string


async def fetch_data_from_api(question):
    url = "https://bot-management-4tozrh7z2a-ue.a.run.app/chat/web"
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    payload = {"prompt": question, "bid" : "edwo6pg1"}

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=payload) as response:
            data = await response.json()
            return data.get("answer")


@ultroid_cmd(pattern="wb ?(.*)")
async def ask_bot(e):
    moi = await e.eor(f"**Fetching the answer**...")
    reply = await e.get_reply_message()
    question = e.pattern_match.group(1)
    #uestion += reply.text
    #question += f"\n {e.text}"
    if not question:
        if reply and reply.text:
            question = reply.message
    if not question:
        return await e.eor("`Please provide a question to ask the bot.`")

    # moi = await b.eor(f"**Question ✅**\n\n`{question}`\n\n`Answer❌❌ `\n""Fetching the answer...")
    try:
        response = await fetch_data_from_api(question)
        if not response:
            return await moi.edit("Failed to fetch the answer.")
    except Exception as exc:
        LOGS.warning(exc, exc_info=True)
        return await moi.edit(f"Error: {exc}")

    out = f"Question ✅\n\n{question}\n\nAnswer 👇`\n{response}"
    if len(out) > 4096:
        out = f"Question ✅\n\n{question}\n\nAnswer 👇`\n{response}"
        with BytesIO(out.encode()) as outf:
            outf.name = "answer.txt"
            await e.respond(f"`{response}`", file=outf, reply_to=e.reply_to_msg_id)
        await e.delete()
    else:
        out = f"**Question ✅**\n\n`{question}`\n\n`Answer👇👇👇\n\n **{response}**"
        #out = f"**Question**✅\n\n`{question}`\n\n**Answer** 👇\n{response}"
        await e.edit(f"{out}",parse_mode="md")
