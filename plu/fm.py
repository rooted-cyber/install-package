from telethon import events
@ultroid_cmd(events.NewMessage(pattern="fm",incoming=True,outgoing=True))
async def hi(event):
  reply = await event.get_reply_message()
  if not reply:
    await event.edit("`Reply any user`")
    return
  a = await bot.get_entity(reply.sender_id)
  b = f"{a.first_name}"
  l = f"{a.last_name}"
  u = f"{a.username}"
  await event.respond(f"First Name: `{b}`\nLast Name: `{l}`\nUsername: `@{u}`")


@ultroid_cmd(events.NewMessage(pattern="fm",incoming=True,outgoing=True))
async def hi(event):
  reply = await event.get_reply_message()
  if not reply:
    await event.edit("|𝗥𝗲𝗽𝗹𝘆 𝗮𝗻𝘆 𝘂𝘀𝗲𝗿`")
    return
  a = await bot.get_entity(reply.sender_id)
  b = "First_name: ", "`",a.first_name,"`"
  l = "Last Name: ", "`",a.last_name,"`"
  u = a.username
  await bot.send_message(event.chat_id,f"{b}\n\n{l}\n\nUsername: @{u}")


