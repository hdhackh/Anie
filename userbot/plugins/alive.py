# Thanks to Sipak bro and Aryan..
# animation Idea by @ItzSipak && @Hell boy_pikachu
# Made by @hellboi_atul ....and thanks to @Crackexy for the logos...
# Kang with credits else gay...
import asyncio
import time

from userbot import ALIVE_NAME
from userbot.__init__ import StartTime
from userbot.utils import admin_cmd, sudo_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "ǟռɨɛ"


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


uptime = get_readable_time((time.time() - StartTime))

# Thanks to Sipak bro and Aryan..
# animation Idea by @ItzSipak && @Hell boy_pikachu
# Made by @hellboi_atul ....and thanks to @Crackexy for the logos...
# Kang with credits else gay...
# alive.py for DC(DARK COBRA)
global ghanti
ghanti = borg.uid
edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/74baa0fee2d1f3cc8112d.jpg"
file2 = "https://telegra.ph/file/897db0c5f8f06134556f2.jpg"
file3 = "https://telegra.ph/file/09c1cb99d4bd6f0b9cbad.jpg"
file4 = "https://telegra.ph/file/9271370fd1f5dd877388b.jpg"
""" =======================CONSTANTS====================== """


@borg.on(admin_cmd(pattern=r"alive"))
@borg.on(sudo_cmd(pattern=r"alive", allow_sudo=True))
async def hmm(yes):
    await yes.get_chat()
    global ghanti
    ghanti = borg.uid
    await yes.delete()
    pm_caption = "**↤↤↤↤↤ ★彡ᴀɴɪᴇ彡★ ↦↦↦↦↦**\n\n"
    pm_caption += "**ᴀᴡᴀᴋᴇ ᴀɴᴅ ᴀʟɪᴠᴇ**\n\n"
    pm_caption += "**ᴀʙᴏᴜᴛ ᴍʏ ꜱʏꜱᴛᴇᴍ**\n\n"
    pm_caption += f"**ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ:** 1.20.0\n"
    pm_caption += f"**ᴀᴡᴀᴋᴇ ꜱɪɴᴄᴇ:** {uptime}\n\n"
    pm_caption += f"**ᴍᴀꜱᴛᴇʀ** [{DEFAULTUSER}](tg://user?id={ghanti})\n"
    on = await borg.send_file(yes.chat_id, caption=pm_caption)
