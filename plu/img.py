# Ultroid Image Generator Plugin
# Command: .img <prompt>  OR  reply + .img

from . import ultroid_cmd, eor
import urllib.parse

@ultroid_cmd(pattern="img(?: |$)(.*)")
async def create_image(event):
    prompt = event.pattern_match.group(1)

    # agar command me text nahi hai, to reply se lo
    if not prompt:
        reply = await event.get_reply_message()
        if reply and reply.text:
            prompt = reply.text
        else:
            return await eor(
                event,
                "❌ Use: `.img <image description>`\n"
                "ya kisi message pe **reply karke** `.img`"
            )

    status = await eor(event, "🎨 Image bana raha hoon...")

    query = urllib.parse.quote(prompt)
    img_url = f"https://image.pollinations.ai/prompt/{query}"

    await event.client.send_file(
        event.chat_id,
        img_url,
        caption=f"🖼️ **Prompt:** `{prompt}`",
        reply_to=event.reply_to_msg_id or event.id
    )

    await status.delete()
