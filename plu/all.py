from . import ultroid_cmd

@ultroid_cmd(pattern="all$")
async def count_messages(e):
    await e.eor("Processing...")
    n = ""
    async for m in e.client.iter_participants(e.chat_id):
        b = m.id
        c = f"[**{m.first_name}**](tg://user?id={b})"
        d = f"**{m.first_name}**"
        try:
            a = await e.client.get_messages(e.chat_id, limit=0, from_user=b)
            n += f"{c} : {a.total} msgs\n"
        except Exception as ex:
            print(f"Error fetching messages for {m.first_name}: {ex}")
    await e.eor(n or "No data found.",parse_mode="md")
    

from . import ultroid_cmd

@ultroid_cmd(pattern="total$")
async def count_messages(e):
    await e.eor("Processing...")
    n = ""
    total_msgs = 0
    user_count = 0
    reply = await e.get_reply_message()
    if reply:
      rp = await e.respond(inline_mention(reply.sender))
      rc = await e.client.get_messages(e.chat_id, limit=0, from_user=reply).total
      await e.eor("rp msgs = rc")
    async for m in e.client.iter_participants(e.chat_id):
        b = m.id
        name = f"[*{m.first_name}*](tg://user?id={b})"
        try:
            a = await e.client.get_messages(e.chat_id, limit=0, from_user=b)
            n += f"{name} : {a.total} msgs\n"
            total_msgs += a.total
            user_count += 1
        except Exception as ex:
            print(f"Error fetching messages for {m.first_name}: {ex}")

    if not n:
        await e.eor("No data found.")
    else:
        msg = f"{n}\n**Total Msgs:** `{total_msgs}`\n*Total Users:* `{user_count}`\n"
        await e.eor(msg, parse_mode="md")
