# Written by @moiusrname (dot arc) for Ultroid!
# API by @botsbakery

"""
**GDToT Extractor!**

> Get GDrive Link from GDToT Links.

✘ Commands Available
> `{i}gdtot` <some gdtot link>
> `{i}gdtot https://new7.gdtot.cfd/file/1374091784`
"""

from re import findall

from . import async_searcher, LOGS, ultroid_cmd


@ultroid_cmd(pattern="cl( (.*)|$)",manager=True)
async def extract_gdtot_links(e):
    args = e.pattern_match.group(2)
    reply = await e.get_reply_message()
    if not args:
        if reply and reply.text:
            args = reply.message
    if not args:
        return await e.eor("`Gimme a GDToT link to Bypass...`", time=6)

    if not findall(r"https?:\/\/\w+\.gdtot\.\S+", args):
        return await e.eor("`Not a a Valid GDToT link?...` 🤖", time=6)

    msg = await e.eor("`extracting drive link..`")
    try:
        response = await async_searcher(
            f"https://apis.imkaif.me/gdtot?url={args}", re_json=True,
        )
    except Exception as exc:
        LOGS.exception(exc)
        return await msg.edit(
            f"**Something went Wrong while processing Gdtot Link.** \n\n`{exc}"
        )

    if err := response.get("error"):
        return await msg.edit(f"**Got Error:** `{err}`")

    editText = "<b><i>Extracted GDrive Link from GDToT 💯</i>\n\n🎥 Title:</b>  <code>{title}</code>\n🖇️ <b>Size:<b>  <code>{size}</code>\n\n<b>Links:  <a href='{gdtot}'>GDToT Link</a> | <a href='{gdrive}'>GDrive Link</a></b>"
    await msg.edit(
        editText.format(
            title=response.get("filename"),
            size=response.get("filesize"),
            gdtot=args,
            gdrive=response.get("gdriveLink"),
        ),
        parse_mode="html",
    )
