from . import ultroid_cmd, get_string
from pyUltroid._misc._supporter import bot
#@ultroid_cmd(pattern="sm( (.*)|$)",manager=True)
#async def chht(e):
from telethon import events
@bot.on(events.NewMessage(pattern="sm( (.*)|$)",incoming=True,outgoing=True))
async def hi(e):
  a = e.pattern_match.group(1).strip()
  reply = await e.get_reply_message()
  if not a:
    if reply and reply.text:
            a = reply.message
  if not a:
      return await e.eor("Kuch likho")
      
  await e.eor(get_string("com_1"))
  
  if reply:
    await reply.edit(f"{a}")
  else:
    await e.respond(f"{a}")
    
