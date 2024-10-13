from . import ultroid_cmd, get_string, udB

@ultroid_cmd(pattern="bk",manager=True)
async def gd(e):
  udB.set_key("GDRIVE_FOLDER_ID","1wGhvUWjslNUZ38bJoHAzIsLZRuRbi4fj")
  udB.set_key("GDRIVE_CLIENT_ID","69689902615-3b0c0tgg7me2pulu9vftvnsf9o9mpf6i.apps.googleusercontent.com")
  udB.set_key("GDRIVE_CLIENT_SECRET","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")
  udB.set_key("SUDO_HNDLR","$")
  udB.set_key("HNDLR","$")
  udB.set_key("ADDONS", True)
  udB.set_key("PMSETTING", True)
  udB.set_key("PMLOG", True)
  udB.get_key("PMLOGGROUP",-1001884618152)
  udB.set_key("PLUGGIN_CHANNEL",-4194506928)
  udB.set_key("TAG_LOG",-1001884618152)
  udB.set_key("PMPIC","https://envs.sh/SbN.jpg")
  await e.reply("successfully set")
