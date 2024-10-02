from pyUltroid.startup.loader import load_addons
from os import listdir as ls
from . import ultroid_cmd, get_string

@ultroid_cmd(pattern="pyc( (.*)|$)",manager=True)
async def ch(e):
  q = e.pattern_match.group(1).strip()
  reply = await e.get_reply_message()
  if reply:
    await e.respond("**Type plugin name not reply**")
    return
  b = f"{q}.py"
  d = ls("pyUltroid/_mu")
  if b in d:
    await e.eor(get_string("com_1"))
    load_addons(f"plugins/{q}.py")
    await e.reply(f"`Successfully loaded` **{q}** file")
  else:
     await e.respond(f"**{q} file not found**")
