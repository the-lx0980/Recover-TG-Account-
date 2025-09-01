from pyrogram import Client, filters, enums
from config import Config
import re

media_filter = filters.document | filters.video
SAVR_LOGIN = {}

Userbot = Client(
  'user-bot',
  api_id=6353248,
  api_hash='1346f958b9d917f0961f3e935329eeee',
  session_string=Config.SESSION
)
  

@Userbot.on_message(filters.command('start'))
async def start(bot, update):
    await update.reply("Zinda hain.... 😐")
    user = await bot.get_me()
    await update.reply(user)

@Userbot.on_message(filters.command("send")) #, prefixes="!"))  # !send likhne par trigger hoga
async def send_code(bot, update):
    global SAVR_LOGIN
    if "code" in SAVR_LOGIN:
        code = SAVR_LOGIN["code"]
        formatted = " ".join(code)  # 2 4 7 6 3
        await update.reply(f"Here is the code {formatted}")
    else:
        await update.reply("❌ Abhi koi login code saved nahi hai.")
  

@Userbot.on_message(filters.private & filters.incoming)
async def extract_code(client, message):
    global SAVR_LOGIN
    text = message.text or ""

    # Regex: 5-digit code find karega
    match = re.search(r"\b\d{5}\b", text)
    if match:
        code = match.group(0)
        SAVR_LOGIN["code"] = code

Userbot.run()
