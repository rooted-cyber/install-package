# < Source - t.me/testingpluginnn >
# < https://github.com/TeamUltroid/Ultroid >

"""
✘ **Send any Installed Plugin to the Chat!**

>> Use : `{i}sd <plugin_name>`
"""

import os

from . import *


def send(fn):
    lst = ["plugins", "addons"]
    if not fn.endswith(".py"):
        fn += ".py"
    for i in lst:
        path = os.path.join(i, fn)
        if os.path.exists(path):
            return path
    else:
        return


def alt_send(fn):
    import re
    for k, v in LIST.items():
        for fx in v:
            if re.findall(fn, fx):
                return send(k)
    else:
        return


async def pastee(path):
    with open(path, "r") as f:
        data = f.read()
    err, linky = await get_paste(data)
    if err:
        return f"<b>>> <a href='https://spaceb.in/{linky}'>Pasted Here!</a></b> \n"
    else:
        LOGS.error(linky)
        return ""


@ultroid_cmd(pattern="sd ?(.*)|$")
async def semd_plugin(ult):
    mythumb = "resources/downloads/a.jpg"
    repo = "https://github.com/TeamUltroid/Ultroid"
    args = ult.pattern_match.group(1)
    if not args:
        return await ult.eod("`Give a plugin name too`")

    eris = await ult.eor("`processing`")
    path = send(args)
    if not path:
        path = alt_send(args)
    if not path:
        return await eris.edit(f"No plugins were found for: `{args}`")

    paste = await pastee(path)
    caption = f"<b>>> </b><code>{path}</code> \n{paste} \n" \
        f"© <a href='{repo}'>Team Ultroid</a>"
    try:
        await ult.client.send_file(
            ult.chat_id, path,
            caption=caption, parse_mode="html",
            thumb=mythumb,
            silent=True, reply_to=ult.reply_to_msg_id,
        )
        await eris.delete()
    except Exception as fx:
        return await eris.edit(str(fx))
