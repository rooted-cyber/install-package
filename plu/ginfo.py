from . import ultroid_cmd

@ultroid_cmd(pattern="ginfo$")
async def grp_info(e):
    chat = e.chat

    msg = f"""*📑 Group Info*
*Title:* {chat.title}
**ID:** {chat.id}
**Type:* {'Megagroup' if getattr(chat, 'megagroup', False) else 'Group/Channel'}
**Username:** @{chat.username if chat.username else 'None'}
**Verified:** {chat.verified}
**Restricted:** {chat.restricted}
**Scam:** {chat.scam}
"""
    await e.reply(msg)
