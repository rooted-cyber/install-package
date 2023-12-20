from pyUltroid._misc import sudoers
from os import mkdir, listdir as ls
from . import get_string, inline_mention, udB, ultroid_bot, ultroid_cmd, eor, HNDLR


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
    #udB.set_key('FULLSUDO', " ".join(str(i) for i in n))
    await x.edit(f"𝗦𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆 𝗮𝗱𝗱𝗲𝗱 𝗦𝗨𝗗𝗢")

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
