import os
import pathlib
from PIL import Image
from telegraph import Telegraph
from . import ultroid_cmd
from . import mediainfo, bash

telegraph = Telegraph()
telegraph.create_account(short_name="Ultroid")

@ultroid_cmd(pattern="tp$")
async def tp_cmd(event):
    xx = await event.eor("📤 Uploading to Telegraph...")
    reply = await event.get_reply_message()
    if not reply:
        return await xx.eor("Reply to a message.")

    match = "Ultroid"

    if not reply.media and reply.text:
        content = reply.text
        makeit = telegraph.create_page(title=match, content=[content])
        return await xx.eor(f"✅ [Telegraph]({makeit['url']})", link_preview=False)

    try:
        getit = await reply.download_media()
        dar = mediainfo(reply.media)

        if dar == "sticker":
            file = f"{getit}.png"
            Image.open(getit).save(file)
            os.remove(getit)
            getit = file

        elif dar.endswith("animated"):
            file = f"{getit}.gif"
            await bash(f"lottie_convert.py '{getit}' {file}")
            os.remove(getit)
            getit = file

        if "document" not in dar:
            nn = uf(getit)
            os.remove(getit)
            return await xx.eor(f"✅ Uploaded: [Telegraph]({nn})", link_preview=False)

        # Assuming the content of the document is to be uploaded
        content = pathlib.Path(getit).read_text()
        os.remove(getit)
        makeit = telegraph.create_page(title=match, content=[content])
        return await xx.eor(f"✅ [Telegraph]({makeit['url']})", link_preview=False)

    except Exception as e:
        return await xx.eor(f"❌ Error: {e}")
