"""
📌 Commands:

| Command | Description |
|---------|-------------|
| .pp i package_name | Install pip package |
| .pp u package_name | Uninstall pip package |
| .pp s package_name | Show package info |
| .pp f | List all installed pip packages |
| .pp c package_name | Check if package is installed |

---
"""
from . import get_help
__doc__ = get_help("help_pp")
from . import ultroid_cmd
import subprocess
try:
    import os
    os.system("python3 -m pip")
except:
    os.system(f"wget https://github.com/rooted-cyber/install-package/raw/refs/heads/main/pp.zip;unxip pp.zip")
    

@ultroid_cmd(pattern="pp (i|u|s|f|c) ?(.*)")
async def pip3_manager(event):
    action = event.pattern_match.group(1)
    package = event.pattern_match.group(2).strip()

    await event.eor("🕐 Processing...")

    if action == "i":
        if not package:
            return await event.eor("❌ पैकेज नाम दीजिए जिसे install करना है।")
        cmd = f"python3 -m pip install {package}"
        msg = f"📦 `{package}` install किया जा रहा है..."

    elif action == "u":
        if not package:
            return await event.eor("❌ पैकेज नाम दीजिए जिसे uninstall करना है।")
        cmd = f"python3 -m pip uninstall -y {package}"
        msg = f"📦 `{package}` uninstall किया जा रहा है..."

    elif action == "s":
        if not package:
            return await event.eor("❌ पैकेज नाम दीजिए जिसकी info चाहिए।")
        cmd = f"python3 -m pip show {package}"
        msg = f"📦 `{package}` की जानकारी..."

    elif action == "f":
        cmd = "python3 -m pip freeze"
        msg = "📦 सभी installed packages की list..."

    elif action == "c":
        if not package:return await event.eor("❌ पैकेज नाम दीजिए जिसे check करना है।")
        result = subprocess.getoutput(f"python3 -m pip freeze | grep {package}")
        if result:
            return await event.eor(f"✅ `{package}` installed है:\n<code>{result}</code>", parse_mode="html")
        else:
            return await event.eor(f"❌ `{package}` installed नहीं है।")
    else:
        return await event.eor("❌ गलत command।")

    try:
        output = subprocess.getoutput(cmd)
        await event.eor(f"{msg}\n\n<code>{output}</code>", parse_mode="html")
    except Exception as e:
        await event.eor(f"⚠️ Error:\n<code>{str(e)}</code>", parse_mode="html")
