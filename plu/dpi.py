from . import *

@ultroid_cmd(pattern="dpi ?(.*)")
async def _(e):
    value = e.pattern_match.group(1)
    if not value.isdigit():
        return await eor(e, "⚠️ Sahi DPI value do. Example: `.dpi 350`")

    await eor(e, f"🔧 DPI set kar rahe hain: `{value}`")

    try:
        # ADB shell command to change DPI
        import subprocess
        cmd = ["adb", "shell", "wm", "density", value]
        subprocess.run(cmd, check=True)

        return await eor(e, f"✅ DPI `{value}` pe set ho gaya.\nReboot required ho sakta hai.")
    except Exception as err:
        return await eor(e, f"❌ Error: {err}\nADB ya Root access zaroori hai.")