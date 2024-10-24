from pyUltroid._my.my import *
from . import eor, ultroid_cmd
from os import getcwd as pwd

@ultroid_cmd(pattern="all")
async def sshe_ed(e):
  try:
    await dl(e)
    await photo(e)
  except:
    await photo(e)
