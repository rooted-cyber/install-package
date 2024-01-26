# Ultroid - UserBot
# Copyright (C) 2021-2023 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

"""
✘ Commands Available -

• {i}w <text or reply to text>
   It will write on a paper.

"""
from os import chdir as cd, listdir as ls, system as s, rename as mv, getcwd as pwd, remove as rm
import os
from random import choice as c

from colorama import Fore as f
from PIL import Image, ImageDraw, ImageFont

from . import async_searcher, eod, get_string, text_set, ultroid_cmd, download_file

co = "chocolate","coral","cornflowerblue","chartreuse","burlywood","blanchedalmond","beige"

@ultroid_cmd(pattern="aw( (.*)|$)")
async def writer(e):
    ab = pwd()
    rg = f"{c(co)}"
    if e.reply_to:
        reply = await e.get_reply_message()
        text = reply.message
    elif e.pattern_match.group(1).strip():
        text = e.text.split(maxsplit=1)[1]
    else:
        return await eod(e, get_string("writer_1"))
    k = await e.eor(get_string("com_1"))
    cd(".")
    if os.path.exists("./resources/downloads/b.jpg"):
      pwd()
    else:
      rd = await e.reply("**Downloading** `a.otf`")
      await download_file("https://github.com/rooted-cyber/install-package/raw/main/b.jpg","resources/downloads/b.jpg")
      await rd.delete()
      await e.reply("**Download complete**m")
    img = Image.open("./resources/downloads/b.jpg")
    draw = ImageDraw.Draw(img)
    if "a.otf" in ls("./resources/downloads/"):
      ls()
    else:
      rfd = await e.reply("**Downloading** `a.otf`")
      await download_file("https://github.com/rooted-cyber/install-package/raw/main/a.otf","resources/downloads/a.otf")
      await rfd.delete()
      await e.reply("**Download complete**")
    font = ImageFont.truetype("resources/downloads/a.otf", size=30)
    x, y = 120, 140
    lines = text_set(text)
    line_height = font.getbbox("hi")[3]
    for line in lines:
        draw.text((x, y), line, fill=f"{rg}", font=font)
        y = y + line_height - 5
    file = "ult.jpg"
    img.save(file)
    await e.reply(file=file)
    os.remove(file)
    await k.delete()
    cd(ab)
    await e.reply(ab)
