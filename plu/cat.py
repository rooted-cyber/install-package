from . import udB, bash, ultroid_cmd, get_string
import requests

@ultroid_cmd(pattern="cat$")
async def catbox_uploader(e):
    ax = await e.eor(get_string("com_1"))
    reply = await e.get_reply_message()

    if not reply or not reply.media:
        return await e.reply("कृपया किसी इमेज पर रिप्लाई करें।")

    d = await e.client.download_media(reply)

    try:
        with open(d, 'rb') as f:
            res = requests.post(
                "https://catbox.moe/user/api.php",
                data={"reqtype": "fileupload"},
                files={"fileToUpload": f},
                headers={
                    "User-Agent": "Mozilla/5.0"
                },
                timeout=60
            )

        if res.status_code == 200 and res.text.startswith("https://"):
            await ax.reply(f"✅ Upload Successful:\n🔗 {res.text}")
        else:
            await e.reply(f"❌ Upload Failed\nResponse: {res.text}")

    except Exception as err:
        await e.reply(f"❌ Error:\n{str(err)}")
