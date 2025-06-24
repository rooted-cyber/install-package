from . import ultroid_cmd

@ultroid_cmd(pattern="all$")
async def count_messages(e):
    await e.eor("Processing...")
    n = ""
    async for m in e.client.iter_participants(e.chat_id):
        b = m.id
        c = f"[**{m.first_name}**](tg://user?id={b}"
        d = f"**{m.first_name}**"
        try:
            a = await e.client.get_messages(e.chat_id, limit=0, from_user=b)
            n += f"*{m.first_name}*{c} : {a.total} msgs\n"
        except Exception as ex:
            print(f"Error fetching messages for {m.first_name}: {ex}")
    await e.eor(n or "No data found.")
