try:
  from RyuzakiLib.hackertools.chatgpt import RendyDevChat
except:
  import os
  os.system("pip3 install -U RyuzakiLib")
  from RyuzakiLib.hackertools.chatgpt import RendyDevChat
from . import ultroid_cmd, eor, get_string

@ultroid_cmd(pattern="bi")
async def cas(e):
  reply = await e.get_reply_message()
  await e.eor(get_string("com_1"))

  text = reply.text
  code = RendyDevChat(text)

  answer_bing = await code.get_response_bing(bing=True)
  await e.reply(answer_bing)