from . import ultroid_cmd, get_string, bash

@ultroid_cmd(pattern="tu( (.*)|$)",manager=True)
async def cht(e):
  a = e.pattern_match.group(1).strip()
  await e.eor(get_string("com_1"))
  if not a:
    c,b = await bash(f"tu")
p(b))
    await e.reply(b)
  else:
    a,b = await bash(f"tu {a}")
    await e.reply(a)
