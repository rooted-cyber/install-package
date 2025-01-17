from . import ultroid_cmd, get_string, bash

@ultroid_cmd(pattern="tu( (.*)|$)",manager=True)
async def cht(e):
  a = e.pattern_match.group(1).strip()
  await e.eor(get_string("com_1"))
  if not a:
    c,b = await bash(f"tu")
    await e.reply(f"{c}\n{b}")
  else:
    a,b = await bash(f"tu {a}")
    await e.reply(a)



@ultroid_cmd(pattern="pp( (.*)|$)",manager=True)
async def cht(e):
  a = e.pattern_match.group(1).strip()
  await e.eor(get_string("com_1"))
  if not a:
    c,b = await bash(f"pp")
    await e.reply(f"{c}\n{b}")
  else:
    a,b = await bash(f"pp i {a}")
    await e.reply(a)

@ultroid_cmd(pattern="msg( (.*)|$)",manager=True)
async def linkrhss(e):
  ab = await e.get_reply_message()
  ty = e.pattern_match.group(1)
  if not ab:
    await e.reply(f"{ty}",parse_mode="html")
  else:
    await e.reply(f"{ab.text}",parse_mode="html")
