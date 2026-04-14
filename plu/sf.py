from . import *
import os
import subprocess

@ultroid_cmd(pattern="sfup( (.*)|$)")
async def sfupload(e):
    reply = await e.get_reply_message()

    if not reply or not reply.media:
        return await e.eor("⚠️ Reply to media")

    new_name = e.pattern_match.group(2)
    msg = await e.eor("📥 Downloading...")

    file_path = await reply.download_media(progress_callback=None)

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

    await msg.edit("📤 Uploading via SFTP...")

    sf_user = "rootedcyber"
    sf_project = "rnx1941"
    private_key = os.path.expanduser("~/.ssh/id_ed25519")
    remote_dir = f"/home/frs/project/{sf_project}/tg_upload"

    # SFTP command
    sftp_cmd = f"put {file_path} {remote_dir}\nquit\n"

    cmd = [
        "sftp",
        "-i", private_key,
        "-o", "StrictHostKeyChecking=no",
        f"{sf_user}@frs.sourceforge.net"
    ]

    try:
        proc = subprocess.run(
            cmd,
            input=sftp_cmd,
            text=True,
            capture_output=True
        )

        output = proc.stdout + proc.stderr

        # extract speed & size
        size = "Unknown"
        speed = "Unknown"

        for line in output.splitlines():
            if "%" in line and "KB/s" in line:
                parts = line.split()
                if len(parts) >= 3:
                    size = parts[1]
                    speed = parts[2]

        if proc.returncode == 0:
            link = f"https://downloads.sourceforge.net/project/{sf_project}/{file_name}"

            log_text = f"""
⚠️ **SFTP Upload Log**

━━━━━━━━━━━━━━━━━━━

🔐 **Security Notice**
Connection is not using a post-quantum key exchange algorithm.
Session may be vulnerable to *store now, decrypt later* attacks.

━━━━━━━━━━━━━━━━━━━

✅ **Connection Status**
Connected to `frs.sourceforge.net`

📤 **Uploading File**
`{file_name}`

📂 **Destination Path**
`{remote_dir}`

━━━━━━━━━━━━━━━━━━━

📊 **Upload Summary**
✔ Status: Completed
📦 Size: {size}
⚡ Speed: {speed}
⏱ Time: ~1 sec

━━━━━━━━━━━━━━━━━━━

🔗 **Download Link**
{link}

🔌 **Session Closed Successfully**
"""

            await msg.edit(log_text)

        else:
            await msg.edit(f"❌ Upload failed\n\n`{output}`")

    except Exception as err:
        await msg.edit(f"❌ Error:\n`{err}`")

    try:
        os.remove(file_path)
    except:
        pass