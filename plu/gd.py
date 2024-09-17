from . import ultroid_cmd, get_string, udB

@ultroid_cmd(pattern="gd",manager=True)
async def gd(e):
  b = await e.eor(get_string("com_1"))
  udB.set("GDRIVE_FOLDER_ID","1wGhvUWjslNUZ38bJoHAzIsLZRuRbi4fj")
  udB.set("GDRIVE_CLIENT_ID","69689902615-3b0c0tgg7me2pulu9vftvnsf9o9mpf6i.apps.googleusercontent.com")
  udB.set("GDRIVE_CLIENT_SECRET","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")
  udB.set("SUDO_HNDLR","$")
  udB.set_key("HNDLR","$")
  udB.set_key("ADDONS", True)
  await b.reply("**successfully set**")
