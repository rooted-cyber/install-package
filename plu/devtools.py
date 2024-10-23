# Ultroid - UserBot
# Copyright (C) 2021-2023 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

from . import get_help

__doc__ = get_help("help_devtools")
from os import system as s, mkdir, chmod, remove as rm, listdir as ls,chdir as cd, getcwd as pwd
import inspect
import sys
import traceback
from io import BytesIO, StringIO
from os import remove
from pprint import pprint

from telethon.utils import get_display_name

from pyUltroid import _ignore_eval
from . import *
try:
    from pyUltroid._my.my import *
except:
    leave_group = None
# Used for Formatting Eval Code, if installed
try:
    import black
except ImportError:
    black = None
from random import choice

try:
    from yaml import safe_load
except ImportError:
    from pyUltroid.fns.tools import safe_load
try:
    from telegraph import upload_file as uf
except ImportError:
    uf = None
from telethon.tl import functions

fn = functions

@ultroid_cmd(
    pattern="sys$",
)
async def _(e):
    xx = await e.eor(get_string("com_1"))
    x, y = await bash("neofetch|sed 's/\x1B\\[[0-9;\\?]*[a-zA-Z]//g' >> neo.txt")
    if y and y.endswith("NOT_FOUND"):
        return await xx.edit(f"Error: `{y}`")
    with open("neo.txt", "r", encoding="utf-8") as neo:
        p = (neo.read()).replace("\n\n", "")
    haa = await Carbon(code=p, file_name="neofetch", backgroundColor=choice(ATRA_COL))
    if isinstance(haa, dict):
        await xx.edit(f"`{haa}`")
    else:
        await e.reply(file=haa)
        await xx.delete()
    remove("neo.txt")


@ultroid_cmd(pattern="b", only_devs=True)
async def _(event):
    mythumb = "resources/downloads/a.jpg"
    carb, rayso, yamlf = None, None, False
    try:
        cmd = event.text.split(" ", maxsplit=1)[1]
        if cmd.split()[0] in ["-c", "--carbon"]:
            cmd = cmd.split(maxsplit=1)[1]
            carb = True
        if cmd.split()[0] in ["-r", "--rayso"]:
            cmd = cmd.split(maxsplit=1)[1]
            rayso = True
    except IndexError:
        return await event.eor(get_string("devs_1"), time=10)
    xx = await event.eor(get_string("com_1"))
    reply_to_id = event.reply_to_msg_id or event.id
    stdout, stderr = await bash(cmd, run_code=1)
    OUT = f"**☞ BASH\n\n• COMMAND:**\n`{cmd}` \n\n"
    err, out = "", ""
    cpyc = f"```{cmd}```"
    if stderr:
        err = f"**• ERROR:** \n```{stderr}```\n\n"
    if stdout:
        if (carb or udB.get_key("CARBON_ON_BASH")) and (
            event.is_private
            or event.chat.admin_rights
            or event.chat.creator
            or event.chat.default_banned_rights.embed_links
        ):
            li = await Carbon(
                code=stdout,
                file_name="bash",
                download=True,
                backgroundColor=choice(ATRA_COL),
            )
            if isinstance(li, dict):
                await xx.edit(
                    f"Unknown Response from Carbon: `{li}`\n\nstdout`:{stdout}`\nstderr: `{stderr}`"
                )
                return
            url = f"https://graph.org{uf(li)[-1]}"
            OUT = f"[\xad]({url}){OUT}"
            out = "**• OUTPUT:**"
            remove(li)
        elif (rayso or udB.get_key("RAYSO_ON_BASH")) and (
            event.is_private
            or event.chat.admin_rights
            or event.chat.creator
            or event.chat.default_banned_rights.embed_links
        ):
            li = await Carbon(
                code=stdout,
                file_name="bash",
                download=True,
                backgroundColor=choice(ATRA_COL),
                rayso=True,
            )
            if isinstance(li, dict):
                await xx.edit(
                    f"Unknown Response from Carbon: `{li}`\n\nstdout`:{stdout}`\nstderr: `{stderr}`"
                )
                return
            url = f"https://graph.org{uf(li)[-1]}"
            OUT = f"[\xad]({url}){OUT}"
            out = "**• OUTPUT:**"
            remove(li)
        else:
            if "piip" in cmd and all(":" in line for line in stdout.split("\n")):
                try:
                    load = safe_load(stdout)
                    stdout = ""
                    for data in list(load.keys()):
                        res = load[data] or ""
                        if res and "http" not in str(res):
                            res = f"`{res}`"
                        stdout += f"**{data}**  :  {res}\n"
                    yamlf = True
                except Exception as er:
                    stdout = f"`{stdout}`"
                    LOGS.exception(er)
            else:
                stdout = f"```{stdout}```"
            out = f"**• OUTPUT:**\n{stdout}"
    if not stderr and not stdout:
        out = "**• OUTPUT:**\n`Success`"
    OUT += err + out + cpyc
    if len(OUT) > 4096:
        ultd = err + out + cpyc
        with BytesIO(str.encode(ultd)) as out_file:
            out_file.name = "bash.txt"
            await event.client.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                thumb=mythumb,
                allow_cache=False,
                caption=f"`{cmd}`" if len(cmd) < 998 else None,
                reply_to=reply_to_id,
            )

            await xx.delete()
    else:
        await xx.edit(OUT, link_preview=not yamlf)


pp = pprint  # ignore: pylint
bot = ultroid = ultroid_bot


class u:
    _ = ""


def _parse_eval(value=None):
    if not value:
        return value
    if hasattr(value, "stringify"):
        try:
            return value.stringify()
        except TypeError:
            pass
    elif isinstance(value, dict):
        try:
            return json_parser(value, indent=1)
        except BaseException:
            pass
    elif isinstance(value, list):
        newlist = "["
        for index, child in enumerate(value):
            newlist += "\n  " + str(_parse_eval(child))
            if index < len(value) - 1:
                newlist += ","
        newlist += "\n]"
        return newlist
    return str(value)


@ultroid_cmd(pattern="e", manager=True, only_devs=True)
async def _(event):
    mythumb = "resources/downloads/a.jpg"
    try:
        cmd = event.text.split(maxsplit=1)[1]
    except IndexError:
        return await event.eor(get_string("devs_2"), time=5)
    xx = None
    mode = ""
    spli = cmd.split()
    if cmd == starswith("`"):
        await event.reply(f"``{cmd}```")

    async def get_():
        try:
            cm = cmd.split(maxsplit=1)[1]
        except IndexError:
            await event.eor("->> Wrong Format <<-")
            cm = None
        return cm

    if spli[0] in ["-s", "--silent"]:
        await event.delete()
        mode = "silent"
    elif spli[0] in ["-n", "-noedit"]:
        mode = "no-edit"
        xx = await event.reply(get_string("com_1"))
    elif spli[0] in ["-gs", "--source"]:
        mode = "gsource"
    elif spli[0] in ["-ga", "--args"]:
        mode = "g-args"
    if mode:
        cmd = await get_()
    if not cmd:
        return
    if not mode == "silent" and not xx:
        xx = await event.eor(get_string("com_1"))
    if black:
        try:
            cmd = black.format_str(cmd, mode=black.Mode())
        except BaseException:
            # Consider it as Code Error, and move on to be shown ahead.
            pass
    reply_to_id = event.reply_to_msg_id or event
    
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()
    redirected_error = sys.stderr = StringIO()
    stdout, stderr, exc, timeg = None, None, None, None
    tima = time.time()
    try:
        value = await aexec(cmd, event)
    except Exception:
        value = None
        exc = traceback.format_exc()
    tima = time.time() - tima
    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr
    if value:
        try:
            if mode == "gsource":
                exc = inspect.getsource(value)
            elif mode == "g-args":
                args = inspect.signature(value).parameters.values()
                name = ""
                if hasattr(value, "__name__"):
                    name = value.__name__
                exc = f"**{name}**\n\n" + "\n ".join([str(arg) for arg in args])
        except Exception:
            exc = traceback.format_exc()
    evaluation = exc or stderr or stdout or _parse_eval(value) or get_string("instu_4")
    if mode == "silent":
        if exc:
            msg = f"• <b>EVAL ERROR\n\n• CHAT:</b> <code>{get_display_name(event.chat)}</code> [<code>{event.chat_id}</code>]"
            msg += f"\n\n∆ <b>CODE:</b>\n<code>{cmd}</code>\n\n∆ <b>ERROR:</b>\n<code>{exc}</code>"
            log_chat = udB.get_key("LOG_CHANNEL")
            if len(msg) > 4000:
                with BytesIO(msg.encode()) as out_file:
                    out_file.name = "Eval-Error.txt"
                return await event.client.send_message(
                    log_chat, f"`{cmd}`", file=out_file
                )
            await event.client.send_message(log_chat, msg, parse_mode="html")
        return
    tmt = tima * 1000
    timef = time_formatter(tmt)
    timeform = timef if not timef == "0s" else f"{tmt:.3f}ms"
    final_output = "💛 **__𝗘𝗩𝗔𝗟__** 💙 (**{}**)\n```{}``` \n\n __►__ **OUTPUT** in 💜💜 {}: \n```{}``` \n\n**COPY THIS**:\n `{}`\n".format(
        timeform,
        cmd,
        timeform,
        evaluation,
        cmd,
    )
    if len(final_output) > 4096:
        final_output = evaluation
        with BytesIO(str.encode(final_output)) as out_file:
            out_file.name = "eval.txt"
            await event.client.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                thumb=mythumb,
                allow_cache=False,
                caption=f"```{cmd}```" if len(cmd) < 998 else None,
                reply_to=reply_to_id,
            )
        return await xx.delete()
    hut = "💛 **__EVAL__** 💙 (**{}**)\n```{}``` \n\n __►__ **OUTPUT** in 💜💜 {}:".format(timeform,cmd,timeform)
    await xx.edit(f"{final_output}")


def _stringify(text=None, *args, **kwargs):
    if text:
        u._ = text
        text = _parse_eval(text)
    return print(text, *args, **kwargs)


async def aexec(code, event):
    exec(
        (
            "async def __aexec(e, client): "
            + "\n print = p = _stringify"
            + "\n message = event = e"
            + "\n u.r = r = reply = await event.get_reply_message()"
            + "\n chat = event.chat_id"
            + "\n u.lr = locals()"
      )
        + "".join(f"\n {l}" for l in code.split("\n"))
    )

    return await locals()["__aexec"](event, event.client)
