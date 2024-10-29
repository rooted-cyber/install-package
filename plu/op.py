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
    if a.text:
        with BytesIO(a.text.encode()) as bakwaas:
          bakwaas.name = c
          return await ax.reply(file=bakwaas,thumb=ULTConfig.thumb)
    b = event.pattern_match.group(1).strip()
    if not ((a and a.media) or (b and os.path.exists(b))):
        return await event.eor(get_string("com_1"), time=5)
    xx = await event.eor(get_string("com_1"))
    rem = None
    if not b:
        b = await event.client.download_media(a)
        rem = True
    try:
        with open(b) as c:
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
