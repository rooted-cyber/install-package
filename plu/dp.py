import aiohttp, asyncio
import os
from telethon.tl.functions.photos import UploadProfilePhotoRequest
from . import ultroid_cmd

@ultroid_cmd(pattern="dp$")
async def actress_pfp(e):
    await e.eor("📸 Getting random actress image...")
    url = "https://api.pexels.com/v1/search?query=indian%20actress&per_page=1&page=1"
    headers = {"Authorization": "dSeVwI2GvVsrG0EcpXOZ1xqexoCDUgv1qGJK4SaGfvLXLO1sFFroboJ0"}

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as resp:
                if resp.status != 200:
                    await e.eor("❌ Failed to fetch data from Pexels.")
                    return
                
                data = await resp.json()
                
                if "photos" not in data or not data["photos"]:
                    await e.eor("⚠️ No photos found.")
                    return

                img_url = data["photos"][0]["src"]["large"]
                
                while True:
                    async with session.get(img_url) as img:
                      if img.status == 200:
                        with open("actress.jpg", "wb") as f:
                          f.write(await img.read())
                          file = await e.client.upload_file("actress.jpg")
                          await asyncio.sleep(20)
                          await e.client(UploadProfilePhotoRequest(file=file))
                          await e.respond("✅ Profile pic set successfully.")
                      else:
                          await e.eor("❌ Failed to download image.")
    except Exception as ex:
        await e.eor(f"❗Error: {ex}")
    finally:
        if os.path.exists("actress.jpg"):
            os.remove("actress.jpg")
