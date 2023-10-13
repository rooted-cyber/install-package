from . import ultroid_cmd
@ultroid_cmd(pattern="ma( (.*)|$)",manager=True)
async def hi(event):
  a = event.pattern_match.group(1)
  reply = await event.get_reply_message()
  if reply:
    await event.respond(reply.text)
  else:
    await event.respond(f"{a}")