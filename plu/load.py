from pyUltroid.startup.loader import load_addons
from os import listdir as ls
from . import ultroid_cmd, get_string

@ultroid_cmd(pattern="lo( (.*)|$)",manager=True)
async def ch(e):
  q = e.pattern_match.group(1).strip()
  reply = await e.get_reply_message()
  if reply:
    await e.respond("**Type plugin name or reply**")
    return
  b = f"{q}.py"
  d = ls("plugins")
  s = ls("addons")
  if b in d:
    pr = await e.eor(get_string("com_1"))
    load_addons(f"plugins/{q}.py")
    await pr.edit(f"Successfully loaded **{q}** plugin")
    load_addons(f"plugins/{reply}.py")
    await pr.edit(f"Successfully loaded **{reply}** plugin"
  elif b in s:
    pr = await e.eor(get_string("com_1"))
    load_addons(f"addons/{q}.py")
    await pr.edit(f"Successfully loaded **{q}** Addons plugin")
  else:
     await e.respond(f"**{q}** `Not found Plugins or Addons folder`")

