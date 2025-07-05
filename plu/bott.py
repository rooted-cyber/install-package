from . import ultroid_bot, udB
import asyncio
from telethon.tl.functions.contacts import UnblockRequest
from random import randint
from pyUltroid.fns.helpers import enable_inline

@ultroid_cmd(pattern="autobot$")
async def make_autobot(e):

    await e.eor("Creating bot... Please wait.")
    
    # Check if a bot token already exists
    if udB.get_key("BOT_TOKEN"):
        return await e.eor("Bot already exists or BOT_TOKEN is set.")

    try:
        await ultroid_bot.start()
        who = ultroid_bot.me
        name = f"{who.first_name}'s Bot"
        username = (who.username + "_bot") if who.username else f"ultroid_{str(who.id)[5:]}_bot"

        bf = "@BotFather"
        await ultroid_bot(UnblockRequest(bf))
        await ultroid_bot.send_message(bf, "/cancel")
        await asyncio.sleep(1)
        
        await ultroid_bot.send_message(bf, "/newbot")
        #await asyncio.sleep(2)

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
    except:
      ptint("hi")
