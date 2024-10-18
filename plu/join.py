from telethon import events, TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors.rpcerrorlist import UserAlreadyParticipantError
from . import *
@ultroid_cmd(pattern="j( (.*)")
async def join_channel_or_group(event):
    input_str = event.pattern_match.group(1)
    li = input_str
    try:
        await bot(JoinChannelRequest(f"{li}"))
        await event.respond(f"**Successfully joined** \n {input_str}")
    except UserAlreadyParticipantError:
        await event.respond(f"You're already a member of {input_str}.")
    except Exception as e:
        await event.respond(f"Failed to join {input_str}. Error: {str(e)}")
