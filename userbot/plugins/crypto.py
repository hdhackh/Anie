# Made By @RoseloverX Kang With Credits Else Gey [Modified from @xditya's Plugin]

from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

naam = str(ALIVE_NAME)

bot = "@HeathonCryptoBot"


@borg.on(admin_cmd("btc ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    sysarg = event.pattern_match.group(1)
    if sysarg == "":
        async with borg.conversation(bot) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/btc ")
                audio = await conv.get_response()
                await borg.send_message(event.chat_id, audio.text)
                await event.delete()
            except YouBlockedUserError:
                await event.edit("Error: unblock @HeathonCryptoBot and retry!")
    elif "@" in sysarg:
        async with borg.conversation(bot) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/btc " + sysarg)
                audio = await conv.get_response()
                await borg.send_message(event.chat_id, audio.text)
                await event.delete()
            except YouBlockedUserError:
                await event.edit("Error: unblock @HeathonCryptoBot and try again!")
    elif "" in sysarg:
        async with borg.conversation(bot) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/btc " + sysarg)
                audio = await conv.get_response()
                await borg.send_message(event.chat_id, audio.text)
                await event.delete()
            except YouBlockedUserError:
                await event.edit("Error: unblock @HeathonCryptoBot `and try again!")


bot = "@HeathonCryptoBot"


@borg.on(admin_cmd("crypto ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    sysarg = event.pattern_match.group(1)
    if sysarg == "":
        async with borg.conversation(bot) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/crypto ")
                audio = await conv.get_response()
                await borg.send_message(event.chat_id, audio.text)
                await event.delete()
            except YouBlockedUserError:
                await event.edit("Error: unblock @HeathonCryptoBot and retry!")
    elif "@" in sysarg:
        async with borg.conversation(bot) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/crypto " + sysarg)
                audio = await conv.get_response()
                await borg.send_message(event.chat_id, audio.text)
                await event.delete()
            except YouBlockedUserError:
                await event.edit("Error: unblock @HeathonCryptoBot and try again!")
    elif "" in sysarg:
        async with borg.conversation(bot) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/crypto " + sysarg)
                audio = await conv.get_response()
                await borg.send_message(event.chat_id, audio.text)
                await event.delete()
            except YouBlockedUserError:
                await event.edit("Error: unblock @HeathonCryptoBot `and try again!")
