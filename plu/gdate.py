from . import ultroid_cmd
from datetime import datetime

@ultroid_cmd(pattern="gdate$")
async def group_create_date(event):
    chat = await event.get_chat()
    if not hasattr(chat, "date"):
        return await event.eor("⚠️ This is not a valid group.")
    date = chat.date
    formatted_date = date.strftime("%d-%m-%Y %H:%M:%S")
    await event.eor(f"📅 Group Created On: `{formatted_date}`")
