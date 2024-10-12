import asyncio
from . import ultroid_cmd, get_string

@ultroid_cmd(pattern="file ?(.*)")
async def hi(event):
  text = event.pattern_match.group(1)
  ab = await event.get_reply_message()
  if not ab:
    await event.edit("`Reply any file or type name !!`")
    return
  await event.edit("`processing..`")
  await ab.download_media(text)
  await event.edit("`Proccessing Done` ✔️")
  await asyncio.sleep(1)
  await event.edit("`Now sending file`")
  await asyncio.sleep(0.1)
  await bot.send_file(event.chat_id, text,force_document=True)
