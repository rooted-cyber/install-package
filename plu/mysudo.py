from . import eor, SUDO_HNDLR, ultroid_cmd, get_string, eor, bash, inline_mention, LOGS, udB

@ultroid_cmd(pattern="ssuu")
async def szudo(e):
  reply = await e.get_reply_message()
  rid = reply.sender_id
  udB.set_key("SUDOS",rid)
  udB.set_key("FULLSUDO",rid)
  name = await e.client.get_entity(int(rid))
  una = name.username
  fn = name.first_name
  ln = name.last_name
  men = inline_mention(name)
  ii = udB.get_key("FULLSUDO")
  await e.reply(f"""**Added** {men} **as FULLSUDO and SUDO User**
First name : {fn}
Last name : {ln}
id : {ii}
username : {una}
SUDO_HNDLR : {SUDO_HNDLR}
""")