"""Execute GNU/Linux commands inside Telegram
Syntax: .exec Code"""
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
import asyncio
import io
import time

from . import ALIVE_NAME

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Aɳιҽ"
from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="salive ?(.*)"))
async def _(event):
    if event.fwd_from or event.via_bot_id:
        return
    PROCESS_RUN_TIME = 100
    cmd = event.pattern_match.group(1)
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    e = stderr.decode()
    if not e:
        e = "No Error"
    o = stdout.decode()
    if not o:
        o = "**Tip**: \n`If you want to see the results of your code, I suggest printing them to stdout.`"
    else:
        _o = o.split("\n")
        o = "`\n".join(_o)
    OUTPUT = f"        ꧁༒☬𝓐𝓷𝓲𝓮☬༒꧂\nAႦσυƚ ɱყ ʂყʂƚҽɱ\n➾ Tҽʅҽƚԋσɳ Vҽɾʂισɳ= 1.17.5\n➾Cσρყɾιɠԋƚ Ⴆყ= Aɳιҽ\n➾Mყ Mαʂƚҽɾ = {DEFAULTUSER}\n"
    if len(OUTPUT) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(OUTPUT)) as out_file:
            out_file.name = "exec.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=cmd,
                reply_to=reply_to_id,
            )
            await event.delete()
    await event.edit(OUTPUT)
