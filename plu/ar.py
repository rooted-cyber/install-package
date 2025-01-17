from telethon import events
from os import system as s
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
  s("tof maruf")


@ultroid_bot(pattern="msg( (.*)")
async def linkrhss(e):
  await e.reply(f"{b}",parse_mode="html")
