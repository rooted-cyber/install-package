import asyncio
from . import ultroid_cmd
import yt_dlp

async def get_video_info(link):
    ydl_opts = {'quiet': True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(link, download=False)  # Get video info without downloading
    return {
        'title': info.get('title'),
        'size': info.get('filesize') or 'Unknown size',  # File size of the video
        'format': info.get('formats')[0]['format_id'] if info.get('formats') else 'Unknown format'  # Best format
    }

@ultroid_cmd(pattern="vd ?(.*)")
async def vdown(event):
    link = event.pattern_match.group(1)
    if not link:
        return await event.reply("🔗 Link dedo pehle!")
    
    video_info = await get_video_info(link)  
    await event.reply(f"🎥 Title: {video_info['title']}\n📏 Size: {video_info['size']}\n📂 Format: {video_info['format']}")
    msg = await event.reply("📥 Downloading start kar raha hoon...")

    cmd = f"yt-dlp --newline {link}"
    process = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.STDOUT
    )

    while True:
        line = await process.stdout.readline()
        if not line:
            break
        line = line.decode().strip()
        if "%" in line:
            try:
                percent = line.split('%')[0].split()[-1]
                # Get downloading speed mentioned in the output
                speed = line.split('at ')[-1] if 'at ' in line else "Unknown speed"
                downloading_bar = "●" * (int(float(percent) / 5))
                empty_bar = "○" * (20 - len(downloading_bar))
                bar = f"[{downloading_bar}{empty_bar}] {percent}%"
                await msg.edit(f"📥 Downloading... {bar}\n⚡ Speed: {speed}")
            except Exception:
                pass
    
    await msg.edit("✅ Download complete!")