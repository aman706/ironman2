from aiohttp import ClientSession
import html 
import re 

from YoneRobot import *
from YoneRobot.events import register

#value
ARQ_API_KEY = "QCRJIN-MJOBNZ-SPYKTN-NFZKZZ-ARQ"
ARQ_API_URL = "https://thearq.tech/"

aiohttpsession = ClientSession()
arq = ARQ(ARQ_API_URL, ARQ_API_KEY, aiohttpsession)

from YoneRobot import pbot as app
from YoneRobot.pyrogramee.errors import capture_err
from YoneRobot.pyrogramee.json_prettify import json_prettify
from YoneRobot.pyrogramee.fetch import fetch
from pyrogram import filters

@app.on_message(filters.command("covid") & ~filters.edited)
@capture_err
async def lyrics_func(_, message):
    if len(message.command) < 2:
        await message.reply_text("**Sike That's The Wrong Command Usage!** \nUse `/lyrics` (song name)")
        return
    m = await message.reply_text("**Searching For Song Lyrics**")
    query = message.text.strip().split(None, 1)[1]
    song = await arq.lyrics(query)
    lyrics = song.result
    if len(lyrics) < 4095:
        await m.edit(f"__{lyrics}__")
        return
    lyrics = await paste(lyrics)
    await m.edit(f"**Oops! Lyrics Too Long To Send!** \n**Your Song Lyrics: [Click Here]({lyrics})**")