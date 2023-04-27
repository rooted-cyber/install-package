

@ultroid_cmd(pattern="ah ?(.*)|$")
async def openai_chat_gpt(e):
    args = e.pattern_match.group(1)
    reply = await e.get_reply_message()
    if not args:
        if reply and reply.text:
            args = reply.message
    if not args:
        return await e.eor(file="CAADAgADMgkAAhhC7ggR-4x175jn2gI")