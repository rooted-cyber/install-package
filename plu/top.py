"""
✘ Commands Available -

• `{i}top <limit> <dd-mm-yy>`
    Display the leaderboard of the most active chat members based on message count.
    - `<limit>` (optional): Number of top users to show.
    - `<dd-mm-yy>` (optional): Show leaderboard for messages sent on a specific date.

Examples:

• `{i}top`
    Show the full leaderboard by total messages sent.

• `{i}top 10`
    Show the top 10 most active users by total messages.

• `{i}top 01-06-25`
    Show leaderboard for messages sent on June 1, 2025.

• `{i}top 5 01-06-25`
    Show the top 5 most active users on June 1, 2025.
"""



from datetime import datetime, timedelta
from collections import defaultdict
from . import ultroid_cmd
from telethon.utils import get_display_name
from pyUltroid.fns.tools import make_html_telegraph

@ultroid_cmd(pattern=r"top(?:\s+(\d+))?(?:\s+([\w\-]+))?$")
async def top_leaderboard_handler(event):
    chat = await event.get_input_chat()
    limit_arg = event.pattern_match.group(1)
    date_arg = (event.pattern_match.group(2) or "").strip().lower()

    member_count = 0
    try:
        async for user in event.client.iter_participants(chat):
            if not getattr(user, "bot", False) and not getattr(user, "deleted", False):
                member_count += 1
                if member_count >= 100:
                    await event.eor("`This command is disabled for groups with 100 or more members.`")
                    return
    except Exception:
        pass

    limit = int(limit_arg) if limit_arg and limit_arg.isdigit() else member_count

    if limit >= 100:
        await event.eor("`This command is disabled for groups with 100 or more members or limit >= 100.`")
        return

    mode = "messages"
    filter_date = None

    if date_arg:
        for fmt in ("%d-%m-%y", "%d-%m-%Y"):
            try:
                filter_date = datetime.strptime(date_arg, fmt).date()
                mode = "date"
                break
            except ValueError:
                continue
        else:
            return await event.eor("`Invalid date format. Use: dd-mm-yy or dd-mm-yyyy (e.g., 01-06-25)`")

    date_text = f" on {filter_date.strftime('%d-%m-%Y')}" if filter_date else ""
    await event.eor(f"`Gathering message activity leaderboard for top {limit} users{date_text}...`")

    user_counts = defaultdict(int)

    try:
        async for user in event.client.iter_participants(chat):
            if getattr(user, "bot", False) or getattr(user, "deleted", False):
                continue

            try:
                if mode == "messages":
                    count = (await event.client.get_messages(chat, from_user=user.id, limit=0)).total

                elif mode == "date":
                    count = 0
                    cutoff = datetime.combine(filter_date + timedelta(days=1), datetime.min.time())
                    async for msg in event.client.iter_messages(chat, from_user=user.id, reverse=False, offset_date=cutoff):
                        if msg.date.date() == filter_date:
                            count += 1
                        elif msg.date.date() < filter_date:
                            break

                if count > 0:
                    user_counts[user.id] = count

                if len(user_counts) >= limit * 2:
                    break

            except Exception:
                continue

        if not user_counts:
            return await event.eor("`No messages found matching the criteria.`")

        sorted_users = sorted(user_counts.items(), key=lambda x: x[1], reverse=True)[:limit]

        lines = []
        for rank, (user_id, count) in enumerate(sorted_users, start=1):
            try:
                user_entity = await event.client.get_entity(user_id)
                display_name = get_display_name(user_entity) or "Anonymous"
            except Exception:
                display_name = "Unknown"
            lines.append(f"{rank}. {display_name} - {count}")

        output_text = f"🏆 Top {limit} Most Active Users{date_text}\n\n" + "\n".join(lines)

        if len(output_text) > 4095:
            content_lines = [
                f"<p><b>{rank}. {get_display_name(await event.client.get_entity(user_id)) or 'Anonymous'}</b> — {count} messages</p>"
                for rank, (user_id, count) in enumerate(sorted_users, start=1)
            ]
            html_content = f"<p><strong>🏆 Chat Activity Leaderboard</strong></p>" + "".join(content_lines)
            title = f"Top {limit} Most Active Members{date_text}"
            url = await make_html_telegraph(title, html_content)
            if url:
                await event.eor(f"Leaderboard is too long, view it here: [Telegraph]({url})", link_preview=True)
            else:
                await event.eor("`Failed to create telegraph page.`")
        else:
            await event.eor(f"```\n{output_text}\n```")


    except Exception as e:
        await event.eor(f"`An error occurred while generating the leaderboard: {str(e)}`")