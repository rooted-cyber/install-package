from . import eor, SUDO_HNDLR, ultroid_cmd
from os import mkdir, listdir as ls
from pyUltroid.fns.helper import inline_mention
from . import HNDLR, get_string, inline_mention, udB, ultroid_bot, ultroid_cmd, eor, SUDO_HNDLR

@ultroid_cmd(pattern="sur")
async def szudo(e):
  reply = await e.get_reply_message()
  rid = "{}".format(reply.sender_id)
  udB.set_key("SUDOS",list(rid))
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
HNDLR : {HNDLR}
SUDO_HNDLR : {SUDO_HNDLR}
""")


from pyUltroid._misc import sudoers


@ultroid_cmd(
    pattern="su$",
)
async def _(ult):
    x = await ult.eor("**Adding sudo/fullsodo.....**")
    n = udB.get_key("SUDOS") or []
    async for m in ult.client.iter_participants(ult.chat_id):
      if not (m.bot or m.deleted):
        n.append(m.id)

    n = list(set(n))
    udB.set_key('SUDOS', n)
    udB.set_key('FULLSUDO', " ".join(str(i) for i in n))
    await x.edit("**List of sudo users**\n1.All members in this group")
