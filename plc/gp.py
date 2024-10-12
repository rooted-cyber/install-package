from . import *
@bot.on(events.NewMessage(pattern='\.bh', from_users='me'))
async def bhai(event):
 text = event.text.split(maxsplit=1)
 if event.is_reply and not len(text) == 2:
  msg = await event.get_reply_message()
  query = msg.text
 elif len(text) == 2:
  query = text[1]
 else:
  pass
 reply = await event.reply('𝙂𝙚𝙩𝙩𝙞𝙣𝙜 𝙧𝙚𝙨𝙥𝙤𝙣𝙨𝙚 𝙛𝙧𝙤𝙢 𝙗𝙝𝙖𝙞')
 extra = "<p>You are user's friend.You need to reply to query in a friendly tone in hindi using emojies and adress user as bhai using words like &quot;Arey bhai&quot;,&quot;Nahi bhai&quot;,&quot;Haan bhai&quot;,&quot;Theek bhai&quot; etc.Your query is:</p>"
 text = extra + query
 params = {"model_id": 5, "prompt": text}
 req = requests.post('https://lexica.qewertyy.me/models', params=params)
 if req.status_code == 200:
  req = req.json()
  text = '𝘽𝙝𝙖𝙞:' + '\n\n' + req['content']
  await reply.edit(text)