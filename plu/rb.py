from . import ultroid_cmd, get_string
from urllib.parse import unquote
from bs4 import BeautifulSoup
import requests
@ultroid_cmd(pattern="rb")
async def sed(e):
  c = await e.eor(get_string("com_1"))
  rp = await event.get_reply_message()
  pb = "•••••••••••••••••••••"
  try:
    resp = requests.get(rp.text).content
    soup = BeautifulSoup(resp, 'html.parser')
    content = unquote(soup.get_text())
    await c.reply(content)
  except:
    await c.reply("not")