from . import eor, ultroid_cmd, get_string, bash, LOGS
from io import BYtesIO
@ultroid_cmd(pattern="sher ?(.*)")
async def sshe_ed(e):
  x = e.pattern_match.group(1).strip()
  d = await e.reply(f'[+] **searching** `{x}`')
  y = await e.eor(get_string("com_1"))
  z,  _ = await bash(f"command -v sherlock || sher;wget -q -O sher https://gist.githubusercontent.com/rooted-cyber/aa5c3f2e24c37be15c5e40157b09873f/raw/97e61757789bf1850302041629298be91ae3309e/sher && bash sher > /dev/null 2>&1")
  a = await bash("sherlock {x}")
  if len(a) > 4096:
    with BYtesI9(a.encode()) as sh:
      sh.name = "details.txt"
      await e.respond(file=sh)
  #b,_ = await e.client.fast_uploader(f"{x}.txt")
  #c = await e.client.send_file(e.chat, b)
  await y.edit(a)
  
