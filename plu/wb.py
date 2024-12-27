from . import eor, ultroid_cmd
from io import BytesIO
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
  b = f"{list(a)}"
  try:
    await e.reply(f"{b}")
  except:
    with BytesIO(b.encode()) as faltu:
      faltu.name = "faltu.txt"
      await e.reply(file=faltu)
import aiohttp
from io import BytesIO

from . import ultroid_cmd, check_filename, udB, LOGS, run_async, get_string


async def fetch_data_from_api(question):
    url = "http://app-paal-chat-1003522928061.us-east1.run.app"
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    payload = {"prompt": question, "bid" : "edwo6pg1"}

    async with aiohttp.ClientSession() as session:

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
