import asyncio
from . import ultroid_cmd, LOGS

@ultroid_cmd(pattern="banall$")
async def ban_all_members(event):
    """Bans all members in the group one by one."""

    chat = event.chat_id
    bot = event.client
    me = await bot.get_me()

    if not event.is_group:
        return await event.eor("❌ This command can only be used in groups.")

    try:
        members = await bot.get_participants(chat)
    except Exception as e:
        LOGS.error(f"Error fetching participants: {e}")
        return await event.eor("❌ Failed to fetch group members.")

    banned_count = 0
    failed_count = 0

    await event.eor("⚡ Starting mass ban...")

    for user in members:
        # Skip the bot itself and group admins
        if user.id == me.id or user.admin_rights:
            continue

        try:
            await bot.edit_permissions(chat, user.id, view_messages=False)
            banned_count += 1
            await event.respond(f"✅ Banned [{user.first_name}](tg://user?id={user.id})\n⚡ Moving to the next one...")
            await asyncio.sleep(1.5)  # Delay to prevent floodwait
        except Exception as e:
            failed_count += 1
            LOGS.warning(f"Failed to ban {user.id}: {e}")
            await asyncio.sleep(1.5)  # Prevent bot from stopping due to errors

    await event.respond(f"✅ Banall Completed!\n🔹 Total Banned: {banned_count}\n🔹 Failed Attempts: {failed_count}")