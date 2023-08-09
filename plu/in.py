from . import get_string, eor

@ultroid_cmd(pattern="in",manager=True)
async def infoo(event):
  re = await event.get_reply_message()
  an = await bot.get_permissions(event.chat_id,re.sender_id)
  if not re:
    await event.edit("Reply any user")
  else:
    pho = await bot.download_profile_photo(re.sender_id)
    await event.eor(get_string("com_1"))
    st = "💚 𝗦𝗢𝗠𝗘 𝗜𝗡𝗙𝗢𝗥𝗠𝗔𝗧𝗜𝗢𝗡 𝗚𝗘𝗡𝗘𝗥𝗔𝗧𝗘 💜"
    a = await bot.get_entity(re.sender_id)
    b = f"{a.first_name}"
    l = f"{a.last_name}"
    u = f"{a.username}"
    id = f"{a.id}"
    fm = f"**First name** : {b}\n**Last name** : {l}\n**Username** : @{u}\n**User id** : {id}\n"
    await event.respond(f"{st}\n{fm}",file=pho)

@ultroid_cmd(pattern="ain",manager=True)
async def int(event):
  await event.eor(get_string("com_1"))
  re = await event.get_reply_message()
  an = await bot.get_permissions(event.chat_id,re.sender_id)
  if not re:
    await event.edit("Reply any user")
    return

  st = "💚 𝗦𝗢𝗠𝗘 𝗜𝗡𝗙𝗢𝗥𝗠𝗔𝗧𝗜𝗢𝗡 𝗚𝗘𝗡𝗘𝗥𝗔𝗧𝗘 💜"
  e = await bot.get_permissions(event.chat_id,re.sender_id)
  f = await bot.get_entity(e.participant.promoted_by)
  usn = f"@{f.username}"
  ma = f"**promoted** : `{e.participant.promoted_by}`({usn})"
  a = await bot.get_entity(re.sender_id)
  b = f"{a.first_name}"
  l = f"{a.last_name}"
  u = f"{a.username}"
  id = f"{a.id}"
  fm = f"**First name** : {b}\n**Last name** : {l}\n**Username** : @{u}\n**User id : {id}\n"
  pho = await bot.download_profile_photo(re.sender_id)
  gh = f"**Admin permission**"
  if an.participant.admin_rights.change_info == True:
    ch = "⚡ **  Change Info ** = ✅"
  else:
    ch = "⚡ **  Change Info ** = ❌"
  if an.participant.admin_rights.post_messages == True:
    pm = "⚡ **  Post Messages ** = ✅"
  else:
    pm = "⚡ **  Post Messages ** = ❌"
  if an.participant.admin_rights.edit_messages == True:
    em = "⚡ **  Edit messages ** = ✅"
  else:
    em = "⚡ **  Edit messages ** = ❌"
  if an.participant.admin_rights.delete_messages == True:
    dm = "⚡ **  Delete Messages ** = ✅"
  else:
    dm = "⚡ **  Delete Messages ** = ❌"
  if an.participant.admin_rights.ban_users == True:
    bu = "⚡ **  Ban users ** = ✅"
  else:
    bu = "⚡ **  Ban users ** = ❌"
  if an.participant.admin_rights.invite_users == True:
    iu = "⚡ **  Invite Users ** = ✅"
  else:
    iu = "⚡ **  Invite Users ** = ❌"
  if an.participant.admin_rights.pin_messages == True:
    pms = "⚡ **  Pin Messages ** = ✅"
  else:
    pms = "⚡ **  Pin_Messages ** = ❌"
  if an.participant.admin_rights.add_admins == True:
    ad = "⚡ **  Add Admins ** = ✅"
  else:
    ad = "⚡ **  Add Admins ** = ❌"
  if an.participant.admin_rights.manage_call == True:
    mc = "⚡ **  Manage Voice Chat ** = ✅"
  else:
    mc = "⚡ **  Manage Voice Chat  ** = ❌"
  if an.participant.admin_rights.other == True:
    ot = "⚡ **  Other ** = ✅"
  else:
    ot = "⚡ **  Other ** = ❌"

  sa = await bot.get_permissions(event.chat_id,re.sender_id)
  sb = sa.is_admin
  if sb == True:
    await event.client.send_message(event.chat_id,f"{st}\n\n{fm}\n{gh}\n{ma}\n{ch}\n{pm}\n{em}\n{dm}\n{bu}\n{iu}\n{pms}\n{ad}\n{mc}\n{ot}",file=pho)
