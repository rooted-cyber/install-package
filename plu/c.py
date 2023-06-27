@ultroid_cmd(pattern="c",manager=True)
async def hi(event):
  reply = await event.get_reply_message()
  try:
    await event.respond(f"`{reply.text}`")
  except:
    await event.respond(f"`{event.text}`")