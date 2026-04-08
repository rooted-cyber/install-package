# Ultroid - GDrive Size (Auto Refresh)

from . import ultroid_cmd, udB, eor
import requests

# 🔁 Get new access token automatically
def get_access_token():
    REFRESH_TOKEN = udB.get_key("GDRIVE_REFRESH")

    if not REFRESH_TOKEN:
        return None

    url = "https://oauth2.googleapis.com/token"
    data = {
        "client_id": "407408718192.apps.googleusercontent.com",
        "client_secret": "secret",
        "refresh_token": REFRESH_TOKEN,
        "grant_type": "refresh_token"
    }

    res = requests.post(url, data=data).json()
    return res.get("access_token")


def get_files(folder_id, token):
    url = "https://www.googleapis.com/drive/v3/files"
    headers = {"Authorization": f"Bearer {token}"}

    files = []
    page_token = None

    while True:
        params = {
            "q": f"'{folder_id}' in parents and trashed=false",
            "fields": "nextPageToken, files(id,name,mimeType,size)",
            "pageSize": 1000
        }

        if page_token:
            params["pageToken"] = page_token

        res = requests.get(url, params=params, headers=headers)
        data = res.json()

        if "error" in data:
            return None, data

        files.extend(data.get("files", []))
        page_token = data.get("nextPageToken")

        if not page_token:
            break

    return files, None


def get_size(folder_id, token, level=0):
    total = 0
    output = ""

    files, error = get_files(folder_id, token)

    if error:
        return 0, "", error

    for f in files:
        if f["mimeType"] == "application/vnd.google-apps.folder":
            size, text, err = get_size(f["id"], token, level + 1)
            if err:
                return 0, "", err
            total += size
            output += "  " * level + f"📁 {f['name']} → {size/1024**3:.2f} GB\n" + text
        else:
            total += int(f.get("size", 0))

    return total, output, None


# 🔐 Save Refresh Token
@ultroid_cmd(pattern="sett( (.*)|$)", fullsudo=True)
async def set_refresh(ult):
    token = ult.pattern_match.group(1).strip()

    if not token:
        return await eor(ult, "❌ Give refresh token!")

    udB.set_key("GDRIVE_REFRESH", token)
    await eor(ult, "✅ Refresh Token Saved!")


# 📦 Check Drive Size
@ultroid_cmd(pattern="gsize$", fullsudo=True)
async def gsize_cmd(ult):
    msg = await eor(ult, "📦 Calculating Drive Size...")

    token = get_access_token()

    if not token:
        return await msg.edit("❌ No refresh token!\nUse `.st <refresh_token>`")

    total, details, error = get_size("root", token)

    if error:
        return await msg.edit(f"❌ API Error:\n`{error}`")

    gb = total / (1024**3)

    text = f"💾 Total Drive Size: {gb:.2f} GB\n\n"
    text += "📊 Folder Breakdown:\n\n"
    text += details[:4000]

    await msg.edit(text)
