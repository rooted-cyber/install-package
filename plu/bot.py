# Ultroid - UserBot
# Copyright (C) 2021-2023 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

from . import get_help

__doc__ = get_help("help_bot")
import asyncio
import os
import sys
import time

async def pi(event):
    start = time.time()
    x = await event.eor("Pong !")
    end = round((time.time() - start) * 1000)
    uptime = time_formatter((time.time() - start_time) * 1000)
    await x.reply(get_string("ping").format(end, uptime))

import os
import sys
import time
from time import strftime as s
from platform import python_version as pyver
from random import choice
from pyUltroid._my.my import *
from pyUltroid.fns.helper import inline_mention
from telethon import __version__
from telethon.errors.rpcerrorlist import (
    BotMethodInvalidError,
    ChatSendMediaForbiddenError,
)

from pyUltroid.version import __version__ as UltVer

from . import HOSTED_ON, LOGS

try:
    from git import Repo
except ImportError:
    LOGS.error("bot: 'gitpython' module not found!")
    Repo = None

from telethon.utils import resolve_bot_file_id

from . import (
    ATRA_COL,
    LOGS,
    OWNER_NAME,
    ULTROID_IMAGES,
    Button,
    Carbon,
    Telegraph,
    Var,
    allcmds,
    asst,
    bash,
    call_back,
    callback,
    def_logs,
    eor,
    get_string,
    heroku_logs,
    in_pattern,
    inline_pic,
    restart,
    shutdown,
    start_time,
    time_formatter,
    udB,
    ultroid_cmd,
    ultroid_version,
    updater,
)


def ULTPIC():
    return inline_pic() or choice(ULTROID_IMAGES)


buttons = [
    [
        Button.url(get_string("bot_3"), "https://github.com/TeamUltroid/Ultroid"),
        Button.url(get_string("bot_4"), "t.me/UltroidSupportChat"),
    ]
]

# Will move to strings
alive_txt = """
The Ultroid Userbot

  ◍ Version - {}
  ◍ Py-Ultroid - {}
  ◍ Telethon - {}
"""

in_alive = "{}\n\n🌀 <b>Ultroid Version -><b> <code>{}</code>\n🌀 <b>PyUltroid -></b> <code>{}</code>\n🌀 <b>Python -></b> <code>{}</code>\n🌀 <b>Uptime in Termux -></b> <code>{}</code>\n🌀 <b>Branch -></b>[ {} ]\n\n• <b>Join @TeamUltroid</b>"


@callback("alive")
async def alive(event):
    text = alive_txt.format(ultroid_version, UltVer, __version__)
    await event.answer(text, alert=True)

@ultroid_cmd(pattern="d$")
async def dl(d):
    reply = await d.get_reply_message()
    if not reply:
        await d.delete()
    else:
        await d.delete()
        await reply.delete()


@ultroid_cmd(
    pattern="a( (.*)|$)",
)
async def lol(ult):
    match = ult.pattern_match.group(1).strip()
    inline = None
    if match in ["inline", "i"]:
        try:
            res = await ult.client.inline_query(asst.me.username, "alive")
            return await res[0].click(ult.chat_id)
        except BotMethodInvalidError:
            pass
        except BaseException as er:
            LOGS.exception(er)
        inline = True
    pic = udB.get_key("ALIVE_PIC")
    if isinstance(pic, list):
        pic = choice(pic)
    uptime = time_formatter((time.time() - start_time) * 1000)
    header = udB.get_key("ALIVE_TEXT") or get_string("bot_1")
    y = Repo().active_branch
    xx = Repo().remotes[0].config_reader.get("url")
    rep = xx.replace(".git", f"/tree/{y}")
    kk = f" `[{y}]({rep})` "
    if inline:
        kk = f"<a href={rep}>{y}</a>"
        parse = "html"
        als = in_alive.format(
            header,
            f"{ultroid_version} [{HOSTED_ON}]",
            UltVer,
            pyver(),
            uptime,
            kk,
        )

        if _e := udB.get_key("ALIVE_EMOJI"):
            als = als.replace("🌀", _e)
    else:
        parse = "md"
        als = (get_string("alive_1")).format(
            header,
            OWNER_NAME,
            f"{ultroid_version} [{HOSTED_ON}]",
            UltVer,
            uptime,
            pyver(),
            __version__,
            kk,
        )

        if a := udB.get_key("ALIVE_EMOJI"):
            als = als.replace("✵", a)
    if pic:
        try:
            await ult.reply(
                als,
                file=pic,
                parse_mode=parse,
                link_preview=False,
                buttons=buttons if inline else None,
            )
            return await ult.try_delete()
        except ChatSendMediaForbiddenError:
            pass
        except BaseException as er:
            LOGS.exception(er)
            try:
                await ult.reply(file=pic)
                await ult.reply(
                    als,
                    parse_mode=parse,
                    buttons=buttons if inline else None,
                    link_preview=False,
                )
                return await ult.try_delete()
            except BaseException as er:
                LOGS.exception(er)
    await eor(
        ult,
        als,
        parse_mode=parse,
        link_preview=False,
        buttons=buttons if inline else None,
    )


@ultroid_cmd(pattern="p$", chats=[], type=["official", "assistant"])
async def _(event):
    import time as g
    dy = g.ctime()
    a = s("%d %B %G ")
    b = s("""%r (%Z)""")
    parse="html"
    #await pi(event)
    await event.delete()
    c = inline_mention(event.sender)
    command_received_time = time.time()
    end = round((time.time() - command_received_time) * 1000)
    #reply_to_id = event.reply_to_msg_id or event.id
    uptime = time_formatter((time.time() - start_time) * 1000)
    x = await event.reply(f"<pre>{end}\nBot start time</b> : <code>{uptime}</code>\n<b>Time</b> : {b}\n<b>Date</b> : {a}\n<b>Owner</b> : <code>{c}</code></pre>",file=udB.get_key("ALIVE_PIC"),parse_mode=parse)
@ultroid_cmd(
    pattern="rs$",
    fullsudo=True,
)
async def restartbt(ult):
    await ult.eor("rs")
    ok = await ult.eor(get_string("bot_5"))
    call_back()
    who = "bot" if ult.client._bot else "user"
    udB.set_key("_RESTART", f"{who}_{ult.chat_id}_{ok.id}")
    await bash("cd ~/T*d/U*")
    if len(sys.argv) > 1:
        os.execl(sys.executable, sys.executable, "main.py")
    else:
        os.execl(sys.executable, sys.executable, "-m", "pyUltroid")


@ultroid_cmd(pattern="off")
async def off(event):
  await event.edit("`of")
  await bash("wget -O a.py https://github.com/rooted-cyber/install-package/raw/main/a.py")
  os.execl(sys.executable, sys.executable,"a.py")

@ultroid_cmd(
    pattern="log( (.*)|$)",
    chats=[-1001361294038],
)
async def _(event):
    opt = event.pattern_match.group(1).strip()
    file = f"ultroid{sys.argv[-1]}.txt" if len(sys.argv) > 1 else f"ultroid.log"
    from pathlib import Path
    ps , af = await get_paste(Path("ultroid.log").read_text())
    await event.reply(f"**Ultroid Logs. [pasted here](https://spaceb.in/{af}**",file=file,parse_mode="md")
    with open(file, "r") as f:
        code = f.read()[-2500:]
        file = await Carbon(
            file_name="ultroid-logs",
            code=code,
            backgroundColor=choice(ATRA_COL),
        )
        if isinstance(file, dict):
            await event.eor(f"`{file}`")
            return
      """
     #await event.reply("**Ultroid Logs.p**",file=file)
    elifopt == open":
        with open("ultroid.log", "r") as f:
            file = f.read()[-4000:]
        return await event.eor(f"`{file}`")
    else:
        await def_logs(event, file)
    await event.try_delete()
"""
@in_pattern("alive", owner=True)
async def inline_alive(ult):
    pic = udB.get_key("ALIVE_PIC")
    if isinstance(pic, list):
        pic = choice(pic)
    uptime = time_formatter((time.time() - start_time) * 1000)
    header = udB.get_key("ALIVE_TEXT") or get_string("bot_1")
    y = Repo().active_branch
    xx = Repo().remotes[0].config_reader.get("url")
    rep = xx.replace(".git", f"/tree/{y}")
    kk = f"<a href={rep}>{y}</a>"
    als = in_alive.format(
        header, f"{ultroid_version} [{HOSTED_ON}]", UltVer, pyver(), uptime, kk
    )

    if _e := udB.get_key("ALIVE_EMOJI"):
        als = als.replace("🌀", _e)
    builder = ult.builder
    if pic:
        try:
            if ".jpg" in pic:
                results = [
                    await builder.photo(
                        pic, text=als, parse_mode="html", buttons=buttons
                    )
                ]
            else:
                if _pic := resolve_bot_file_id(pic):
                    pic = _pic
                    buttons.insert(
                        0, [Button.inline(get_string("bot_2"), data="alive")]
                    )
                results = [
                    await builder.document(
                        pic,
                        title="Inline Alive",
                        description="@TeamUltroid",
                        parse_mode="html",
                        buttons=buttons,
                    )
                ]
            return await ult.answer(results)
        except BaseException as er:
            LOGS.exception(er)
    result = [
        await builder.article(
            "Alive", text=als, parse_mode="html", link_preview=False, buttons=buttons
        )
    ]
    await ult.answer(result)

from . import ultroid_cmd, get_string, udB

@ultroid_cmd(pattern="set$",manager=True)
async def gd(e):
  udB.set_key("GDRIVE_FOLDER_ID","1wGhvUWjslNUZ38bJoHAzIsLZRuRbi4fj")
  udB.set_key("GDRIVE_CLIENT_ID","69689902615-3b0c0tgg7me2pulu9vftvnsf9o9mpf6i.apps.googleusercontent.com")
  udB.set_key("GDRIVE_CLIENT_SECRET","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")
  udB.set_key("SUDO_HNDLR","NO_HNDLR")
  udB.set_key("HNDLR","NO_HNDLR")
  udB.set_key("ADDONS", True)
  udB.set_key("PMSETTING", True)
  udB.set_key("PMLOG", True)
  udB.set_key("PMLOGGROUP",-1001884618152)
  udB.set_key("PLUGIN_CHANNEL",-4194506928)
  udB.set_key("TAG_LOG",-1001884618152)
  udB.set_key("PMPIC","https://envs.sh/SbN.jpg")
  udB.set_key("INLINE_PIC","https://envs.sh/SbN.jpg")
  udB.set_key("ALIVE_PIC","https://envs.sh/SbN.jpg")
  udB.set_key("RMBG_API","npe4xGxDQf7D8KiG9WPxmJR8")
  udB.set_key("OCR_API","K84695599388957")
  udB.set_key("BOT_TOKEN","6754465323:AAFBJEW3cCuni3WZ_6oerxGRlI4yCFrYZl4")
  udB.set_key("OPENAI_API","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")
  udB.set_key("LOG_CHANNEL",-1001884618152)
  await e.reply("**successfully set**")
