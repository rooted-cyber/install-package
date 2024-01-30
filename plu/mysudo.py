# Ultroid - UserBot
# Copyright (C) 2021-2023 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.
"""
✘ Commands Available -

• `{i}asudo`
    Add Sudo Users by replying to user or using <space> separated userid(s)

• `{i}dsudo`
    Remove Sudo Users by replying to user or using <space> separated userid(s)

• `{i}lsudo`
    List all sudo users.

•  `{i}su`
     give all group members

•  `{i}ssuu`
     Add Sudo and fullsudo Users by replying
"""

from telethon.tl.types import User

from pyUltroid._misc import sudoers

from . import get_string, inline_mention, udB, ultroid_bot, ultroid_cmd, HNDLR


@ultroid_cmd(pattern="addsudo( (.*)|$)", fullsudo=True)
async def _(ult):
    inputs = ult.pattern_match.group(1).strip()
    if ult.reply_to_msg_id:
        replied_to = await ult.get_reply_message()
        id = replied_to.sender_id
        name = await replied_to.get_sender()
    elif inputs:
        try:
            id = await ult.client.parse_id(inputs)
        except ValueError:
            try:
                id = int(inputs)
            except ValueError:
                id = inputs
        try:
            name = await ult.client.get_entity(int(id))
        except BaseException:
            name = None
    elif ult.is_private:
        id = ult.chat_id
        name = await ult.get_chat()
    else:
        return await ult.eor(get_string("sudo_1"), time=5)
    if name and isinstance(name, User) and (name.bot or name.verified):
        return await ult.eor(get_string("sudo_4"))
    name = inline_mention(name) if name else f"`{id}`"
    if id == ultroid_bot.uid:
        mmm = get_string("sudo_2")
    elif id in sudoers():
        mmm = f"{name} `is already a SUDO User ...`"
    else:
        udB.set_key("SUDO", "True")
        key = sudoers()
        key.append(id)
        udB.set_key("SUDOS", key)
        mmm = f"**Added** {name} **as SUDO User**"
    await ult.eor(mmm, time=5)


@ultroid_cmd(pattern="dsudo( (.*)|$)", fullsudo=True)
async def _(ult):
    inputs = ult.pattern_match.group(1).strip()
    if ult.reply_to_msg_id:
        replied_to = await ult.get_reply_message()
        id = replied_to.sender_id
        name = await replied_to.get_sender()
    elif inputs:
        try:
            id = await ult.client.parse_id(inputs)
        except ValueError:
            try:
                id = int(inputs)
            except ValueError:
                id = inputs
        try:
            name = await ult.client.get_entity(int(id))
        except BaseException:
            name = None
    elif ult.is_private:
        id = ult.chat_id
        name = await ult.get_chat()
    else:
        return await ult.eor(get_string("sudo_1"), time=5)
    name = inline_mention(name) if name else f"`{id}`"
    if id not in sudoers():
        mmm = f"{name} `wasn't a SUDO User ...`"
    else:
        key = sudoers()
        key.remove(id)
        udB.set_key("SUDOS", key)
        mmm = f"**Removed** {name} **from SUDO User(s)**"
    await ult.eor(mmm, time=5)


@ultroid_cmd(
    pattern="lsudo$",
)
async def _(ult):
    sudos = sudoers()
    if not sudos:
        return await ult.eor(get_string("sudo_3"), time=5)
    msg = ""
    for i in sudos:
        try:
            name = await ult.client.get_entity(int(i))
        except BaseException:
            name = None
        if name:
            msg += f"• {inline_mention(name)} ( `{i}` )\n"
        else:
            msg += f"• `{i}` -> Invalid User\n"
    m = udB.get_key("SUDO") or True
    if not m:
        m = "[False](https://graph.org/Ultroid-04-06)"
    return await ult.eor(
        f"**SUDO MODE : {m}\n\nList of SUDO Users :**\n{msg}", link_preview=False
    )


from . import eor, SUDO_HNDLR
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
from os import mkdir, listdir as ls
from . import get_string, inline_mention, udB, ultroid_bot, ultroid_cmd, eor, SUDO_HNDLR


@ultroid_cmd(
    pattern="su$",
)
async def _(ult):
    x = await ult.eor("**Adding.....**")
    n = udB.get_key("SUDOS") or []
    async for m in ult.client.iter_participants(ult.chat_id):
      if not (m.bot or m.deleted):
        n.append(m.id)

    n = list(set(n))
    udB.set_key('SUDOS', n)
    udB.set_key('FULLSUDO', " ".join(str(i) for i in n))
    await x.edit(f"""
**Added FULLSUDO and SUDO in all group members**

HNDLR : {HNDLR}
SUDO_HNDLR : {SUDO_HNDLR}""")

    await ult.respond("**Now checking....**")
    sudos = sudoers()
    if not sudos:
        return await ult.eor(get_string("sudo_3"), time=5)
    msg = ""
    for i in sudos:
        try:
            name = await ult.client.get_entity(int(i))
        except BaseException:
            name = None
        if name:
            msg += f"• {inline_mention(name)} ( `{i}` )\n"
        else:
            msg += f"• `{i}` -> Invalid User\n"
    m = udB.get_key("SUDO") or True
    if not m:
        m = "[False](https://graph.org/Ultroid-04-06)"
        await ult.eor(
        f"**SUDO MODE : {m}\n\nList of SUDO Users :**\n{msg}", link_preview=False
    )

    if not "sudo":
      mkdir("sudo")

    if len(msg) > 4096:
       with open("list.txt","w") as ld:
         ld.write(f"{msg}")
    b,_ = await ult.client.fast_uploader(f"list.txt")
    c = await ult.client.send_file(ult.chat, b)
    #await ult.eor(c)

