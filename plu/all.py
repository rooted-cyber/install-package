from pyUltroid._my.my import *
from . import eor, ultroid_cmd
from os import getcwd as pwd

@ultroid_cmd(pattern="all")
async def sshe_ed(e):
  r = await e.get_reply_message()
  if r:
    await dl(e)
    await photo(e)
  else:
    await photo(e)
