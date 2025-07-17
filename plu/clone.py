from telethon.tl.functions.photos import UploadProfilePhotoRequest
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.users import GetFullUserRequest
import os

@ultroid_cmd(pattern="cl ?(.*)")
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

        # Profile photo clone
        if user.photo:
            photo = await event.client.download_profile_photo(user, file="clone.jpg")
            await event.client(UploadProfilePhotoRequest(file=await event.client.upload_file(photo)))
            os.remove(photo)

        await event.edit(f"Cloned {user.first_name} successfully.")

    except Exception as e:
        await event.edit(f"Error: {e}")
