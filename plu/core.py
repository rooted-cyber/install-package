from . import get_help

__doc__ = get_help("help_core")


import os
try:
  from pyUltroid._my.my import *
except:
  ins = None

from pyUltroid.startup.loader import load_addons

from . import LOGS, async_searcher, eod, get_string, safeinstall, ultroid_cmd, un_plug


@ultroid_cmd(pattern="sp")
async def speed(e):
  a = await e.edit("`Checking your ultroid userbot speed....`")
  await a.sp(e)

@ultroid_cmd(pattern="ins", fullsudo=True)
async def install(event):
    await safeinstall(event)

@ultroid_cmd(
    pattern=r"un( (.*)|$)",
)
async def uninstall(event):
    shortname = event.pattern_match.group(1).strip()
    if not shortname:
        await event.eor(get_string("core_13"))
        return
    lsd = os.listdir("addons")
    lsp = os.listdir("plugins")
    zym = f"{shortname}.py"
    if zym in lsp:
        un_plug(shortname)
        await event.eor(f"**Plugins : Uɴɪɴsᴛᴀʟʟᴇᴅ** `{shortname}` **Sᴜᴄᴄᴇssғᴜʟʟʏ.**", time=5)
        os.remove(f"plugins/{shortname}.py")
    elif zym in lsd:
            un_plug(shortname)
            await event.eor(f"**Addons : Uɴɪɴsᴛᴀʟʟᴇᴅ** `{shortname}` **Sᴜᴄᴄᴇssғᴜʟʟʏ.**", time=5)
            os.remove(f"addons/{shortname}.py")
    else:
            await event.eor(f"**Not found **\n{shortname}")
    
@ultroid_cmd(
    pattern=r"load( (.*)|$)",
    fullsudo=True,
)
async def load(event):
    shortname = event.pattern_match.group(1).strip()
    if not shortname:
        await event.eor(get_string("core_16"))
        return
    try:
        try:
            un_plug(shortname)
        except BaseException:
            pass
        load_addons(f"addons/{shortname}.py")
        await event.eor(get_string("core_17").format(shortname), time=3)
    except Exception as e:
        LOGS.exception(e)
        await eod(
            event,
            get_string("core_18").format(shortname, e),
            time=3,
        )


@ultroid_cmd(pattern="link( (.*)|$)", fullsudo=True)
async def get_the_addons_lol(event):
    thelink = event.pattern_match.group(1).strip()
    xx = await event.eor(get_string("com_1"))
    fool = get_string("gas_1")
    if thelink is None:
        return await xx.eor(fool, time=10)
    split_thelink = thelink.split("/")
    if not ("raw" in thelink and thelink.endswith(".py")):
        return await xx.eor(fool, time=10)
    name_of_it = split_thelink[-1]
    plug = await async_searcher(thelink)
    fil = f"addons/{name_of_it}"
    await xx.edit("Packing the codes...")
    with open(fil, "w", encoding="utf-8") as uult:
        uult.write(plug)
    await xx.edit("Packed. Now loading the plugin..")
    shortname = name_of_it.split(".")[0]
    try:
        load_addons(fil)
        await xx.eor(get_string("core_17").format(shortname), time=15)
    except Exception as e:
        LOGS.exception(e)
        await eod(
            xx,
            get_string("core_18").format(shortname, e),
            time=3,
            )
