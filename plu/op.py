from . import ultroid_cmd, get_string, get_paste
import os
@ultroid_cmd(
    pattern="op( (.*)|$)",
)
async def _(event):
    a = await event.get_reply_message()
    b = event.pattern_match.group(1).strip()
    if not ((a and a.media) or (b and os.path.exists(b))):
        return await event.eor(get_string("cvt_7"), time=5)
    xx = await event.eor(get_string("com_1"))
    rem = None
    if not b:
        b = await a.download_media()
        rem = True
    try:
        with open(b) as c:
            d = c.read()
    except UnicodeDecodeError:
        return await xx.eor(get_string("cvt_8"), time=5)
    try:
        await xx.edit(f"```{d}```")
    except BaseException:
        what, key = await get_paste(d)
        await xx.edit(f"**MESSAGE EXCEEDS TELEGRAM LIMITS**")
        await event.client.inline_query(asst.me.username,f"pasta-{key}") 
    if rem:
        os.remove(b)