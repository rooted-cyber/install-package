from . import asst, ultroid_cmd, get_string, get_paste, ULTConfig
import os
from io import BytesIO
@ultroid_cmd(
    pattern="op( (.*)|$)",
)
async def _(event):
    ax = await event.eor(get_string("com_1"))
    a = await event.get_reply_message()
    if not a:
        return await event.eor("`Reply any msg/flle`")
    c = event.pattern_match.group(1)
    if a.media:
        abr = await event.client.download_media(a)
        with open(abr) as rw:
            b = rw.read()
        try:
          return await event.reply(f"```{b}```")
        except:
            hat, key = await get_paste(b)
            with BytesIO(b.encode()) as faltu:
              faltu.name = "pasted.txt"
              await ax.reply(f"**MESSAGE EXCEEDS TELEGRAM LIMITS**\nPasted [SPACEBIN](https://spaceb.in/{key}) or [RAW](https://spaceb.in/api/v1/documents/{key}/raw)",file=faltu,thumb=ULTConfig.thumb)
    if a.text:
        with BytesIO(a.text.encode()) as bakwaas:
          bakwaas.name = c
          ab = thumb=ULTConfig.thumb
          rp = a.text
          fb = file=bakwaas
          return await ax.reply(file=bakwaas)
    #b = event.pattern_match.group(1).strip()
    #if not ((a and a.media) or (b and os.path.exists(b))):
        #return await event.eor(get_string("com_1"), time=5)
    #xx = await event.eor(get_string("com_1"))
    rem = None
    if not b:
        br = await event.client.download_media(a)
        rem = True
    try:
        with open(br) as c:
            d = c.read()
    except UnicodeDecodeError:
        return await xx.eor(get_string("cvt_8"), time=5)
    try:
        await xx.edit(f"```{d}```")
    except BaseException:
        hat, key = await get_paste(d)
        with BytesIO(d.encode()) as faltu:
            faltu.name = "pasted.txt"
            await xx.reply(f"**MESSAGE EXCEEDS TELEGRAM LIMITS**\nPasted [SPACEBIN](https://spaceb.in/{key}) or [RAW](https://spaceb.in/api/v1/documents/{key}/raw)",file=faltu,thumb=ULTConfig.thumb)
            await event.client.inline_query(asst.me.username, f"pasta-{key}")
    if rem:
        os.remove(b)
