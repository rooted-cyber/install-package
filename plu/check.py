from . import ultroid_cmd

@ultroid_cmd(pattern="ch ?(.*)")
async def check_user(event):
    username = event.pattern_match.group(1).strip()
    if not username:
        return await event.eor("Please provide a username to check.")

    try:
        user = await event.client.get_entity(username)
    except Exception as e:
        return await event.eor(f"Error: {str(e)}")

    groups_list = []
    total_groups = 0
    async for dialog in event.client.iter_dialogs():
        entity = dialog.entity
        if getattr(entity, "megagroup", False) and not getattr(entity, "broadcast", False):
            total_groups += 1
            groups_list.append(entity.title)

    if total_groups == 0:
        return await event.eor("No groups found for the user.")

    response = f"Total Groups Joined: {total_groups}\n" + "\n".join(groups_list)

    # Split and send response in chunks if necessary
    max_length = 4096
    for i in range(0, len(response), max_length):
        await event.respond(response[i:i + max_length])