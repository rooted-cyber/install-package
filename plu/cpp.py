from . import udB, ultroid_cmd, get_string, bash, call_back
import os, sys
@ultroid_cmd(pattern="cpp",manager=True)
async def cppb(ult):
  c = await ult.eor(get_string("com_1"))
  a,d = await bash(f"curl -Ls https://gist.githubusercontent.com/rooted-cyber/1bd2b7d3eb4d66ab06ab5e83098395e3/raw/cpp | bash")
  await c.edit(f"{a}\n\n")
  ok = await ult.eor(get_string("bot_5"))
  call_back()
  who = "bot" if ult.client._bot else "user"
  udB.set_key("_RESTART", f"{who}_{ult.chat_id}_{ok.id}")
  await bash("cd ~/T*d/U*")
  if len(sys.argv) > 1:
    os.execl(sys.executable, sys.executable, "main.py")
  else:
    os.execl(sys.executable, sys.executable, "-m", "pyUltroid")


@ultroid_cmd(pattern="py$",manager=True)
async def pby(e):
  c = await e.eor(get_string("com_1"))
  a,b = await bash(f"curl -L https://gist.githubusercontent.com/rooted-cyber/edc0ac4c7da73e933ad954f90c40447e/raw/py | bash")
  await c.edit(f"{a}")
  
@ultroid_cmd(pattern="opy$",manager=True)
async def opy(e):
  c = await e.eor(get_string("com_1"))
  fa,b = await bash(f"curl -L https://gist.githubusercontent.com/rooted-cyber/748b2a820247bd435c50d0de45fa9e3c/raw/opy | bash")
  await e.edit(fa)
  
