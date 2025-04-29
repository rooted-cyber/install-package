from . import ultroid_cmd
from telethon import events

@ultroid_cmd(pattern="amcount$")
async def group_msg_counter(event):
    await event.edit("📊 Starting count...")

    dialogs = [d async for d in event.client.iter_dialogs() if d.is_group]
    total_groups = len(dialogs)
    done = 0
    result = "*📊 Message Count in Groups*\n\n"
    total_msgs = 0

    for dialog in dialogs:
        count = 0
        async for msg in event.client.iter_messages(dialog.id, from_user='me'):
            count += 1
        total_msgs += count
        result += f"• {dialog.name}: {count}\n"
        done += 1

        # Progress bar text
        percent = int((done / total_groups) * 100)
        bar = "▓" * (percent // 10) + "░" * (10 - (percent // 10))
        await event.edit(f"🔄 Counting...\n\n\n[{bar}] {percent}%\n\nCompleted: {done}/{total_groups} groups")

    result += f"\n🧮 *Total Messages in All Groups:* {total_msgs}"
    await event.edit(result or "No messages found.")
