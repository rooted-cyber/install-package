from . import eor, ultroid_cmd, get_string, bash, LOGS

@ultroid_cmd(pattern="speed$")
async def spp_ed(e):
  z = await e.eor(get_string("com_1"))
  x, y = await bash("wget -q https://gist.githubusercontent.com/rooted-cyber/67631f88b791b73c114ff352badd873f/raw/speed;bash speed")
  if y: LOGS.info(y)
  await z.edit(x)
