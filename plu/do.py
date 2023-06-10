#copy paste by unknow user

from . import get_help

__doc__ = get_help("help_mi")

import asyncio
import glob
import os
import time
from datetime import datetime as dt

from aiohttp.client_exceptions import InvalidURL
from telethon.errors.rpcerrorlist import MessageNotModifiedError

from pyUltroid.fns.helper import time_formatter
from pyUltroid.fns.tools import get_chat_and_msgid, set_attributes

from . import (
    LOGS,
    ULTConfig,
    downloader,
    eor,
    fast_download,
    get_all_files,
    get_string,
    progress,
    time_formatter,
    ultroid_cmd,
)

import os
import time

from telethon.tl.types import Message

from pyUltroid.fns.gDrive import GDriveManager
from pyUltroid.fns.helper import time_formatter

from . import ULTConfig, HNDLR, asst, eod, eor, get_string, ultroid_cmd


@ultroid_cmd(
    pattern="do( (.*)|$)",manager=True
)
async def down(event):
    matched = event.pattern_match.group(1).strip() or await event.get_reply_message()
    msg = await event.eor(get_string("udl_4"))
    if not matched:
        return await eor(msg, get_string("udl_5"), time=5)
    try:
        splited = matched.split(" | ")
        link = splited[0]
        filename = splited[1]
    except IndexError:
        filename = None
    s_time = time.time()
    try:
        filename, d = await fast_download(
            link,
            filename,
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(
                    d,
                    t,
                    msg,
                    s_time,
                    f"Downloading from {link}",
                )
            ),
        )
    except InvalidURL:
        return await msg.eor("`Invalid URL provided :(`", time=5)
    await msg.eor(f"`{filename}` Now uplod into gdrive")

    input_file = filename
    GDrive = GDriveManager()
    if not os.path.exists(GDrive.token_file):
        return await eod(event, get_string("gdrive_6").format(asst.me.username))
    if not input_file:
        return await eod(event, "`Reply to file or give its location.`")
    mone = await event.eor(get_string("com_1"))
    if isinstance(input_file, Message):
        location = "resources/downloads"
        if input_file.photo:
            filename = await input_file.download_media(location)
        else:
            filename = input_file.file.name
            if not filename:
                filename = str(round(time.time()))
            filename = f"{location}/{filename}"
            try:
                filename, downloaded_in = await event.client.fast_downloader(
                    file=input_file.media.document,
                    filename=filename,
                    show_progress=True,
                    event=mone,
                    message=get_string("com_5"),
                )
                filename = filename.name
            except Exception as e:
                return await eor(mone, str(e), time=10)
        await mone.edit(
            f"`Downloaded to ``{filename}`.`",
        )
    else:
        filename = input_file.strip()
        if not os.path.exists(filename):
            return await eod(
                mone,
                "File Not found in local server. Give me a file path :((",
                time=5,
            )
    folder_id = None
    if os.path.isdir(filename):
        files = os.listdir(filename)
        if not files:
            return await eod(
                mone, "`Requested directory is empty. Can't create empty directory.`"
            )
        folder_id = GDrive.create_directory(filename)
        c = 0
        for files in sorted(files):
            file = f"{filename}/{files}"
            if not os.path.isdir(file):
                try:
                    await GDrive._upload_file(mone, path=file, folder_id=folder_id)
                    c += 1
                except Exception as e:
                    return await mone.edit(
                        f"Exception occurred while uploading to gDrive {e}"
                    )
        return await mone.edit(
            f"`Uploaded `[{filename}](https://drive.google.com/folderview?id={folder_id})` with {c} files.`"
        )
    try:
        g_drive_link = await GDrive._upload_file(
            mone,
            filename,
        )
        await mone.edit(
            get_string("gdrive_7").format(filename.split("/")[-1], g_drive_link)
        )
    except Exception as e:
        await mone.edit(f"Exception occurred while uploading to gDrive {e}")

@ultroid_cmd(
    pattern="gd( (.*)|$)",
    manager=True,
)
async def gdown(event):
    GDrive = GDriveManager()
    match = event.pattern_match.group(1).strip()
    if not match:
        return await eod(event, "`Give file id or Gdrive link to download from!`")
    filename = match.split(" | ")[1].strip() if " | " in match else None
    eve = await event.eor(get_string("com_1"))
    _start = time.time()
    status, response = await GDrive._download_file(eve, match, filename)
    if not status:
        return await eve.edit(response)
    await eve.edit(
        f"`Downloaded ``{response}`` in {time_formatter((time.time() - _start)*1000)}`"
    )


@ultroid_cmd(pattern="help",manager=True)
async def helpp(event):
  await event.reply(f"""
`/do` - download and upload gdrive.
`/gd` - drive file download
`/cl` - Clone gdtot link
`{HNDLR}ytv` - Download youtube videos
`{HNDLR}yta` - Download youtube audio
""")

