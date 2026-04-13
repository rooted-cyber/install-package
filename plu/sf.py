from . import *
import os
import subprocess
import time
import requests

@ultroid_cmd(pattern="sf( (.*)|$)")
async def sfupload(e):
    reply = await e.get_reply_message()

    if not reply or not reply.media:
        return await e.eor("⚠️ Reply to media")

    new_name = e.pattern_match.group(2)
    msg = await e.eor("📥 Downloading...")

    file_path = await reply.download_media()

    if not file_path:
        return await msg.edit("❌ Download fail")

    # rename
    if new_name:
        if "." not in new_name:
            new_name += os.path.splitext(file_path)[1]
        new_path = os.path.join(os.path.dirname(file_path), new_name)
        os.rename(file_path, new_path)
        file_path = new_path

    sf_user = "rootedcyber"
    sf_project = "rnx1941"
    private_key = os.path.expanduser("~/.ssh/id_ed25519")
    remote_dir = f"/home/frs/project/{sf_project}/"

    file_name = os.path.basename(file_path)
    link = f"https://downloads.sourceforge.net/project/{sf_project}/{file_name}"

    await msg.edit("📤 Uploading... (auto retry enabled)")

    # 🔁 RETRY SYSTEM
    success = False
    max_retry = 3

    for i in range(max_retry):
        cmd = [
            "sftp",
            "-i", private_key,
            f"{sf_user}@frs.sourceforge.net"
        ]

        sftp_cmd = f"put {file_path} {remote_dir}\nquit\n"

        result = subprocess.run(cmd, input=sftp_cmd, text=True)

        if result.returncode == 0:
            success = True
            break

        await msg.edit(f"⚠️ Retry {i+1}/{max_retry}...")

        time.sleep(2)

    if not success:
        return await msg.edit("❌ Upload failed after retries")

    # 🌐 LINK CHECK (instant verify)
    try:
        r = requests.head(link, timeout=5)
        if r.status_code != 200:
            return await msg.edit(
                f"⚠️ Upload done but link not active yet\n\n{link}"
            )
    except:
        pass

    await msg.edit(
        f"✅ Upload Successful!\n\n"
        f"📁 <code>{file_name}</code>\n"
        f"📎 <a href='{link}'>Download Link</a>",
        parse_mode="html"
    )

    try:
        os.remove(file_path)
    except:
        pass