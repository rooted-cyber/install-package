from . import eor, ultroid_cmd, get_string, bash, LOGS
from io import BytesIO as open
from os import system as s
@ultroid_cmd(pattern="sher ?(.*)")
async def sshe_ed(e):
  x = e.pattern_match.group(1).strip()
  d = await e.edit(f'[+] **searching** `{x}`')
  a = s(f"sher;sher {x}")
  if len(a) > 4096:
    await e.reply("Not poslsible")
  await d.edit(a)
  
