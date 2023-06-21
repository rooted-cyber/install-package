@ultroid_cmd(pattern="msg ?(.*)")
async def msg(event):
	inp = event.pattern_match.group(1)
	reply = await event.get_reply_message()
	await bot.send_message(reply.fwd_from.from_id, f"{inp}")
	a = reply.fwd_from.from_id.user_id
	b = await bot.get_entity(a)
	c = b.username
	u = (f"@{c}")
	await event.reply(f"Your message sent {u}")