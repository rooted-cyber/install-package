from . import eor, ultroid_cmd, get_string, eor, bash, LOGS
from pyUltroid.startup.loader import load_addons
from os import listdir as ls
@ultroid_cmd(pattern="ins")
async def sshd(e):
  rep = await e.get_reply_message()
  r = await rep.download_media()
  if r in ls("plugins"):
    return await e.reply("Already installed")
  await bash(f"cp {r} plugi*")
  load_addons(f"plugins/{r}")
  await bash(f"rm plu*/{r}")
  await e.reply("Installation completed")