from telethon import events
from pyUltroid._my.my import *

@ultroid_cmd(pattern="fm( (.*)|$)",manager=True)
async def hi(e):
  await fm(e)
