from telethon import events, TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors.rpcerrorlist import UserAlreadyParticipantError

# Ensure your bot variable is defined and correctly initialized somewhere in your main script
# For demonstration, ensure 'bot' is the actual instantiated and logged-in TelegramClient

@bot.on(events.NewMessage(pattern=r"\.join (.+)"))
async def join_channel_or_group(event):
    input_str = event.pattern_match.group(1)

    try:
        # Check if the input is a complete invite link or just a username
        if input_str.startswith('https://t.me/'):
            # Extract the invite hash or username
            input_str = input_str.split('/')[-1]

        await bot(JoinChannelRequest(input_str))
        await event.respond(f"Successfully joined {input_str}. Created by @pragyan.")
    except UserAlreadyParticipantError:
        await event.respond(f"You're already a member of {input_str}. Created by @pragyan.")
    except Exception as e:
        await event.respond(f"Failed to join {input_str}. Error: {str(e)}. Created by @pragyan.")