# plugins/mkbot.py (इसे Ultroid के plugins फोल्डर में सेव करें)

from . import ultroid_cmd, ultroid_bot, LOGS
import asyncio
from telethon.tl.functions.contacts import UnblockRequest
from random import randint
from telethon import errors  # Telethon की त्रुटियों को हैंडल करने के लिए

# BotFather से प्रतिक्रियाओं को पार्स करने के लिए कुछ सहायक टेक्स्ट
BOT_FATHER_SUCCESS_START = "Good."
BOT_FATHER_DONE_START = "Done!"
BOT_FATHER_BOT_LIMIT_KEYWORD = "20 bots"
BOT_FATHER_CANNOT_KEYWORD = "cannot"
BOT_FATHER_SORRY_KEYWORD = "Sorry"
BOT_FATHER_TOKEN_PREFIX = "`" # Token `backticks` के बीच होता

@ultroid_cmd(pattern="mbot$")
async def make_autobot(e):
    bf = "@botfather"
    await ultroid_bot.send_message(bf,"/newbot")
    await asyncio.sleep(3)
    ab = (await ultroid_bot.get_messages(bf, limit=1))[0].text
    if ab.endswith("seconds."):
        return await e.eor(f"""**𝗰𝘂𝗿𝗿𝗲𝗻𝘁𝗹𝘆 𝗯𝗹𝗼𝗰𝗸𝗲𝗱 𝗶️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️𝗻 𝗯𝗼𝘁𝗳𝗮𝘁𝗵𝗲𝗿.**
`{ab}`""")
    else:
        await e.eor("Creating bot... Please wait.")
    
    who = await ultroid_bot.get_me() # .me के बजाय get_me() का उपयोग करें
    name = who.first_name + "'s Bot"
    # यदि who.username नहीं है, तो एक अधिक मजबूत डिफ़ॉल्ट प्रदान करें
    username = (who.username + "_ultroid_bot") if who.username else f"rooted_{str(who.id)[-6:]}_bot" 
    
    bf = "@BotFather"

    try:
        await ultroid_bot(UnblockRequest(bf))
        # BotFather से पिछले इंटरैक्शन को साफ करने के लिए कुछ कमांड
        await ultroid_bot.send_message(bf, "/cancel")
        await asyncio.sleep(1) # Flood से बचने के लिए थोड़ा इंतजार करें
        await ultroid_bot.send_message(bf, "/newbot")
        await asyncio.sleep(2) # Flood से बचने के लिए थोड़ा इंतजार करें

        # BotFather की प्रतिक्रिया प्राप्त करें
        # get_messages में limit=1 का मतलब सबसे नया मैसेज है
        resp_msg = (await ultroid_bot.get_messages(bf, limit=1))[0]
        resp_text = resp_msg.text if resp_msg else "" # सुनिश्चित करें कि मैसेज खाली नहीं है

        if BOT_FATHER_BOT_LIMIT_KEYWORD in resp_text or BOT_FATHER_CANNOT_KEYWORD in resp_text.lower():
            return await e.eor(f"❌ BotFather से प्रतिक्रिया: {resp_text}\n"
                               "बहुत सारे बॉट। एक को हटाएं या BOT_TOKEN मैन्युअल रूप से सेट करें।")

        await ultroid_bot.send_message(bf, name)
        await asyncio.sleep(2) # Flood से बचने के लिए थोड़ा इंतजार करें

        resp_msg = (await ultroid_bot.get_messages(bf, limit=1))[0]
        resp_text = resp_msg.text if resp_msg else ""

        # यदि पहला नाम स्वीकार नहीं किया जाता है, तो एक वैकल्पिक नाम का प्रयास करें
        if not resp_text.startswith(BOT_FATHER_SUCCESS_START):
            LOGS.info("BotFather ने पहला बॉट नाम स्वीकार नहीं किया, वैकल्पिक नाम का प्रयास कर रहा है।")
            await ultroid_bot.send_message(bf, "rootedcyber_bot") # या कोई और सामान्य नाम
            await asyncio.sleep(2)

        # बॉट के लिए यूजरनेम भेजें
        await ultroid_bot.send_message(bf, username)
        await asyncio.sleep(3) # Flood से बचने के लिए थोड़ा अधिक इंतजार करें

        resp_msg = (await ultroid_bot.get_messages(bf, limit=1))[0]
        resp_text = resp_msg.text if resp_msg else ""

        # यदि यूजरनेम पहले से ही लिया गया है, तो एक नया यूजरनेम उत्पन्न करें
        if resp_text.startswith(BOT_FATHER_SORRY_KEYWORD):
            LOGS.warning(f"BotFather ने यूजरनेम '{username}' को अस्वीकार कर दिया। नया उत्पन्न कर रहा है।")
            username = f"rootedcyber_{str(who.id)[-5:]}{randint(10, 99)}_bot" # अधिक विविधता के लिए randint को 10-99 करें
            await ultroid_bot.send_message(bf, username)
            await asyncio.sleep(3) # Flood से बचने के लिए और इंतजार करें

            resp_msg = (await ultroid_bot.get_messages(bf, limit=1))[0] # नए यूजरनेम के लिए प्रतिक्रिया
            resp_text = resp_msg.text if resp_msg else ""
            
            # यदि दूसरा यूजरनेम भी अस्वीकार कर दिया जाता है
            if resp_text.startswith(BOT_FATHER_SORRY_KEYWORD):
                return await e.eor(f"❌ बॉट के लिए यूजरनेम बनाने में विफल रहा। BotFather ने '{username}' भी अस्वीकार कर दिया।")
        
        # अंत में बॉट टोकन की जांच करें
        if resp_text.startswith(BOT_FATHER_DONE_START):
            # टोकन `backticks` के बीच होता है
            try:
                token = resp_text.split(BOT_FATHER_TOKEN_PREFIX)[1].split(BOT_FATHER_TOKEN_PREFIX)[0]
                # enable_inline फ़ंक्शन उपलब्ध है या नहीं, यह सुनिश्चित करने के लिए जांच करें
                # from pyUltroid.core.helpers import enable_inline # अगर यह .pyUltroid में है तो इसे आयात करें
                # if 'enable_inline' in locals(): # अगर इसे वैश्विक रूप से या कहीं और परिभाषित किया गया है
                #    await enable_inline(ultroid_bot, username)
                # else:
                #    LOGS.warning("enable_inline फ़ंक्शन उपलब्ध नहीं है। कृपया इसे मैन्युअल रूप से चलाएं।")

                await e.reply(f"✅ सफलतापूर्वक @{username} बनाया गया। \n**टोकन**: `{token}`\n")
                # आप चाहें तो इसे किसी लॉग चैनल या अन्य स्थान पर भी भेज सकते हैं
            except IndexError:
                await e.eor(f"❌ BotFather से बॉट टोकन निकालने में विफल रहा। पूरी प्रतिक्रिया देखें:\n`{resp_text}`")
            except Exception as ex:
                LOGS.exception(f"बॉट बनाने के बाद की प्रक्रिया में त्रुटि: {ex}")
                await e.eor(f"✅ सफलतापूर्वक @{username} बनाया गया, लेकिन कुछ अतिरिक्त सेटअप में समस्या आई।\n**टोकन**: BotFather चैट में देखें।")

        else:
            await e.eor(f"❌ बॉट बनाने में विफल रहा। कारण देखें: \n`{resp_text}`")
            # BotFather से अंतिम मैसेज भी दिखा सकते हैं
            await ultroid_bot.send_message(bf, "/newbot") # इसे फिर से भेजने की जरूरत नहीं है
            await asyncio.sleep(3)
            b = (await ultroid_bot.get_messages(bf))[0].text # यह पिछले मैसेज को ही दिखाएगा
            await e.eor(f"BotFather से अंतिम स्थिति:\n`{b}`")

    except errors.FloodWaitError as ex:
        # यदि Telegram Floodwait त्रुटि भेजता है
        await e.eor(f"⚠️ Telegram Flood Wait त्रुटि: कृपया {ex.seconds} सेकंड बाद पुनः प्रयास करें।")
        LOGS.warning(f"Telegram Flood Wait: {ex.seconds} seconds.")
    except Exception as ex:
        LOGS.exception(f"बॉट बनाने की प्रक्रिया में एक अप्रत्याशित त्रुटि हुई: {ex}")
        await e.eor(f"❌ बॉट बनाने की प्रक्रिया में एक अप्रत्याशित त्रुटि हुई: ")


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


@ultroid_cmd(pattern="token ?(.*)")
async def token_by_username(e):
    username = e.pattern_match.group(1)
    if not username:
        return await e.eor("🔤 Bot username do: `.token <username>`")

    bf = "@BotFather"
    await e.client.send_message(bf, "/cancel")
    await asyncio.sleep(1)
    await e.client.send_message(bf, "/token")
    await e.client.send_message(bf, f"{username}")
    rp = (await ultroid_bot.get_messages(bf, limit=1))[0].text
    if rp.startswith("You"):
      token = rp.split("`")[1]
      await e.eor(f"""Bot : {username}
        token : {token}""")
