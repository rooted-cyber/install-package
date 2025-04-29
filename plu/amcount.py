from . import ultroid_cmd
from telethon import events

@ultroid_cmd(pattern="amcount$")
async def group_msg_counter(event):
    await event.edit("📊 Counting messages in all groups... (this may take a while)")
    result = "*📊 Message Count in Groups*\n\n"
    total = 0

    async for dialog in event.client.iter_dialogs():
        if dialog.is_group:
            count = 0
            async for msg in event.client.iter_messages(dialog.id, from_user='me'):
                count += 1
            total += count
            result += f"• {dialog.name}: {count}\n"

    result += f"\n🧮 *Total Messages in All Groups:* {total}"
    await event.edit(result or "No messages found.")
