from . import ultroid_cmd, get_string, bash

@ultroid_cmd(pattern="ytt( (.*)|$)",manager=True)
async def cht(e):
  a = e.pattern_match.group(1).strip()
  await e.eor(get_string("com_1"))
  if not a:
    a = await bash("ytt --help")
    await e.reply(a)
  else:
    a,b = await bash(f"ytt {a}")
    await e.reply(a)