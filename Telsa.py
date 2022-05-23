import os 
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup 
import tgcrypto
import io
from pyrogram.types import Message
from pyrogram import Client,filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


HB = Client(
    "MSG_DELETING Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

START_TEXT = """**
HI {}, 
I AM A SIMPLE 
TEXT TO FILE BOT 
JUST SENT YOUR CODE OR TEXT MESSAGE 
THEN I WILL CONVERT IT INTO FILE

MADE BY @TELSABOTS**"""

HELP_TEXT = """**
SENT ANY TEXT MESSAGE.......

THEN REPLY WITH ANY /COMMAND

eg :- /python

PRESS /LIST COMMAND TO KNOW ABOUT
CUREENTLY SUPPORTED EXTENSIONS

MADE BY @TELSABOTS**
"""

ABOUT_TEXT = """
 🤖<b>BOT :MEDIA INFO 🤖</b>

📢<b>CHANNEL :</b>@TELSA BOTS

🧑🏼‍💻DEV🧑🏼‍💻: @ALLUADDICT

"""

SOURCE_TEXT = """</b>PRESS SOURCE BUTTON FOR SOURCE 
AND WATCH TOTOURIAL VIDEO IF YOU WANT ANY HELP</b>"""

START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🤩SOURCE🤩', url='https://hbamal.blogspot.com/2021/08/how-to-make-your-own-discussion-unpin_4.html'),
        InlineKeyboardButton('💟TOTOURIAL💟', url='https://www.youtube.com/watch?v=sXTg5CB9dy8')
        ],[
        InlineKeyboardButton('🆘HELP🆘', callback_data='help'),
        InlineKeyboardButton('🤗ABOUT🤗', callback_data='about'),
        InlineKeyboardButton('🔐CLOSE🔐', callback_data='close')
        ]]
    )
HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('📢CHANNEL📢', url='https://telegram.me/TELSABOTS'),
        InlineKeyboardButton('🧑🏼‍💻DEV🧑🏼‍💻', url='https://telegram.me/alluaddict')
        ],[
        InlineKeyboardButton('🏡HOME🏡', callback_data='home'),
        InlineKeyboardButton('🤗ABOUT🤗', callback_data='about'),
        InlineKeyboardButton('🔐CLOSE🔐', callback_data='close')
        ]]
    )
ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('📢CHANNEL📢', url='https://telegram.me/TELSABOTS'),
        InlineKeyboardButton('🤩SOURCE🤩', url='https://youtu.be/sXTg5CB9dy8')
        ],[
        InlineKeyboardButton('🏡HOME🏡', callback_data='home'),
        InlineKeyboardButton('🆘HELP🆘', callback_data='help'),
        InlineKeyboardButton('🔐CLOSE🔐', callback_data='close')
        ]]
    )

SOURCE_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🤩SOURCE🤩', url='https://hbamal.blogspot.com/2021/08/how-to-make-your-own-discussion-unpin_4.html'),
        InlineKeyboardButton('💟TOTOURIAL💟', url='https://www.youtube.com/watch?v=sXTg5CB9dy8')
        ],[
        InlineKeyboardButton('🔐CLOSE 🔐', callback_data='close')
        ]]
    )

@HB.on_callback_query()
async def cb_data(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=START_TEXT.format(update.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP_TEXT,
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTONS
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT,
            disable_web_page_preview=True,
            reply_markup=ABOUT_BUTTONS
        )
    else:
        await update.message.delete()
    
@HB.on_message(filters.command(["start"]))
async def start(bot, update):
    text = START_TEXT.format(update.from_user.mention)
    reply_markup = START_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )
    
@HB.on_message(filters.command(["help"]))
async def help_message(bot, update):
    text = HELP_TEXT
    reply_markup = HELP_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )     
    
@HB.on_message(filters.command(["about"]))
async def about_message(bot, update):
    text = ABOUT_TEXT
    reply_markup = ABOUT_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )     
    
@HB.on_message(filters.command(["Source", "s"]))
async def Source_message(bot, update):
    text = SOURCE_TEXT
    reply_markup = SOURCE_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )     
result_buttons = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('📢CHANNEL📢', url='https://telegram.me/TELSABOTS'),
        InlineKeyboardButton('🧑🏼‍💻DEV🧑🏼‍💻', url='https://telegram.me/alluaddict')
        ],[
        InlineKeyboardButton('🔐CLOSE🔐', callback_data='close')
        ]]
    )

result_text = """**JOIN @TELSABOTS"""
@HB.on_message(filters.text & filters.command(["plain"]))
async def echo_document(client: Client, msg: Message):
    reply_markup = result_buttons
    file_obj = io.BytesIO(bytes(msg.text, "utf-8"))
    file_obj.name = "msg.txt"
    await client.send_document(msg.chat.id, file_obj, reply_markup=reply_markup, caption=result_text)

@HB.on_message(filters.text & filters.command(["YAML"]))
async def echo_document(client: Client, msg: Message):
    reply_markup = result_buttons
    file_obj = io.BytesIO(bytes(msg.text, "utf-8"))
    file_obj.name = "HB.yml"
    await client.send_document(msg.chat.id, file_obj, reply_markup=reply_markup, caption=result_text)

@HB.on_message(filters.text & filters.command(["swift"]))
async def echo_document(client: Client, msg: Message):
    reply_markup = result_buttons
    file_obj = io.BytesIO(bytes(msg.text, "utf-8"))
    file_obj.name = "HB.swift"
    await client.send_document(msg.chat.id, file_obj, reply_markup=reply_markup, caption=result_text)

@HB.on_message(filters.text & filters.command(["docker"]))
async def echo_document(client: Client, msg: Message):
    reply_markup = result_buttons
    file_obj = io.BytesIO(bytes(msg.text, "utf-8"))
    file_obj.name = "DOCKER.dockerfile"
    await client.send_document(msg.chat.id, file_obj, reply_markup=reply_markup, caption=result_text)

@HB.on_message(filters.text & filters.command(["python"]))
async def echo_document(client: Client, msg: Message):
    reply_markup = result_buttons
    file_obj = io.BytesIO(bytes(msg.text, "utf-8"))
    file_obj.name = "main.py"
    await client.send_document(msg.chat.id, file_obj, reply_markup=reply_markup, caption=result_text)

@HB.on_message(filters.text & filters.command(["sql"]))
async def echo_document(client: Client, msg: Message):
    reply_markup = result_buttons
    file_obj = io.BytesIO(bytes(msg.text, "utf-8"))
    file_obj.name = "MY.sql"
    await client.send_document(msg.chat.id, file_obj, reply_markup=reply_markup, caption=result_text)



@HB.on_message(filters.text & filters.command(["C"]))
async def echo_document(client: Client, msg: Message):
    reply_markup = result_buttons
    file_obj = io.BytesIO(bytes(msg.text, "utf-8"))
    file_obj.name = "main.c"
    await client.send_document(msg.chat.id, file_obj, reply_markup=reply_markup, caption=result_text)



@HB.on_message(filters.text & filters.command(["ruby"]))
async def echo_document(client: Client, msg: Message):
    reply_markup = result_buttons
    file_obj = io.BytesIO(bytes(msg.text, "utf-8"))
    file_obj.name = "RUBY.rb"
    await client.send_document(msg.chat.id, file_obj, reply_markup=reply_markup, caption=result_text)

@HB.on_message(filters.text & filters.command(["markdown"]))
async def echo_document(client: Client, msg: Message):
    reply_markup = result_buttons
    file_obj = io.BytesIO(bytes(msg.text, "utf-8"))
    file_obj.name = "README.md"
    await client.send_document(msg.chat.id, file_obj, reply_markup=reply_markup, caption=result_text)
    
@HB.on_message(filters.text & filters.command(["html"]))
async def echo_document(client: Client, msg: Message):
    reply_markup = result_buttons
    file_obj = io.BytesIO(bytes(msg.text, "utf-8"))
    file_obj.name = "index.html"
    await client.send_document(msg.chat.id, file_obj, reply_markup=reply_markup, caption=result_text)

@HB.on_message(filters.text & filters.command(["java"]))
async def echo_document(client: Client, msg: Message):
    reply_markup = result_buttons
    file_obj = io.BytesIO(bytes(msg.text, "utf-8"))
    file_obj.name = "app.java"
    await client.send_document(msg.chat.id, file_obj, reply_markup=reply_markup, caption=result_text)

@HB.on_message(filters.text & filters.command(["js"]))
async def echo_document(client: Client, msg: Message):
    reply_markup = result_buttons
    file_obj = io.BytesIO(bytes(msg.text, "utf-8"))
    file_obj.name = "script.js"
    await client.send_document(msg.chat.id, file_obj, reply_markup=reply_markup, caption=result_text)

@HB.on_message(filters.text & filters.command(["css"]))
async def echo_document(client: Client, msg: Message):
    reply_markup = result_buttons
    file_obj = io.BytesIO(bytes(msg.text, "utf-8"))
    file_obj.name = "style.css"
    await client.send_document(msg.chat.id, file_obj, reply_markup=reply_markup, caption=result_text)

@HB.on_message(filters.text & filters.command(["sass"]))
async def echo_document(client: Client, msg: Message):
    reply_markup = result_buttons
    file_obj = io.BytesIO(bytes(msg.text, "utf-8"))
    file_obj.name = "STYLE.scss"
    await client.send_document(msg.chat.id, file_obj, reply_markup=reply_markup, caption=result_text)

@HB.on_message(filters.text & filters.command(["perl"]))
async def echo_document(client: Client, msg: Message):
    reply_markup = result_buttons
    file_obj = io.BytesIO(bytes(msg.text, "utf-8"))
    file_obj.name = "file.perl"
    await client.send_document(msg.chat.id, file_obj, reply_markup=reply_markup, caption=result_text)
@HB.on_message(filters.text & filters.command(["xml"]))
async def echo_document(client: Client, msg: Message):
    file_obj = io.BytesIO(bytes(msg.text, "utf-8"))
    file_obj.name = "PROJECT.py"
    await client.send_document(msg.chat.id, file_obj, reply_markup=reply_markup, caption=result_text)


@HB.on_message(filters.text & filters.command(["kivy"]))
async def echo_document(client: Client, msg: Message):
    file_obj = io.BytesIO(bytes(msg.text, "utf-8"))
    file_obj.name = "thelab.kv"
    await client.send_document(msg.chat.id, file_obj, reply_markup=reply_markup, caption=result_text)


@HB.on_message(filters.text & filters.command(["php"]))
async def echo_document(client: Client, msg: Message):
    reply_markup = result_buttons
    file_obj = io.BytesIO(bytes(msg.text, "utf-8"))
    file_obj.name = "site.php"
    await client.send_document(msg.chat.id, file_obj, reply_markup=reply_markup, caption=result_text)




HB.run()
