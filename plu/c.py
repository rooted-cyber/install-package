# Ported From DarkCobra , Originally By Uniborg
# Ultroid - UserBot
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

"""
✘ Commands Available

• `{i}clone <reply/username>`
    clone the identity of user.

• `{i}revert`
    Revert to your original identity
"""

import html

from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.photos import DeletePhotosRequest, UploadProfilePhotoRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName

from . import *


@ultroid_cmd(pattern="c ?(.*)")
async def _(event):
    eve = await event.eor("`Processing...`")
    reply_message = await event.get_reply_message()
    whoiam = await event.client(GetFullUserRequest(ultroid_bot.uid))
    if whoiam.full_user.about:
        mybio = str(ultroid_bot.me.id) + "01"
        udB.set_key(f"{mybio}", whoiam.full_user.about)  # saving bio for revert
    udB.set_key(f"{ultroid_bot.uid}02", whoiam.users[0].first_name)
    if whoiam.users[0].last_name:
        udB.set_key(f"{ultroid_bot.uid}03", whoiam.users[0].last_name)
    replied_user, error_i_a = await get_full_user(event)
    if replied_user is None:
        await eve.edit(str(error_i_a))
        return
    user_id = replied_user.users[0].id
    first_name = html.escape(replied_user.users[0].first_name)
    if first_name is not None:
        first_name = first_name.replace("\u2060", "")
    last_name = replied_user.users[0].last_name
    if last_name is not None:
        last_name = html.escape(last_name)
        last_name = last_name.replace("\u2060", "")
    if last_name is None:
        last_name = "⁪⁬⁮⁮⁮"
    #user_bio = replied_user.full_user.about
    file = await event.client.upload_file(reply_message)
    await event.client(UploadProfilePhotoRequest(file=file))
    await event.client(UpdateProfileRequest(first_name=first_name))
    await event.client(UpdateProfileRequest(last_name=last_name))
    #await event.client(UpdateProfileRequest(about=user_bio))
    await eve.delete()
    await event.client.send_message(
        event.chat_id, f"**I am `{first_name}` from now...**", reply_to=reply_message
    )

