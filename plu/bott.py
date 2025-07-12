from . import *
import asyncio
from telethon.tl.functions.contacts import UnblockRequest
from random import randint
#from pyUltroid.core.helpers import enable_inline

@ultroid_cmd(pattern="mkbot$")
async def make_autobot(e):
    from . import udB, ultroid_bot, LOGS

    await e.eor("Creating bot... Please wait.")
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
        await ultroid_bot.send_message(bf,"rootedcyber bot")
        await asyncio.sleep(1)

    await ultroid_bot.send_message(bf, username)
    await asyncio.sleep(2)
    resp = (await ultroid_bot.get_messages(bf, limit=1))[0].text

    if resp.startswith("Sorry"):
        username = f"rootedcyber_{str(who.id)[6:]}{randint(1, 99)}_bot"
        await ultroid_bot.send_message(bf, username)
        await ultroid_bot.send_message(chat, username)
        return await asyncio.sleep(2)
        resp = (await ultroid_bot.get_messages(bf, limit=1))[0].text

    if resp.startswith("Done!"):
        token = resp.split("`")[1]
        await e.eor(token)
        await enable_inline(ultroid_bot, username)
        await e.eor(f"✅ Successfully created @{username} \n Token : `{token}`")
    else:
        await e.eor("❌ Failed to create bot. see reason")
        await ultroid_bot.send_message(bf,"/newbot")
        b = (await ultroid_bot.get_messages(bf))[0].text
        await e.eor(f"{b}")


import asyncio

@ultroid_cmd(pattern="dlbot ?(.*)")
async def delbot_by_username(e):
    username = e.pattern_match.group(1)
    if not username:
        return await e.eor("🔤 Bot username do: `.delbot <username>`")

    bf = "@BotFather"
    #await e.eor("🗑 Bot delete request sent. BotFather me jaake confirm karo.")
    try:
        await e.client.send_message(bf, "/cancel")
        await asyncio.sleep(1)
        await e.client.send_message(bf, "/deletebot")
        await asyncio.sleep(1)
        await e.client.send_message(bf, f"{username}")
        await asyncio.sleep(1)
        isdone = (await ultroid_bot.get_messages("@botFather", limit=1))[0].text
        if isdone.startswith("Invalid"):
            return await e.eor(f"Not Found @{username}")
        await e.client.send_message(bf,"""Yes, I am totally sure.""")
        await e.respond(f"✅Successfully delete {username}")
    except Exception as ex:
        await e.eor(f"⚠️ Error: {ex}")
