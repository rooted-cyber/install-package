from telethon import events
from random import choice as c
from telethon.tl import types
from . import ultroid_bot
@ultroid_bot.on(events.NewMessage(outgoing=True))
async def linkrss(e):

  a = "😍","🔥","❤️","🤔","👍","😁","🥰"
  await e.react([types.ReactionEmoji(f"{c(a)}")])

from random import choice
from telethon import events, types
from . import ultroid_bot

emojis = ("😍","🔥","❤️","🤔","👍","😁","🥰")

@ultroid_bot.on(events.NewMessage(func=lambda e: e.out or (e.mentioned and not e.is_private)))
async def rootedcyber(rootedcyber):
  await rootedcyber.react([types.ReactionEmoji(choice(emojis))], big=False if rootedcyber.out else choice((True, False)))
