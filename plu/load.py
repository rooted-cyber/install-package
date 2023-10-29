from pyUltroid.startup.loader import load_addons
from os import listdir as ls
from . import ultroid_cmd, get_string

@ultroid_cmd(pattern="l( (.*)|$)",manager=True)
async def ch(e):
  q = e.pattern_match.group(1).strip()
  reply = await event.get_reply_message()
  if reply:
    await e.respond("**Type plugin name not reply**")
    return
  b = f"{q}.py"
  d = ls("plugins")
  if b in d:
    await event.eor(get_string("com_1"))
    load_addons(f"plugins/{q}.py")
    await e.reply(f"Successfully loaded **{q}**")
  else:
     await e.respond("**Type plugin name for load plugin**")
