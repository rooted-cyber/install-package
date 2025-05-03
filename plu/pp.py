from . import ultroid_cmd
import subprocess

@ultroid_cmd(pattern="pp (i|u|s|f|c) ?(.*)")
async def pip_manager(event):
    action = event.pattern_match.group(1)
    package = event.pattern_match.group(2).strip()

    await event.eor("🕐 Processing...")

    if action == "i":
        if not package:
            return await event.eor("❌ Please provide a package name to install.")
        cmd = f"pip install {package}"
        msg = f"📦 Installing {package}..."

    elif action == "u":
        if not package:
            return await event.eor("❌ Please provide a package name to uninstall.")
        cmd = f"pip uninstall -y {package}"
        msg = f"📦 Uninstalling {package}..."

    elif action == "s":
        if not package:
            return await event.eor("❌ Please provide a package name to show info.")
        cmd = f"pip show {package}"
        msg = f"📦 Showing info for {package}..."

    elif action == "f":
        cmd = "pip freeze"
        msg = "📦 Listing all installed pip packages..."

    elif action == "c":
        if not package:
            return await event.eor("❌ Please provide a package name to check.")
        result = subprocess.getoutput(f"pip freeze | grep {package}")
        if result:
            return await event.eor(f"✅ {package} is installed.\n\n<code>{result}</code>", parse_mode="html")
        else:
            return await event.eor(f"❌ {package} is not installed.")

    else:
        return await event.eor("❌ Invalid command.")

    try:
        output = subprocess.getoutput(cmd)
        await event.eor(f"{msg}\n\n<code>{output}</code>", parse_mode="html")
    except Exception as e:
        await event.eor(f"⚠️ Error:\n<code>{str(e)}</code>", parse_mode="html")