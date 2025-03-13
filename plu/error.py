@ultroid_bot.on(events.NewMessage(outgoing=True))
async def linkrss(e):

  a = "😍","🔥","❤️","🤔","👍","😁","🥰"
  try:
    await msg([types.ReactionEmoji(f"{c(a)}")])
  except Exception as ex:
    return LOGS.exception(ex)
  s("tof maruf")
