@ultroid_cmd(pattern="o",manager=True)
async def hi(event):
  n = []
  async for m in asst.iter_participants(event.chat_id):
    if not (m.bot or m.deleted):
      n.append(m.id)

  udB.set_key('SUDOS', n)
  udB.set_key('FULLSUDO', " ".join(str(i) for i in n))
  await event.eor("**𝗦𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆 𝗮𝗱𝗱𝗲𝗱 𝗦𝗢𝗗𝗢 𝗮𝗻𝗱 𝗙𝗨𝗟𝗟𝗦𝗨𝗗𝗢**")
