from . import *
import os
import subprocess
from telethon.tl.types import MessageMediaDocument

@ultroid_cmd(pattern="sf$")
async def sfupload(e):
    reply = await e.get_reply_message()

    if not reply or not reply.media or not isinstance(reply.media, MessageMediaDocument):
        return await e.eor("⚠️ कृपया किसी file/document पर reply करें।")

    await e.eor("📥 फ़ाइल डाउनलोड हो रही है...")

    file_path = await reply.download_media()

    if not file_path or not os.path.isfile(file_path):
        return await e.eor("❌ डाउनलोड विफल हो गया।")

    # 🔧 CONFIG (edit these)
    sf_user = "rootedcyber"
    sf_project = "rnx1941"
    private_key_path = os.path.expanduser("~/.ssh/id_rsa")  # ✅ FIXED

    remote_dir = f"/home/frs/project/{sf_project}/"
    file_name = os.path.basename(file_path)

    await e.eor("📤 SourceForge पर अपलोड हो रहा है...")

    # 🚀 SCP upload with error capture
    cmd = [
        "scp",
        "-i", private_key_path,
        file_path,
        f"{sf_user}@frs.sourceforge.net:{remote_dir}"
    ]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode == 0:
            link = f"https://downloads.sourceforge.net/project/{sf_project}/{file_name}"
            await e.eor(f"✅ Upload successful!\n📎 Download: [Click here]({link})")
        else:
            await e.eor(f"❌ Upload failed!\n\nError:\n{result.stderr}")

    except Exception as ex:
        await e.eor(f"❌ Exception आया:\n{str(ex)}")
