from . import ultroid_cmd, get_string, bash

@ultroid_cmd(pattern="hi",manager=True)
async def acht(e):
  x = await e.eor(get_string("com_1"))
  await x.edit("hello")
