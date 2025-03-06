from . import ultroid_cmd, get_string, bash

@ultroid_cmd(pattern="hi",manager=True)
async def acht(e):

  await e.edit("hello")
