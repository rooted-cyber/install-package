from . import eor, ultroid_cmd, get_string, bash, LOGS
from os import chdir as cd, chmod as ch, listdir as ls

@ultroid_cmd(pattern="speed$")
async def spp_ed(e):
  z = await e.eor(get_string("com_1"))
  x, y = await bash("wget -O sp https://gist.githubusercontent.com/rooted-cyber/6f47f4d7b3455dbe10556008515e0c9f/raw/speed && bash sp")
  if y: LOGS.info(y)
  await z.edit(f"`{x}`")
