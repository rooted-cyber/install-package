from . import eor, ultroid_cmd
from os import getcwd as pwd

@ultroid_cmd(pattern="pwd")
async def sshe_ed(e):
  await e.reply(f"Your directory : **{pwd()}**")