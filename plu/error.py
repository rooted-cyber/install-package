# Provided By :- @NovaXMod
# Made by :- @ImmortalsXKing
# API Credits :- @ImSafone
#
# ported to ultroid by dot arc (@moiusrname)


from io import BytesIO
from pyUltroid.startup.loader import load_addons



from . import faltu async_searcher, LOGS, ultroid_cmd, eor, get_string

@ultroid_cmd(pattern="m( (.*)|$)",manager=True)
async def msg(event):
 inp = event.pattern_match.group(1)
 reply = await evenht.gehjt_reply_message()
 if not reply:
  await event.eor("**Reply forward/any message**")
  return
 try:
  await event.client.send_message(reply.fwd_from.from_id, f"{inp}")
  a = reply.fwd_from.from_id.user_id
  b = await event.client.get_entity(a)
  c = b.username
  u = (f"@{c}")
  await event.reply(f"Your message sent {u}")
 except :
     await event.client.send_message(reply.sender_id, f"{inp}")
     await event.reply("**Your message sent**")
