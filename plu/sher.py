from . import eor, ultroid_cmd, get_string, bash, LOGS
from io import BytesIO as open
@ultroid_cmd(pattern="sher ?(.*)")
async def sshe_ed(e):
  x = e.pattern_match.group(1).strip()
  d = await e.edit(f'[+] **searching** `{x}`')
  z,  _ = await bash(f"sher")
  a = await bash("sher {x}")
  if len(a) > 4096:
    with open(a.encode()) as sh:
      sh.name = "details.txt"
      await e.respond(file=sh)
  #b,_ = await e.client.fast_uploader(f"{x}.txt")
  #c = await e.client.send_file(e.chat, b)
  await d.edit(a)
  
