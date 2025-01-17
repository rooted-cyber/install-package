from . import ultroid_cmd, get_string
@ultroid_cmd(pattern="mlink$")
async def hi(e):
  reply = await e.get_reply_message()
  a = e.input_chat.channel_id
  b = reply.id
  await e.respond(f"msg link : tg://privatepost?channel={a}&amp&post={b} \nor\n https://t.me/c/{a}/{b}")
