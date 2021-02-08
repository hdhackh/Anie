
#    Copyright (C) Midhun KM 2020-2021
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import requests
from bs4 import BeautifulSoup
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
import hachoir
import asyncio
import os
from pathlib import Path
from selenium import webdriver
import time
import requests
import shutil
import os
import argparse
import wget
from fridaybot import bot as borg
import lottie
from fridaybot.utils import load_module
from telethon.tl.types import DocumentAttributeAudio


async def fetch_audio(event, ws):
    if not event.reply_to_msg_id:
        await event.edit("`Reply To A Video / Audio.`")
        return
    warner_stark = await event.get_reply_message()    
    if warner_stark.audio is None  and warner_stark.video is None:
        await event.edit("`Format Not Supported`")
        return
    if warner_stark.video:
        await event.edit("`Video Detected, Converting To Audio !`")
        warner_bros = await event.client.download_media(warner_stark.media)
        stark_cmd = f"ffmpeg -i {warner_bros} -map 0:a friday.mp3"
        stdout, stderr = (await runcmd(stark_cmd))[:2]
        final_warner = "friday.mp3"
    elif warner_stark.audio:
        await event.edit("`Download Started !`")
        final_warner = await event.client.download_media(warner_stark.media)
    await event.edit("`Almost Done!`")    
    return final_warner
