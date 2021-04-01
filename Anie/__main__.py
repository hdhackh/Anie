from pathlib import Path
from sys import argv

import telethon.utils
from telethon import TelegramClient

from Anie import BOT_USERNAME, TOKEN, bot
from Anie.utils import load_module


async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me()
    bot.uid = telethon.utils.get_peer_id(bot.me)


if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tbot = None
    if BOT_USERNAME is not None:
        print("Initiating Inline Bot")
        bot.tbot = TelegramClient("Anie", api_id=API_KEY, api_hash=API_HASH).start(
            bot_token=TOKEN
        )
        print("Initialisation finished with no errors")
        print("Starting Userbot")
        bot.loop.run_until_complete(add_bot(BOT_USERNAME))
        print("Startup Completed")
    else:
        bot.start()


import glob

path = "Anie/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))

print("Anie Bot has been successfully Established Now Try Ping.")

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
