import os
from pyrogram import Client, filters
from pyrogram.types import *
hl = "."

@Client.on_message(filters.command("nice",  hl) & filters.private & filters.me)
async def self_media(client, message):
    replied = message.reply_to_message
    if not replied:
        return
    if not (replied.photo or replied.video):
        return
    fuck = await client.download_media(replied)
    await client.send_document("me", fuck)
    os.remove(fuck)
