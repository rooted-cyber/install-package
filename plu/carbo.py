try:
  from RyuzakiLib.extreme.rayso import CarbonRaySo
except:
  import os
  os.system("pip3 install -U RyuzakiLib")
  from RyuzakiLib.extreme.rayso import CarbonRaySo
from . import ultroid_cmd, eor, get_string

@ultroid_cmd(pattern="ca")
async def ca(e):
  reply = await e.get_reply_message()
  await e.eor(get_string("com_1"))
  code = "".join(reply.text)
  theme = "breeze"
    
  code = CarbonRaySo(code=code,theme=theme,auto_translate=True,check_sticker=False,ryuzaki=True)
  beautiful = code.make_carbon_rayso()
  await e.respond(file=beautiful)