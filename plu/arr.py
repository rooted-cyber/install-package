from random import choice
from telethon import events, types

emojis = ("😍","🔥","❤️","🤔","👍","😁","🥰")

@ultroid_bot.on(events.NewMessage(func=lambda e: e.out or (e.mentioned and not e.is_private)))
async def rootedcyber(rootedcyber):
  await rootedcyber.react([types.ReactionEmoji(choice(emojis))], big=False if e.out else choice((True, False)))