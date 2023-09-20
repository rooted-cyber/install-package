from . import eor, ultroid_cmd, get_string, bash, LOGS

@ultroid_cmd(pattern="sher ?(.*)")
async def sshe_ed(e):
  x = e.pattern_match.group(1).strip()
  d = await e.reply(f'[+] **searching** `{x}`')
  y = await e.eor(get_string("com_1"))
  z,  _ = await bash(f"wget -q -O sher https://gist.githubusercontent.com/rooted-cyber/144f076670e6876b52e93499d9601439/raw/sherlock && bash sher && cd sherlock > /dev/null 2>&1 && python3 sherlock {x}")
  b,_ = await e.client.fast_uploader(f"sherlock/{x}.txt")
  c = await e.client.send_file(e.chat, b)
  await y.edit(z)
  await e.reply(c)