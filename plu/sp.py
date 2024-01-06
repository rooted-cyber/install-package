from . import eor, ultroid_cmd, get_string, bash, LOGS
from os import chdir as cd, chmod as ch, listdir as ls

@ultroid_cmd(pattern="sp$")
async def spp_ed(e):
  z = await e.eor(get_string("com_1"))
  x, y = await bash("wget -O speed https://gist.githubusercontent.com/rooted-cyber/67631f88b791b73c114ff352badd873f/raw/speed;bash speed | grep -e 'Test' -e 'Down' -e 'Upload'")
  if "speed" in ls("/data/data/com.termux/files/usr/bin"):
    await e.reply("available")
  else:
    await bash("cp speed $PREFIX/bin;chmod 777 $PREFIX/bin/speed")
  if y: LOGS.info(y)
  await z.edit(f"`{x}`")