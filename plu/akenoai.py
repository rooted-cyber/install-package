from . import *
@ultroid_cmd(pattern="ak$",manager=True)
async def hi(event):
  reply = await event.get_reply_message()
  import akenoai as dev
  await event.eor(get_string("com_1"))
  api = dev.AkenoPlus(key=...)
  response = await api.chatgpt_old(query=reply.text)
  data = await api.get_json(response=response)
  await event.reply(data.randydev.message)
