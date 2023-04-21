from . import LOGS, ultroid_cmd


@ultroid_cmd(pattern="wbp$")
async def linkss(e):
    r = await e.get_reply_message()
    if not (r and r.media and hasattr(r.media, "webpage")):
        return await e.eor("Reply to a webpage preview msg")

    eris = await e.eor("...")
    m = getattr(r.media, "webpage", None)
    doc = m.photo if m.photo else m.document
    try:
        await e.respond(m.description, file=doc)
    except BaseException as ex:
        return LOGS.exception(ex)
    finally:
        await eris.delete()