import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from deep_translator import GoogleTranslator

from ShrutiCHATBOT import ShrutiCHATBOT, db
from ShrutiCHATBOT.modules.helpers import CHATBOT_ON
from ShrutiCHATBOT.database.chats import add_served_chat
from ShrutiCHATBOT.database.users import add_served_user

translator = GoogleTranslator()

lang_db = db.ChatLangDb.LangCollection


# 🔹 Generate language selection buttons
def generate_language_buttons(languages):
    buttons = []
    current_row = []
    for lang, code in languages.items():
        current_row.append(
            InlineKeyboardButton(lang.capitalize(), callback_data=f"setlang_{code}")
        )
        if len(current_row) == 4:
            buttons.append(current_row)
            current_row = []
    if current_row:
        buttons.append(current_row)
    return InlineKeyboardMarkup(buttons)


# 🔹 Get language from DB
async def get_chat_language(chat_id):
    chat_lang = await lang_db.find_one({"chat_id": chat_id})
    return chat_lang["language"] if chat_lang and "language" in chat_lang else "en"


# 🔹 Set chat language
@ShrutiCHATBOT.on_message(filters.command(["lang", "language", "setlang"]))
async def set_language(client: Client, message: Message):
    await message.reply_text(
        "Please select your chat language:",
        reply_markup=generate_language_buttons(languages),
    )


# 🔹 Reset language
@ShrutiCHATBOT.on_message(filters.command(["resetlang", "nolang"]))
async def reset_language(client: Client, message: Message):
    chat_id = message.chat.id
    lang_db.update_one(
        {"chat_id": chat_id}, {"$set": {"language": "nolang"}}, upsert=True
    )
    await message.reply_text(
        "**Bot language has been reset in this chat to mix language.**"
    )


# 🔹 Chatbot ON/OFF settings
@ShrutiCHATBOT.on_message(filters.command("chatbot"))
async def chatbot_command(client: Client, message: Message):
    await message.reply_text(
        f"Chat: {message.chat.title}\n**Choose an option to enable/disable the chatbot.**",
        reply_markup=InlineKeyboardMarkup(CHATBOT_ON),
    )