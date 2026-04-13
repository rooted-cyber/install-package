from . import *
import os
import subprocess
import time
from html import escape

# 📊 Progress
async def progress(current, total, msg, start, text):
    now = time.time()
    diff = now - start

    if diff == 0:
        return

    speed = current / diff
    percentage = (current / total) * 100 if total else 0

    bar = "█" * int(percentage // 10) + "░" * (10 - int(percentage // 10))

    try:
        await msg.edit(
            f"{text}\n\n"
            f"[{bar}] {percentage:.2f}%\n"
            f"{current // (1024*1024)}MB / {total // (1024*1024) if total else 0}MB\n"
            f"⚡ {speed/1024:.2f} KB/s"
        )
    except:
        pass


@ultroid_cmd(pattern="sf( (.*)|$)")
async def sfupload(e):
    reply = await e.get_reply_message()

    if not reply:
        return await e.eor("⚠️ किसी file/media पर reply करें।")

    if not reply.media:
        return await e.eor("⚠️ ये message media नहीं है।")

    # 📝 Rename
    new_name = e.pattern_match.group(2)

    msg = await e.eor("📥 Download शुरू...")

    start = time.time()

    # 📥 Download (auto detect type)
    file_path = await reply.download_media(
        progress_callback=lambda d, t: progress(d, t, msg, start, "📥 Downloading...")
    )

    if not file_path or not os.path.exists(file_path):
        return await msg.edit("❌ Download fail")

    # 🔍 Auto extension fix
    file_name = os.path.basename(file_path)

    if "." not in file_name:
        # try guess extension
        if reply.photo:
            file_name += ".jpg"
        elif reply.video:
            file_name += ".mp4"
        elif reply.audio:
            file_name += ".mp3"
        else:
            file_name += ".bin"

        new_path = os.path.join(os.path.dirname(file_path), file_name)
        os.rename(file_path, new_path)
        file_path = new_path

    # 📝 Rename override
    if new_name:
        new_path = os.path.join(os.path.dirname(file_path), new_name)
        os.rename(file_path, new_path)
        file_path = new_path

    file_name = os.path.basename(file_path)

    # 🔧 CONFIG
    sf_user = "rootedcyber"
    sf_project = "rnx1941"
    private_key_path = os.path.expanduser("~/.ssh/id_rsa")
    remote_dir = f"/home/frs/project/{sf_project}/"

    await msg.edit("📤 Uploading to SourceForge...")

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
            safe_link = escape(link)

            await msg.edit(
                f"✅ Upload Done!\n\n"
                f"📁 <code>{file_name}</code>\n"
                f"📎 <a href='{safe_link}'>Download</a>",
                parse_mode="html"
            )
        else:
            await msg.edit(
                f"❌ Upload failed\n\n<code>{escape(result.stderr)}</code>",
                parse_mode="html"
            )

    except Exception as ex:
        await msg.edit(
            f"❌ Error:\n<code>{escape(str(ex))}</code>",
            parse_mode="html"
        )

    finally:
        # 🧹 Delete local file
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
        except:
            pass