from . import ultroid_cmd
import asyncio

@ultroid_cmd("hi")
async def slow_hello(event):
    msg = "hello"
    txt = ""
    sent = await event.reply("👀")
    for ch in msg:
        txt += ch
        await sent.edit(txt)
        await asyncio.sleep(0.5)
