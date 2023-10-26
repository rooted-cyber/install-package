from . import eor, ultroid_cmd, get_string, bash, LOGS

@ultroid_cmd(pattern="t$")
async def ed(e):
  await e.eor(get_string("com_1"))
  a = await e.client.get_participants(e.chat_id)
  for b in a:
    c = b.username
    d = f"@{c}  >> hi"
    await e.respond(d)