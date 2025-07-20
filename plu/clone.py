from telethon.tl.functions.photos import UploadProfilePhotoRequest
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.users import GetFullUserRequest
import os
from . import ultroid_cmd

@ultroid_cmd(pattern="c ?(.*)")
async def clone_user(event):
    reply = await event.get_reply_message()
    user = event.pattern_match.group(1)

    if not reply and not user:
        return await event.edit("Reply ya username/id do.")

    try:
        user = await event.client.get_entity(user or reply.sender_id)
        full = await event.client(GetFullUserRequest(user.id))

        # Name and bio clone
        await event.client(UpdateProfileRequest(
            first_name=user.first_name or "",
            last_name=user.last_name or ""
        ))

        await event.edit(f"Cloned {user.first_name} successfully.")

    except Exception as e:
        await event.edit(f"Error: {e}")
