from . import ultroid_cmd, udB, eor

@ultroid_cmd(pattern="su$", manager=True)
async def add_fsudoz(event):
  x = await event.eor("**Adding.....**")
  n = udB.get_key("SUDOS") or []
  async for m in event.client.iter_participants(event.chat_id):
    if not (m.bot or m.deleted):
      n.append(m.id)

  n = list(set(n))
  udB.set_key('SUDOS', n)
  udB.set_key('FULLSUDO', " ".join(str(i) for i in n))
  await x.edit("𝗦𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆 𝗮𝗱𝗱𝗲𝗱 𝗦𝗢𝗗𝗢 𝗮𝗻𝗱 𝗙𝗨𝗟𝗟𝗦𝗨𝗗𝗢")
