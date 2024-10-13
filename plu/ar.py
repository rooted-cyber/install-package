from telethon import events
from random import choice as c
from telethon.tl import types
from . import ultroid_bot
@ultroid_bot.on(events.NewMessage(outgoing=True))
async def linkrss(e):

  a = "😍","🔥","❤️","🤔","👍","😁","🥰"
  await e.react([types.ReactionEmoji(f"{c(a)}")])
