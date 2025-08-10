from . import get_string, eor, ultroid_cmd, inline_mention

@ultroid_cmd(pattern="inf$", manager=True)
async def int(event):
    await event.eor(get_string("com_1"))
    re = await event.get_reply_message()
    re += event.pattern_match.group(1)
    if re:
        rp = inline_mention(re.sender)
        rc = await event.client.get_messages(event.chat_id, limit=0, from_user=re.sender_id)
        to = f"Total msgs = {rc.total} msgs"
    else:
        await event.edit("Reply to a user first.")
        return

    bot = event.client
    pp = f"phone number : {re.sender.phone}" or ""
    try:
        an = await bot.get_permissions(event.chat_id, re.sender_id)
    except Exception as e:
        await event.edit(f"Failed to get permissions: {e}")
        return

    user = await bot.get_entity(re.sender_id)
    photo = await bot.download_profile_photo(re.sender_id)

    st = "💚 𝗦𝗢𝗠𝗘 𝗜𝗡𝗙𝗢𝗥𝗠𝗔𝗧𝗜𝗢𝗡 𝗚𝗘𝗡𝗘𝗥𝗔𝗧𝗘 💜"
    fn = user.first_name
    ln = user.last_name if user.last_name else "None"
    uname = f"@{user.username}" if user.username else "None"
    uid = user.id
    fm = f"**First Name**: {fn}\n**Last Name**: {ln}\n**Username**: {uname}\n**User ID**: {uid}\n"

    is_admin = an.is_admin
    if is_admin:
        try:
            promoted_by = an.participant.promoted_by
            prom_entity = await bot.get_entity(promoted_by)
            prom = f"@{prom_entity.username}" if prom_entity.username else f"{promoted_by}"
            ma = f"**Promoted by**: {prom}"
        except Exception as e:
            ma = "**Promoted by**: Unknown"
        
        rights = an.participant.admin_rights
        def check(right): return "✅" if getattr(rights, right, False) else "❌"
        
        perms = f"""*Admin Permissions*:
⚡ Change Info = {check('change_info')}
⚡ Post Messages = {check('post_messages')}
⚡ Edit Messages = {check('edit_messages')}
⚡ Delete Messages = {check('delete_messages')}
⚡ Ban Users = {check('ban_users')}
⚡ Invite Users = {check('invite_users')}
⚡ Pin Messages = {check('pin_messages')}
⚡ Add Admins = {check('add_admins')}
⚡ Manage Calls = {check('manage_call')}
⚡ Other = {check('other')}
"""
    else:
        ma = "**User is not an admin**"
        perms = ""

    await event.client.send_message(event.chat_id, f"{st}\n{fm}\n{to}\n{pp}\n{ma}\n{perms}", file=photo)


