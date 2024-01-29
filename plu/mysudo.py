from . import eor, ultroid_cmd, get_string, eor, bash, inline_mention, LOGS, udB

@ultroid_cmd(pattern="ssuu")
async def szudo(e):
  reply = await e.get_reply_message()
  rid = reply.sender_id
  a = udB.set_key("SUDOS",rid)
  b = udB.set_key("FULLSUDO",rid)
  name = await e.client.get_entity(int(rid))
  men = inline_mention(name)
  await e.reply(f"**Added** {men} **as FULLSUDO and SUDO User**")