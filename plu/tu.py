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
  elif a == c:
    a,z = await bash(f"pp c tele")
    await e.reply(a)
  else:
    a,b = await bash(f"pp {a}")
    await e.reply(a)
