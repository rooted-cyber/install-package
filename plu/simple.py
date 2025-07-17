from . import ultroid_cmd
import asyncio

@ultroid_cmd("ab ?(.*)")
async def slow_hello(event):
    aa = event.pattern_match.group(1)
    msg = aa
    txt = ""
    sent = await event.reply("👀")
    for ch in msg:
        txt += ch
        await sent.edit(txt)
        await asyncio.sleep(0.5)
