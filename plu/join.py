"""
────────────────────────────────────────────────────────
✨       Telegram Join Script by Charlie        ✨
────────────────────────────────────────────────────────

🔗 This script enables the user to join Telegram channels 
   and groups via invite links using the Telethon library.

🌟 Features:
  - Handles both private and public group join requests.
  - Provides error messages for invalid or expired links.
  - Informs if the user is already a member of the group.

👨‍💻 Developed and maintained by:
   Charlie

🔒 Copyright © 2023 Charlie
   All rights reserved. Unauthorized copying is prohibited.

────────────────────────────────────────────────────────
"""

from telethon.errors.rpcerrorlist import UserAlreadyParticipantError, InviteHashExpiredError
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.channels import JoinChannelRequest
from . import ultroid_cmd

@ultroid_cmd(pattern="j (.+)")
async def ultroid_join(event):
    join_link = event.pattern_match.group(1)

    try:
        if join_link.startswith('https://t.me/+'):
            invite_hash = join_link.replace("https://t.me/+", "")
            try:
                await event.client(ImportChatInviteRequest(invite_hash))
                await event.eor("✅ Successfully joined the private group!")
            except InviteHashExpiredError:
                await event.eor("❌ The invite link is expired or invalid.")
        else:
            if join_link.startswith('https://t.me/'):
                join_link = join_link.split('/')[-1]

            await event.client(JoinChannelRequest(join_link))
            await event.eor(f"✅ Successfully joined {join_link}!")
    except UserAlreadyParticipantError:
        await event.eor(f"⚠️ You're already a member of {join_link}.")
    except Exception as e:
        await event.eor(f"❌ Failed to join {join_link}. Error: {str(e)}.")