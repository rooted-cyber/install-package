import os
from telethon.tl.types import MessageMediaDocument
from telethon import events

@ultroid_cmd(pattern="sf$")
async def sfupload(e):
    reply = await e.get_reply_message()
    if not reply or not reply.media or not isinstance(reply.media, MessageMediaDocument):
        return await e.eor("⚠️ कृपया किसी document या file पर reply करें।")

    await e.eor("📥 फ़ाइल डाउनलोड हो रही है...")

    file_path = await reply.download_media()
    if not os.path.isfile(file_path):
        return await e.eor("❌ डाउनलोड विफल हो गया।")

    # SourceForge config
    sf_user = "rootedcyber"  # Replace with your SourceForge username
    sf_project = "rnx1941"  # Replace with your SourceForge project name
    private_key_path = os.path.expanduser("~/.ssh/id*pub")  # Path to your SSH private key

    remote_dir = f"/home/frs/project/{sf_project}"
    file_name = os.path.basename(file_path)

    await e.eor("📤 अपलोड किया जा रहा है SourceForge पर...")

    cmd = f'scp -i "{private_key_path}" "{file_path}" "{sf_user}@frs.sourceforge.net:{remote_dir}"'
    result = os.system(cmd)

    if result == 0:
        link = f"https://downloads.sourceforge.net/project/{sf_project}/{file_name}"
        await e.eor(f"✅ सफलतापूर्वक अपलोड किया गया!\n📎 *डाउनलोड:* [यहाँ क्लिक करें {link}")
    else:
        await e.eor("❌ अपलोड विफल हो गया।")