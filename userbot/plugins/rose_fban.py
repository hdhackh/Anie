@borg.on(admin_cmd("fban ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    sysarg = event.pattern_match.group(1)
    if sysarg == "":
        async with borg.conversation(bot) as conv:
            try:
                await conv.send_message("/fban ")
                audio = await conv.get_response()
                await borg.send_message(event.chat_id, audio.text)
                await event.delete()
            except YouBlockedUserError:
                await event.edit("Error: unblock @Carol5_bot and retry!")
    elif "@" in sysarg:
        async with borg.conversation(bot) as conv:
            try:
                await conv.send_message("/fban " + sysarg)
                audio = await conv.get_response()
                await borg.send_message(event.chat_id, audio.text)
                await event.delete()
            except YouBlockedUserError:
                await event.edit("Error: unblock @Carol5_bot and try again!")
    elif "" in sysarg:
        async with borg.conversation(bot) as conv:
            try:
                await conv.send_message("/fban " + sysarg)
                audio = await conv.get_response()
                await borg.send_message(event.chat_id, audio.text)
                await event.delete()
            except YouBlockedUserError:
                await event.edit("Error: unblock @Carol5_bot `and try again!")
