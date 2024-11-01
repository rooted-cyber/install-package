from telethon import events
from random import choice as c
from telethon.tl import types
from . import ultroid_bot, LOGS
@ultroid_bot.on(events.NewMessage(outgoing=True))
async def linkrss(e):

  a = "😍","🔥","❤️","🤔","👍","😁","🥰"
  try:
    await e.react([types.ReactionEmoji(f"{c(a)}")])
  except Exception as ex:
    return LOGS.exception(ex)
  print("""
Now bot start

"""
