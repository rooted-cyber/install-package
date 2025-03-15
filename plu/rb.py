from . import ultroid_cmd, get_string
from urllib.parse import unquote
from bs4 import BeautifulSoup
import requests
@ultroid_cmd(pattern="rb")
async def sed(e):
  a = """
e from . import ultroid_cmd, get_string
from . import ultroid_cmd, get_string
from urllib.parse import unquote
from bs4 import BeautifulSoup
from io import BytesIO aas op
import requests
rp = await event.get_reply_message()
resp = requests.get(rp.text).content
soup = BeautifulSoup(resp, 'html.parser')
content = unquote(soup.get_text())
try:
  a = await e.reply(content)
except:
  with op(a.encode()) as op:
    op.name = "hi.txt"
    await e.reply(file="op")
"""
 
  await e.reply(f"<pre>{a}</pre>",parse_mode="html")