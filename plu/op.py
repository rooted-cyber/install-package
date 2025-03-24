 from . import asst, ultroid_cmd, get_string, get_paste, ULTConfig
from os import remove as rm
import os
from io import BytesIO
@ultroid_cmd(
    pattern="op( (.*)|$)",
)
async def _(event):
    ax = await event.eor(get_string("com_1"))
    a = await event.get_reply_message()
    hat, key = await get_paste(a.text)
    pa = f"Pasted in [SPACEBIN](https://spaceb.in/{key}) or [RAW](https://spaceb.in/{key}/raw)"
    if not a:
        return await event.eor("`Reply any msg/flle`")
    c = event.pattern_match.group(1)
    if a.media:
        abr = await event.client.download_media(a)
        with open(abr) as rw:
            b = rw.read()
        try:
          await event.reply(f"**{b}**\n{pa}")
          return rm(abr)
        except:
            hat, key = await get_paste(b)
            with BytesIO(b.encode()) as faltu:
              faltu.name = "pasted.txt"
              await event.reply(f"Found {len(b)} Characters so\nPasted [SPACEBIN](https://spaceb.in/{key}) or [RAW](https://spaceb.in/{key}/raw)",file=faltu,thumb=ULTConfig.thumb,parse_mode="md")
              return rm(abr)
    if a.text:
        with BytesIO(a.text.encode()) as bakwaas:
          bakwaas.name = c
          rp = a.text
          fb = file=bakwaas
          hat, key = await get_paste(rp)
          pa = f"Pasted in [SPACEBIN](https://spaceb.in/{key}) or [RAW](https://spaceb.in/{key}/raw)"
          await event.reply(f"{pa}",file=bakwaas,thumb=ULTConfig.thumb)
          
