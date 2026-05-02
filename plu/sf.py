from . import *
import os
import subprocess
import time
import re

@ultroid_cmd(pattern="sfup( (.*)|$)")
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

    file_name = os.path.basename(file_path)

    await msg.edit("📤 Starting upload...")

    sf_user = "rootedcyber"
    sf_project = "rnx1941"
    private_key = os.path.expanduser("~/.ssh/id_ed25519")
    remote_dir = f"/home/frs/project/{sf_project}/tg_upload"

    # start time
    start_time = time.time()

    cmd = [
        "sftp",
        "-i", private_key,
        "-o", "StrictHostKeyChecking=no",
        f"{sf_user}@frs.sourceforge.net"
    ]

    process = subprocess.Popen(
        cmd,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1
    )

    process.stdin.write(f"put {file_path} {remote_dir}\n")
    process.stdin.write("quit\n")
    process.stdin.flush()

    total_size = os.path.getsize(file_path) / 1024  # KB
    last_update = 0

    percent = 0
    speed = "0 KB/s"

    for line in process.stdout:
        if "%" in line:
            try:
                percent = int(re.search(r'(\d+)%', line).group(1))

                uploaded = (percent / 100) * total_size
                elapsed = time.time() - start_time

                if elapsed > 0:
                    current_speed = uploaded / elapsed
                    speed = f"{current_speed:.1f} KB/s"

                # ⏱ limit edits (avoid flood)
                if time.time() - last_update > 2:
                    bar = "█" * (percent // 10) + "░" * (10 - percent // 10)

                    await msg.edit(
                        f"📤 **Uploading...**\n\n"
                        f"📁 `{file_name}`\n"
                        f"📊 [{bar}] {percent}%\n"
                        f"⚡ Speed: {speed}"
                    )
                    last_update = time.time()

            except:
                pass

    process.wait()

    # fallback size
    size_kb = round(total_size)

    link = f"https://downloads.sourceforge.net/project/{sf_project}/{file_name}"

    final_text = f"""
⚠️ **SFTP Upload Log**

━━━━━━━━━━━━━━━━━━━

🔐 **Security Notice**
Connection is not using a post-quantum key exchange algorithm.
Session may be vulnerable to *store now, decrypt later* attacks.

━━━━━━━━━━━━━━━━━━━

✅ **Connection Status**
Connected to `frs.sourceforge.net`

📤 **Uploaded File**
`{file_name}`

📂 **Path**
`{remote_dir}`

━━━━━━━━━━━━━━━━━━━

📊 **Upload Summary**
✔ Status: Completed
📦 Size: {size_kb} KB
⚡ Avg Speed: {speed}
⏱ Time: {round(time.time() - start_time)} sec

━━━━━━━━━━━━━━━━━━━

🔗 **Download Link**
{link}

🔌 **Session Closed Successfully**
"""

    await msg.edit(final_text)

    try:
        os.remove(file_path)
    except:
        pass