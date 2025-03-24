import os
from PIL import Image, ImageDraw, ImageFont
import os
from random import choice as c
co = "red","blue"
from . import async_searcher, eod, get_string, ultroid_cmd, text_set
@ultroid_cmd(pattern="wr( (.*)|$)")
async def writer(e):
    rg = f"{c(co)}"
    if e.reply_to:
        reply = await e.get_reply_message()
        text = reply.message
    elif e.pattern_match.group(1).strip():
        text = e.text.split(maxsplit=1)[1]
    else:
        return await eod(e, get_string("writer_1"))
    k = await e.eor(get_string("com_1"))
    img = Image.open("resources/downloads/b.jpg")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("resources/fonts/assfont.ttf", 30)
    x, y = 1, 4
    lines = text_set(text)
    line_height = font.getbbox("hg")[3] - font.getbbox("hg")[1]
    for line in lines:
        draw.text((x, y), line, fill=(f"{rg}"), font=font)
        y = y + line_height - 5
    file = "ult.jpg"
    img.save(file)
    await e.reply(file=file)
    os.remove(file)
    await k.delete()
