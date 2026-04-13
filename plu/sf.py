from . import *
import os
import subprocess
import math
from multiprocessing.pool import ThreadPool

@ultroid_cmd(pattern="sf( (.*)|$)")
async def sfupload(e):
    reply = await e.get_reply_message()
    if not reply or not reply.media:
        return await e.eor("⚠️ Reply to media")

    new_name = e.pattern_match.group(2)
    msg = await e.eor("⚡ Ultra Fast Upload Starting...")

    file_path = await reply.download_media(progress_callback=None)

    if not file_path:
        return await msg.edit("❌ Download fail")

    sf_user = "rootedcyber"
    sf_project = "rnx1941"
    private_key = os.path.expanduser("~/.ssh/id_rsa")
    remote_dir = f"/home/frs/project/{sf_project}/"

    # rename
    if new_name:
        if "." not in new_name:
            new_name += os.path.splitext(file_path)[1]
        new_file = os.path.join(os.path.dirname(file_path), new_name)
        os.rename(file_path, new_file)
        file_path = new_file

    # split file
    chunk_size = 5 * 1024 * 1024  # 5MB chunks
    chunks = []

    with open(file_path, "rb") as f:
        i = 0
        while True:
            data = f.read(chunk_size)
            if not data:
                break
            chunk_file = f"{file_path}.part{i}"
            with open(chunk_file, "wb") as cf:
                cf.write(data)
            chunks.append(chunk_file)
            i += 1

    def upload(chunk):
        cmd = [
            "rsync",
            "-az",
            "-e", f"ssh -i {private_key}",
            chunk,
            f"{sf_user}@frs.sourceforge.net:{remote_dir}"
        ]
        subprocess.run(cmd)
        return chunk

    # ⚡ PARALLEL UPLOAD (3 threads)
    pool = ThreadPool(3)
    pool.map(upload, chunks)

    # cleanup
    for c in chunks:
        os.remove(c)

    os.remove(file_path)

    await msg.edit("✅ Ultra Fast Upload Done!")