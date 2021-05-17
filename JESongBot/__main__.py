# Infinity BOTs <https://t.me/Infinity_BOTs>
# @ImJanindu

from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from JESongBot.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from JESongBot import Jebot as app
from JESongBot import LOGGER

pm_start_text = """
Heya [{}](tg://user?id={}), I'm Song Downloader Bot 🎵

Do /help for know my commands

A bot by @Infinity_BOTs
"""

help_text = """
My commands👇

- /song <song name>: download songs via Youtube
- /saavn <song name>: download songs via JioSaavn
- /deezer <song name>: download songs via Deezer
- Send youtube url to my pm for download it on audio format

A bot by @JeBots
"""

credits = """Developer 💻
 • @DeVAJe """


@app.on_message(filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "➕ Add me to a Group ➕",
                url="http://t.me/songjeBot?startgroup=tr",
            )
        ],
        [
            InlineKeyboardButton(
                "Report Bugs 💬", url="https://t.me/DeVAJe"),
        ],
        [
            InlineKeyboardButton("Help 🗣️", callback_data="help"),
            InlineKeyboardButton("Developer 💻", callback_data=b"Credits"),
        ],
        [
            InlineKeyboardButton("📣 Channel", url="https://t.me/JeBots"),
            InlineKeyboardButton("Group 👥", url="https://t.me/JeSupport"),
        ],
    ]
)


    else:
        btn = None
    await message.reply(pm_start_text.format(name, user_id), reply_markup=btn)

@app.on_message(filters.command("help"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
[
        [InlineKeyboardButton("🔙 Back", callback_data="back")],
    ]
)

else:
        btn = None
    await message.reply(help_text.format(name, user_id), reply_markup=btn)

app.start()
LOGGER.info("JESongBot is online.")
idle()
