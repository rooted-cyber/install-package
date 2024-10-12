from . import LOGS
@ultroid_cmd(pattern="idu ?(.*)")
async def hi(event):
  ty = event.pattern_match.group(1)
  await event.edit("`𝗣𝗿𝗼𝗰𝗲𝘀𝘀𝗶𝗻𝗴....`")
  if not ty:
    await event.edit("`𝗧𝘆𝗽𝗲 𝗮𝗻𝘆 𝗶𝗱 𝘁𝗼 𝗴𝗲𝘁 𝘂𝘀𝗲𝗿𝗻𝗮𝗺𝗲`")
    return
  a = await bot.get_entity(int(ty))
  if not a:
    await event.edit("Your id is invalid")
    return
  b = a.username
  c = f"`Username of this id {int(ty)} :`  "
  if not b:
    await event.edit("`𝗧𝗵𝗶𝘀 𝘂𝘀𝗲𝗿 𝗶𝗱 𝗻𝗼𝘁 𝗮𝘃𝗮𝗶𝗹𝗮𝗯𝗹`?")
    return
  await event.respond(f"{c}@{b}")
  LOGS.info(f"{c}@{b}")
