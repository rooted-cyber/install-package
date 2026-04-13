from . import *
import os
import subprocess
import time
from html import escape

# ⚡ Faster progress (reduced edits)
async def progress(current, total, msg, start, text):
    now = time.time()
    diff = now - start

    if diff < 1:   # avoid spam edits
        return

    speed = current / diff
    percentage = (current / total) * 100 if total else 0

    bar = "█" * int(percentage // 20) + "░" * (5 - int(percentage // 20))

    try:
        await msg.edit(
            f"{text}\n\n"
            f"[{bar}] {percentage:.1f}%\n"
            f"⚡ {speed/1024:.1f} KB/s"
        )
    except:
        pass


@ultroid_cmd(pattern="sf( (.*)|$)")
async def sfupload(e):
    reply = await e.get_reply_message()

    if not reply or not reply.media:
        return await e.eor("⚠️ Media par reply karo")

    new_name = e.pattern_match.group(2)

    msg = await e.eor("📥 Starting...")

    start = time.time()

    file_path = await reply.download_media()

    if not file_path:
        return await msg.edit("❌ Download fail")

    file_name = os.path.basename(file_path)

    # auto extension fix
    if "." not in file_name:
        ext = ".jpg" if reply.photo else ".mp4" if reply.video else ".mp3" if reply.audio else ".bin"
        new_path = file_path + ext
        os.rename(file_path, new_path)
        file_path = new_path

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

    await msg.edit("📤 Uploading...")

    cmd = [
        "scp",
        "-C",
        "-i", private_key_path,
        file_path,
        f"{sf_user}@frs.sourceforge.net:{remote_dir}"
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode == 0:
        link = f"https://downloads.sourceforge.net/project/{sf_project}/{os.path.basename(file_path)}"
        await msg.edit(
            f"✅ Done!\n\n📁 <code>{os.path.basename(file_path)}</code>\n"
            f"📎 <a href='{link}'>Download</a>",
            parse_mode="html"
        )
    else:
        await msg.edit(f"❌ Failed:\n<code>{escape(result.stderr)}</code>", parse_mode="html")

    try:
        os.remove(file_path)
    except:
        pass