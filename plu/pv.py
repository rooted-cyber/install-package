@ultroid_cmd(pattern="pv( (.*)|$)",manager=True)
async def msg(event):
 inp = event.pattern_match.group(1)
 reply = await event.get_reply_message()
 if not reply:
  await event.eor("Reply forward message")
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