from pyUltroid import udB
from . import udB, bash, ultroid_cmd, get_string
import requests

@ultroid_cmd(pattern="cat$")
async def catbox_uploader(e):
    ax = await e.eor(get_string("com_1"))
    reply = await e.get_reply_message()
    if not reply or not reply.media:
        return await e.reply("कृपया किसी इमेज पर रिप्लाई करें।")
    d = await e.client.download_media(reply)
    file = {'fileToUpload': open(d, 'rb')}
    res = requests.post('https://catbox.moe/user/api.php', data={'reqtype': 'fileupload'}, files=file)
    if res.status_code == 200 and "catbox" in res.text:
        await ax.reply(f"✅ Upload Successful:\n🔗 {res.text}")
    else:
        await e.reply("❌ Upload Failed, https://catbox.moe")
