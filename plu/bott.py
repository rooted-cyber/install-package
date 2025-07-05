from . import *
import asyncio
from telethon.tl.functions.contacts import UnblockRequest
from random import randint
#from pyUltroid.core.helpers import enable_inline

@ultroid_cmd(pattern="autobot$")
async def make_autobot(e):
    from . import udB, ultroid_bot, LOGS

    await e.eor("Creating bot... Please wait.")
    if udB.get_key("_TOKEN"):
        return await e.eor("Bot already exists or BOT_TOKEN is set.")

    await ultroid_bot.start()
    who = ultroid_bot.me
    name = who.first_name + "'s Bot"
    username = (who.username + "_bot") if who.username else f"ultroid_{str(who.id)[5:]}_bot"

    bf = "@BotFather"
    await ultroid_bot(UnblockRequest(bf))
    await ultroid_bot.send_message(bf, "/cancel")
    await asyncio.sleep(1)
    await ultroid_bot.send_message(bf, "/newbot")
    await asyncio.sleep(2)

    resp = (await ultroid_bot.get_messages(bf, limit=1))[0].text
    if "20 bots" in resp or "cannot" in resp.lower():
        return await e.eor("Too many bots. Delete one or set BOT_TOKEN manually.")

    await ultroid_bot.send_message(bf, name)
    await asyncio.sleep(1)
    resp = (await ultroid_bot.get_messages(bf, limit=1))[0].text
    if not resp.startswith("Good."):
        await ultroid_bot.send_message(bf, "Ultroid Assistant Bot")
        await asyncio.sleep(1)

    await ultroid_bot.send_message(bf, username)
    await asyncio.sleep(2)
    resp = (await ultroid_bot.get_messages(bf, limit=1))[0].text

    if resp.startswith("Sorry"):
        username = f"ultroid_{str(who.id)[6:]}{randint(1, 99)}_bot"
        await ultroid_bot.send_message(bf, username)
        await asyncio.sleep(2)
        resp = (await ultroid_bot.get_messages(bf, limit=1))[0].text

    if resp.startswith("Done!"):
        token = resp.split("`")[1]
        await e.eor(token)
        await enable_inline(ultroid_bot, username)
        await e.eor(f"✅ Successfully created @{username} \n Token : `{token}`")
    else:
        await e.eor("❌ Failed to create bot. Delete old bots or set BOT_TOKEN manually.")
