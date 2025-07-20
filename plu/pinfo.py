from . import ultroid_cmd
from telethon import events
from telethon.tl.functions.contacts import ResolvePhoneRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.types import ChannelParticipantAdmin
from telethon.errors.rpcerrorlist import PhoneNotOccupiedError

@ultroid_cmd(pattern="pinfo ?(.*)")
async def numinfo(event):
    number = event.pattern_match.group(1)
    if not number:
        return await event.edit("give umber pinfo +918210268264")
    await event.edit("Fetching user info...")

    try:
        resolved = await event.client(ResolvePhoneRequest(phone=number))
        user = resolved.users[0]
        full = await event.client(GetFullUserRequest(user.id))
        bio = full.about if hasattr(full, "about") else "None"
        pfps = await event.client.get_profile_photos(user.id)

        # Try to get admin permissions if the bot is an admin in the group
        admin_info = ""
        try:
            participant = await event.client(GetParticipantRequest(
                channel=event.chat_id,
                user_id=user.id
            ))
            if isinstance(participant.participant, ChannelParticipantAdmin):
                admin = participant.participant
                admin_info = f"""
*Admin Permissions:*
Change Info = {'✅' if admin.change_info else '❌'}
Post Messages = {'✅' if admin.post_messages else '❌'}
Edit Messages = {'✅' if admin.edit_messages else '❌'}
Delete Messages = {'✅' if admin.delete_messages else '❌'}
Ban Users = {'✅' if admin.ban_users else '❌'}
Invite Users = {'✅' if admin.invite_users else '❌'}
Pin Messages = {'✅' if admin.pin_messages else '❌'}
"""
        except Exception as e:
            admin_info = ""  # No admin info if an error occurs

        msg = f"""
**• FIRST NAME:** {user.first_name or 'None'}
**• SECOND NAME:** {user.last_name or 'None'}
**• Bio:** {bio}
**• User ID:** {user.id}
**• Username:** @{user.username or 'None'}
**• DC ID:** {user.id % 64}
**• No. Of PFPs:** {len(pfps)}
**• Restricted:** {user.restricted}
**• Verified:** {user.verified}
**• Premium:** {getattr(user, 'premium', False)}
**• Is Bot:** {user.bot}
**Phone Number :** {number}
**Permanent link :** [click here](tg://user?id={user.id})
"""

        
              
        if pfps:
            await event.client.send_file(
                event.chat_id, pfps[0], caption=msg, reply_to=event.reply_to_msg_id
            )
            await event.delete()
        else:
            await eveht.edit(msg)

    except PhoneNotOccupiedError:
        await event.edit("No user found with this number.")
    except IndexError:
        await event.edit("No user data found.")
    except Exception as e:
        await event.edit(f"Error: {str(e)}")
