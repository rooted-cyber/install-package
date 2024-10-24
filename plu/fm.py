from telethon import events
from . import ultroid_cmd
from pyUltroid._my.my import *

@ultroid_cmd(pattern="fm( (.*)|$)",manager=True)
async def hi(e):
  reply = await e.get_reply_message()
  ty = e.pattern_match.group(1).strip()
  if not reply:
    return await e.eor("not reply...", time=5)
  a = reply.sender  # await event.client.get_entity(rep)
  b = a.first_name
  l = a.last_name or ""
  u = ("@" + a.username) if a.username else "???"
  ph = a.phone
  fr = "First_name: ", "`",a.first_name,"`"
  las = "Last Name: ", "`",a.last_name,"`"
  pic = file=await photo(e)
  await e.respond(f"{pic}\nFirst Name: `{b}`\nLast Name: `{l}`\nnUsername: `{u}`\nPhone: `+{ph}`\n\n{fr}\n{las}")
