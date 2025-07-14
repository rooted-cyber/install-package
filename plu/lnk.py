from telethon import events
from . import ultroid_cmd
import requests
from urllib.parse import urlparse

@ultroid_cmd(pattern="lnk")
async def link_info(e):
    reply = await e.get_reply_message()
    if not reply or not reply.text:
        return await e.reply("Kisi link wale message par reply karo.")

    words = reply.text.split()
    link = None
    for word in words:
        if word.startswith("http://") or word.startswith("https://"):
            link = word
            break

    if not link:
        return await e.reply("Koi valid URL nahi mila reply mein.")

    try:
        r = requests.get(link, timeout=10)
        parsed = urlparse(link)
        info = f"""*🔗 Link Details*

**🌐 Domain:** {parsed.netloc}
**🛣️ Path:** {parsed.path or "/"}
**📥 Status:** {r.status_code}
**📄 Content-Type:** {r.headers.get("Content-Type", "Unknown")}
*📦 Size:* {len(r.content)} bytes
"""
        await e.reply(info)
    except Exception as ex:
        await e.reply(f"❌ Error while fetching: {ex}")
