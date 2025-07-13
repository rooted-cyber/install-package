from . import ultroid_cmd, get_string
from . import ultroid_cmd
from urllib.parse import unquote
from bs4 import BeautifulSoup
import requests
from io import BytesIO

@ultroid_cmd(pattern="rb$")
async def urltxt(event):
    reply = await event.get_reply_message()
    if not reply or not reply.text.startswith("http"):
        return await event.reply("Reply to a valid URL.")

    try:
        resp = requests.get(reply.text, timeout=10).content
        soup = BeautifulSoup(resp, "html.parser")
        content = unquote(soup.get_text())
        if len(content) < 4096:
            await event.reply(content)
        else:
            file = BytesIO(content.encode())
            file.name = "output.txt"
            await event.reply("Text too long, sending as file:", file=file)
    except Exception as e:
        await event.reply(f"Error: {e}") e.reply(f"<pre>{a}</pre>",parse_mode="html")
