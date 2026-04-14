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
    remote_dir = f"/home/frs/project/{sf_project}/"

    # SFTP upload
    sftp_cmd = f"put {file_path} {remote_dir}/tg_upload\nquit\n"

    cmd = [
        "sftp",
        "-i", private_key,
        "-o", "StrictHostKeyChecking=no",
        f"{sf_user}@frs.sourceforge.net"
    ]

    result = subprocess.run(cmd, input=sftp_cmd, text=True)

    if result.returncode == 0:
        link = f"https://downloads.sourceforge.net/project/{sf_project}/{file_name}"

        await msg.edit(
            f"✅ Upload Done!\n\n"
            f"📁 <code>{file_name}</code>\n"
            f"📎 <a href='{link}'>Download</a>",
            parse_mode="html"
        )
    else:
        await msg.edit("❌ Upload failed")

    try:
        os.remove(file_path)
    except:
        pass