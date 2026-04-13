from . import *
import os
import subprocess

@ultroid_cmd(pattern="sf( (.*)|$)")
async def sfupload(e):
    reply = await e.get_reply_message()

    if not reply or not reply.media:
        return await e.eor("⚠️ Media par reply karo")

    new_name = e.pattern_match.group(2)

    msg = await e.eor("📥 Processing...")

    file_path = await reply.download_media(progress_callback=None)

    if not file_path:
        return await msg.edit("❌ Download fail")

    file_name = os.path.basename(file_path)

    # rename fix
    if new_name:
        if "." not in new_name:
            new_name += os.path.splitext(file_path)[1]
        new_path = os.path.join(os.path.dirname(file_path), new_name)
        os.rename(file_path, new_path)
        file_path = new_path

    sf_user = "rootedcyber"
    sf_project = "rnx1941"
    private_key_path = os.path.expanduser("~/.ssh/id_rsa")
    remote_dir = f"/home/frs/project/{sf_project}/"

    await msg.edit("📤 Uploading FAST...")

    # ⚡ FASTEST METHOD
    cmd = [
        "rsync",
        "-az",
        "-e",
        f"ssh -i {private_key_path}",
        file_path,
        f"{sf_user}@frs.sourceforge.net:{remote_dir}"
    ]

    result = subprocess.run(cmd)

    if result.returncode == 0:
        link = f"https://downloads.sourceforge.net/project/{sf_project}/{os.path.basename(file_path)}"
        await msg.edit(
            f"✅ Done!\n\n📁 <code>{os.path.basename(file_path)}</code>\n"
            f"📎 <a href='{link}'>Download</a>",
            parse_mode="html"
        )
    else:
        await msg.edit("❌ Upload failed")

    try:
        os.remove(file_path)
    except:
        pass