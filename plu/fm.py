from telethon import events
from . import ultroid_cmd
@ultroid_cmd(pattern="fm",manager=True)
async def hi(event):
  reply = await event.get_reply_message()
  ty = event.pattern_match.group(1).strip():
  if not reply:
    await event.edit("`Reply any user`")
  else:
    return reply = ty
  a = await event.client.get_entity(reply.sender_id)
  b = f"{a.first_name}"
  l = f"{a.last_name}"
  u = f"{a.username}"
  ph = f"{a.phone}"
  await event.respond(f"First Name: `{b}`\nLast Name: `{l}`\nUsername: `@{u}`\nPhone: `+{ph}`")


@ultroid_cmd(pattern="fm ? (.*)",manager=True)
async def hi(event):
  ty = event.pattern_match.group(1).strip():
  reply = await event.get_reply_message()
  if not reply:
    await event.edit("𝗥𝗲𝗽𝗹𝘆 𝗮𝗻𝘆 𝘂𝘀𝗲𝗿`")
  else:
    reply = ty
  a = await event.client.get_entity(reply.sender_id)
  b = "First_name: ", "`",a.first_name,"`"
  l = "Last Name: ", "`",a.last_name,"`"
  u = a.username
  ph = "phone:" +"`"+"+"+a.phone+"`"
  await event.client.send_message(event.chat_id,f"{b}\n\n{l}\n\nUsername: @{u}\n>\n{ph}")


