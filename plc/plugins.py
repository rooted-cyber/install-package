from telethon import *
from userbot import *
from userbot.utils import *
import math
@bot.on(admin_cmd(pattern="sqrt|.sq ?(.*)", outgoing= True,incoming=True))
async def hi(event):
 text = event.pattern_match.group(1)
 if not text:
  await event.edit("Please enter any square number !!!")
  return
 await event.reply(str(math.sqrt(int(text))))
 


@bot.on(admin_cmd(pattern="square ?(.*)", outgoing= True,incoming=True))
async def hi(event):
 text = event.pattern_match.group(1)
 if not text:
  await event.edit("Please enter any number !!!")
  return
 await event.reply(str(f"{text} X {text} = {int(text)*int(text)}"))


@bot.on(admin_cmd(pattern="cube ?(.*)", outgoing= True,incoming=True))
async def hi(event):
 text = event.pattern_match.group(1)
 if not text:
  await event.edit("Please enter any number !!!")
  return
 await event.reply(str(f"{text} X {text} X {text} = {int(text)*int(text)*int(text)}"))


@bot.on(admin_cmd(pattern="table ?(.*)", outgoing= True,incoming=True))
async def hi(event):
 text = event.pattern_match.group(1)
 if not text:
  await event.edit("Please enter Table no !!!")
  return
 await event.edit(f"Starting Table in {text}")
 await event.reply(str(f""" {text} X 1 = {int(text)*1}
{text} X 2 = {int(text)*2}
{text} X 3 = {int(text)*3}
{text} X 4 = {int(text)*4}
{text} X 5 = {int(text)*5}
{text} X 6 = {int(text)*6}
{text} X 7 = {int(text)*7}
{text} X 8 = {int(text)*8}
{text} X 9 = {int(text)*9}
{text} X 10 = {int(text)*10}
"""))


@bot.on(admin_cmd(pattern="mcopy", outgoing= True, incoming=True))
async def hi(event):
  ab = await event.get_reply_message()
  if not ab:
    await event.edit("Reply any message !")
    return
  abc = ab.text
  await event.edit("processing..")
  await ab.reply(f"reply messages : {abc}")




@bot.on(admin_cmd(pattern="mcount", outgoing= True, incoming=True))
async def hi(event):
  ab = await event.get_reply_message()
  if not ab:
   await event.edit("Reply any message !!!")
  abc = ab.text
  await ab.reply(f"Total messages : {len(abc)}")


@bot.on(admin_cmd(pattern="cadmin",incoming=True,outgoing=True))
async def adm(event):
  a = await event.get_reply_message()
  if not a:
   await event.edit("Reply any user !")
   return
  ab = await bot.get_permissions(event.chat_id, a.sender_id)
  if ab.is_admin:
    await a.reply("yes, He is admin")
  else:
    await a.reply("No, He is not admin")



@bot.on(admin_cmd(pattern="mm"))
async def _(event):
  a = await bot.get_messages(event.chat_id, 0, from_user="me")
  b = await bot.get_messages(event.chat_id)
  await event.reply(f" Your Total messages = {a.total}\n\n And Total group messages : {b.total}")




CMD_HELP.update(
    {
        "Plugins": "\n.rename <reply to file and type name>\n usage - reply file rename\n\n"
        ".mcopy <reply to any message>\n usage - copy message and send\n\n"
        ".table <any number> \n usage - Get Table of type number\n\n"
        ".cube <any number>  \n usage - Get cube of type number\n\n"
        ".square <any number>  \n usage - Get square of type number\n\n"
        ".sqrt <any number>  \n usage - Get square root of type number\n\n"
        ".mcount <reply message>  \n usage - Count word of reply message\n\n"
        ".ctt <group username> \n **usage** - Count messages of type group username\n\n"
        " .re <file name> \n **usage** - rename your file\n\n"
        ".cadmin <reply any user> \n **usage** - Check reply user to admin or not admin\n\n"
        ".mm \n usage - Count your send message or Total group message\n\n"
        
    }
)