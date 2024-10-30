from . import ultroid_cmd, get_string, bash, callback
import os, sys
@ultroid_cmd(pattern="cpp",manager=True)
async def cppb(e):
  c = await e.eor(get_string("com_1"))
  a,b = await bash(f"curl -L https://gist.githubusercontent.com/rooted-cyber/1bd2b7d3eb4d66ab06ab5e83098395e3/raw/cpp | bash")
  await c.edit(f"{a}\n\n")


@ultroid_cmd(pattern="py$",manager=True)
async def pby(e):
  c = await e.eor(get_string("com_1"))
  a,b = await bash(f"curl -L https://gist.githubusercontent.com/rooted-cyber/edc0ac4c7da73e933ad954f90c40447e/raw/py | bash")
  await c.edit(a)
  
@ultroid_cmd(pattern="orp$",manager=True)
async def opy(e):
  c = await e.eor(get_string("com_1"))
  a,b = await bash(f"curl -L https://gist.githubusercontent.com/rooted-cyber/748b2a820247bd435c50d0de45fa9e3c/raw/opy | bash")
  await c.reply(a)
  
