import time
import os
from telegraph import upload_file as uf

from . import bash, con, downloader, get_paste, get_string, udB, ultroid_cmd, uploader

@ultroid_cmd(
    pattern="r(.*)|$)",
)
async def imak(event):
    reply = await event.get_reply_message()
    t = time.time()
    if not reply:
        return await event.eor(get_string("cvt_1"))
    inp = event.pattern_match.group(1).strip()
    if not inp:
        return await event.eor(get_string("cvt_2"))
    xx = await event.eor(get_string("com_1"))
    if reply.media:
        if hasattr(reply.media, "document"):
            file = reply.media.document
            image = await downloader(
                reply.file.name or str(time.time()),
                reply.media.document,
                xx,
                t,
                get_string("com_5"),
            )

            file = image.name
        else:
            file = await event.client.download_media(reply.media)
    if os.path.exists(inp):
        os.remove(inp)
    await bash(f'mv """{file}""" """{inp}"""')
    if not os.path.exists(inp) or os.path.exists(inp) and not os.path.getsize(inp):
        os.rename(file, inp)
    k = time.time()
    n_file, _ = await event.client.fast_uploader(
        inp, show_progress=True, event=event, message="Uploading...", to_delete=True
    )
    await event.reply(
        f"`{n_file.name}`",
        file=n_file,
        force_document=False,
        thumb=ULTConfig.thumb,
    )
    os.remove(inp)
    await xx.delete()
