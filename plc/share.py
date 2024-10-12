from telethon import events
from . import ultroid_cmd, get_string

@ultroid.on(events.NewMessage(func=lambda c:  c.text and c.media, incoming=False))
async def linkss(e):
  if m := getattr(e.media, "webpage", None):
    doc = m.photo if m.photo else m.document
    try:
      await e.respond(m.description, file=doc)
    except Exception as ex:
      return LOGS.exception(ex)
