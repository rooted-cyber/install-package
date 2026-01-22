# Ultroid Image Generator Plugin
# Command: .img <prompt>

from . import ultroid_cmd, eor
import urllib.parse

@ultroid_cmd(pattern="img(?: |$)(.*)")
async def create_image(event):
    prompt = event.pattern_match.group(1)

    if not prompt:
        return await eor(event, "❌ Use: `.img <image description>`")

    await eor(event, "🎨 Image bana raha hoon...")

    query = urllib.parse.quote(prompt)
    img_url = f"https://image.pollinations.ai/prompt/{query}"

    await event.client.send_file(
        event.chat_id,
        img_url,
        caption=f"🖼️ **Prompt:** `{prompt}`",
        reply_to=event.id
    )
