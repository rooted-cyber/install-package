from . import ultroid_cmd
from telethon import events

@ultroid_cmd(pattern="amc$")
async def group_msg_counter(event):
    await event.edit("📊 Starting count...")

    # Get all group dialogs
    dialogs = [d async for d in event.client.iter_dialogs() if d.is_group]
    total_groups = len(dialogs)
    done = 0
    result = "Your 📊 Message Count in Groups\n\n"
    total_msgs = 0

    await event.edit("🔄 Counting...\n[░░░░░░░░░░] 0%")  # Initial progress bar

    for dialog in dialogs:
        count = 0
        try:
            # Count messages from the user in the current dialog
            async for msg in event.client.iter_messages(dialog.id, from_user='me'):
                count += 1
            total_msgs += count  # Correctly accumulate the message count
            result += f"• {dialog.name}: {count}\n"
        except Exception as e:
            result += f"• {dialog.name}: Error accessing messages\n"

        done += 1

        # Update progress bar
        percent = int((done / total_groups) * 100)
        bar = "▓" * (percent // 10) + "░" * (10 - (percent // 10))
        await event.edit(f"🔄 Counting...\n[{bar}] {percent}%\n\nCompleted: {done}/{total_groups} groups")

    result += f"\n🧮 Your total Messages in All Groups: {total_msgs}"
    await event.edit(result or "No messages found.")
