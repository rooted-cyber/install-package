from . import ultroid_cmd, get_string

@ultroid_cmd(pattern="sm( (.*)|$)",manager=True)
async def chht(e):
  a = e.pattern_match.group(1).strip()
  reply = await e.get_reply_message()
  await e.eor(get_string("com_1"))
  
  if reply:
    await reply.edit(f"{a}")
  else:
    await e.respond(f"{a}")
    