from . import ultroid_cmd
@ultroid_cmd(pattern="akn$",manager=True)
async def hi(event):
  reply = await event.get_reply_message()
  import akenoai as dev
  api = dev.AkenoPlus(key=...)
  response = await api.chatgpt_old(query=reply.text)
  data = await api.get_json(response=response)
  await event.reply(data.randydev.message)
