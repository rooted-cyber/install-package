from . import ultroid_cmd, inline_mention

@ultroid_cmd("rc$")
async def count_messages(e):
    await e.eor("Processing...")
    n = ""
    total_msgs = 0
    user_count = 0
    reply = await e.get_reply_message()
    if reply:
      rp = inline_mention(reply.sender)
      rc = await e.client.get_messages(e.chat_id, limit=0, from_user=reply.sender_id)
      return await e.eor(f"{rp} msgs = {rc.total} msgs")
    async for m in e.client.iter_participants(e.chat_id):
        b = m.id
        name = f"[{m.first_name}](tg://user?id={b})"
        try:
            a = await e.client.get_messages(e.chat_id, limit=0, from_user=b)
            n += f"**{name}** : {a.total} msgs\n"
            total_msgs += a.total
            user_count += 1
        except Exception as ex:
            print(f"Error fetching messages for {m.first_name}: {ex}")

    if not n:
        await e.eor("No data found.")
    else:
        msg = f"{n}\n**Total Msgs:** `{total_msgs}`\n*Total Users:* `{user_count}`\n"
        await e.eor(msg, parse_mode="md")
