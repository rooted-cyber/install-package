from telethon import events
from telethon.tl.types import ChannelParticipantCreator
from telethon.tl.functions.channels import GetParticipantsRequest

@ultroid_cmd(pattern="gowner$")
async def gowner(event):
    grp = await event.get_input_chat()
    users = await event.client(GetParticipantsRequest(grp, ChannelParticipantsAdmins(), 0, 100, 0))
    for user in users.participants:
        if isinstance(user, ChannelParticipantCreator):
            u = await event.client.get_entity(user.user_id)
            return await event.reply(f"👑 Owner: [{u.first_name}](tg://user?id={u.id})")
    await event.reply("Owner nahi mila.")#from . import ultroid_cmd
#from pyUltroid.fns.helper import inline_mention
# Ultroid - UserBot
# Copyright (C) 2021-2025 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.
"""
✘ Commands Available -

• `{i}tagall`
    Tag Top 100 Members of chat.

• `{i}tagadmins`
    Tag Admins of that chat.

• `{i}tagowner`
    Tag Owner of that chat

• `{i}tagbots`
    Tag Bots of that chat.

• `{i}tagrec`
    Tag recently Active Members.

• `{i}tagon`
    Tag online Members(work only if privacy off).

• `{i}tagoff`
    Tag Offline Members(work only if privacy off).
"""

from telethon.tl.types import ChannelParticipantAdmin as admin
from telethon.tl.types import ChannelParticipantCreator as owner
from telethon.tl.types import UserStatusOffline as off
from telethon.tl.types import UserStatusOnline as onn
from telethon.tl.types import UserStatusRecently as rec

from . import inline_mention, ultroid_cmd


@ultroid_cmd(
    pattern="tag(on|off|all|bots|rec|admins|owner)( (.*)|$)",
    groups_only=True,
)
async def _(e):
    okk = e.text
    lll = e.pattern_match.group(2)
    o = 0
    nn = 0
    rece = 0
    xx = f"{lll}" if lll else ""
    lili = await e.client.get_participants(e.chat_id, limit=99)
    for bb in lili:
        x = bb.status
        y = bb.participant
        if isinstance(x, onn):
            o += 1
            if "on" in okk:
                xx += f"\n{inline_mention(bb)}"
        elif isinstance(x, off):
            nn += 1
            if "off" in okk and not bb.bot and not bb.deleted:
                xx += f"\n{inline_mention(bb)}"
        elif isinstance(x, rec):
            rece += 1
            if "rec" in okk and not bb.bot and not bb.deleted:
                xx += "Recently user\n"
                xx += f"\n{inline_mention(bb)}"
        if isinstance(y, owner):
            xx += f"\n꧁{inline_mention(bb)}꧂"
        if isinstance(y, admin) and "admin" in okk and not bb.deleted:
            xx += f"\n{inline_mention(bb)}"
        if "all" in okk and not bb.bot and not bb.deleted:
            xx += f"\n{inline_mention(bb)}"
        if "bot" in okk and bb.bot:
            xx += f"\n{inline_mention(bb)}"
    await e.eor(xx)

@ultroid_cmd(pattern="tag$",manager=True)
async def hi(event):
  reply = await event.get_reply_message()
  if reply:
    await event.respond(inline_mention(reply.sender))
  else:
    await event.respond(inline_mention(event.sender))
