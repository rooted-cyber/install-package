from . import eor, ultroid_cmd, get_string, bash, LOGS
from os import chdir as cd, chmod as ch, listdir as ls

@ultroid_cmd(pattern="sp$")
async def sp_eed(e):
  z = await e.eor(get_string("com_1"))
  x, y = await bash("curl -L https://gist.githubusercontent.com/rooted-cyber/6f47f4d7b3455dbe10556008515e0c9f/raw/speed | bash")
  if y: LOGS.info(y)
  await z.reply(f"`{x}`")
