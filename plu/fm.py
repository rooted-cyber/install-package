from telethon import events
from . import ultroid_cmd
from pyUltroid._my.my import *
@ultroid_cmd(pattern="fm( (.*)|$)",manager=True)
async def hi(e):
  reply = await event.get_reply_message()
  ty = event.pattern_match.group(1).strip()
  rep = reply.sender_id
  a = await event.client.get_entity(rep)
  b = f"{a.first_name}"
  l = f"{a.last_name}"
  u = f"{a.username}"
  ph = f"{a.phone}"
  b = file=await photo(e)
  await event.respond(f"{b}First Name: `{b}`\nLast Name: `{l}`\nUsername: `@{u}`\nPhone: `+{ph}`")


@ultroid_cmd(pattern="fm( (.*)|$)",manager=True)
async def hi(event):
  ty = event.pattern_match.group(1).strip()
  reply = await event.get_reply_message()
  rep = reply.sender_id
  if not reply:
    await event.edit("𝗥𝗲𝗽𝗹𝘆 𝗮𝗻𝘆 𝘂𝘀𝗲𝗿`")
  a = await event.client.get_entity(rep)
  b = "First_name: ", "`",a.first_name,"`"
  l = "Last Name: ", "`",a.last_name,"`"
  u = a.username
  ph = "phone:" +"`"+"+"+a.phone+"`"
  await event.client.send_message(event.chat_id,f"{b}\n\n{l}\n\nUsername: @{u}\n>\n{ph}")


