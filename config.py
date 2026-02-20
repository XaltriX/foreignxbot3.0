# Don't Remove Credit @CodeFlix_Bots, @rohit_1888
# Ask Doubt on telegram @CodeflixSupport
#
# Copyright (C) 2025 by Codeflix-Bots@Github, < https://github.com/Codeflix-Bots >.
#
# This file is part of < https://github.com/Codeflix-Bots/FileStore > project,
# and is released under the MIT License.
# Please see < https://github.com/Codeflix-Bots/FileStore/blob/master/LICENSE >
#
# All rights reserved.
#

import os
from os import environ,getenv
import logging
from logging.handlers import RotatingFileHandler

#rohit_1888 on Tg
#--------------------------------------------
#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "8154426339:")
APP_ID = int(os.environ.get("APP_ID", "24955235")) #Your API ID from my.telegram.org
API_HASH = os.environ.get("API_HASH", "f317b3f7bbe390346d8b46868cff0de8") #Your API Hash from my.telegram.org
#--------------------------------------------

CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1003526493094")) #Your db channel Id
OWNER = os.environ.get("OWNER", "NeonGhost") # Owner username without @
OWNER_ID = int(os.environ.get("OWNER_ID", "5706788169")) # Owner id
#--------------------------------------------
PORT = os.environ.get("PORT", "8001")
#--------------------------------------------
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://RupsaRoy:ram123@cluster0.msvefse.mongodb.net/?appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "foreignxbohdht")
#--------------------------------------------
FSUB_LINK_EXPIRY = int(os.getenv("FSUB_LINK_EXPIRY", "10"))  # 0 means no expiry
BAN_SUPPORT = os.environ.get("BAN_SUPPORT", "https://t.me/NGSupportGroup")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "200"))
#--------------------------------------------
START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/ec17880d61180d3312d6a.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://telegra.ph/file/e292b12890b8b4b9dcbd1.jpg")

#--------------------------------------------
SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "arolinks.com")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "8a59f7197cfbac8f2fde46f209a9e8fc6504cb0b")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 64800)) # Add time in seconds
TUT_VID = os.environ.get("TUT_VID","https://t.me/HTODLINKZ/13")

#--------------------------------------------

#--------------------------------------------
HELP_TXT = (
    "<b><blockquote>"
    "📦 𝙁𝙞𝙡𝙚 → 𝙇𝙞𝙣𝙠 𝘽𝙤𝙩\n"
    "🤝 𝙒𝙤𝙧𝙠𝙨 𝙁𝙤𝙧 <b>@Linkz_Wallah</b>\n\n"
    "❏ 𝘾𝙤𝙢𝙢𝙖𝙣𝙙\n"
    "├ /start ➜ 𝙎𝙩𝙖𝙧𝙩 𝘽𝙤𝙩\n\n"
    "📌 𝙐𝙨𝙚:\n"
    "➤ 𝘾𝙡𝙞𝙘𝙠 𝙇𝙞𝙣𝙠 → 𝙎𝙩𝙖𝙧𝙩 𝘽𝙤𝙩\n"
    "➤ 𝙅𝙤𝙞𝙣 𝘾𝙝𝙖𝙣𝙣𝙚𝙡𝙨 → 𝙏𝙧𝙮 𝘼𝙜𝙖𝙞𝙣 ⚡\n\n"
    "👨‍💻 𝘽𝙮 <a href='https://t.me/NeonGhost'><b>NeonGhost</b></a>"
    "</blockquote></b>"
)
ABOUT_TXT = """
<b><blockquote>
✨ <b>ᴄʀᴇᴀᴛᴏʀ:</b> <a href='https://t.me/NeonGhost'>NeonGhost</a>
🌐 <b>ꜰᴏᴜɴᴅᴇʀ ᴏꜰ:</b> <a href='https://t.me/NeonGhost_Network'>NeonGhost Network</a>

🎥 <b>Free Videos ᴄʜᴀɴɴᴇʟ:</b> <a href='https://t.me/+l-xqPJba7KMyOTg1'>Lust Diaries 2.0</a>
🍿 <b>Movie Search ɢʀᴏᴜᴘ:</b> <a href='https://t.me/+DU6yY8lZ45dlOTc0'>NEW MOVIE REQUEST GROUP</a>
📱 <b>Paid Apps & MOD APK:</b> <a href=' https://t.me/+w3r7mmOPmK01ZmU1'>Paid Apps & MOD APK</a>

💻 <b>ᴅᴇᴠᴇʟᴏᴘᴇʀ:</b> <a href='https://t.me/NeonGhost'>NeonGhost</a>
</blockquote></b>
"""#--------------------------------------------
#--------------------------------------------
START_MSG = os.environ.get(
    "START_MESSAGE",
    "<b>ʜᴇʟʟᴏ {mention} ✨\n\n"
    "<blockquote>"
    "📦 ɪ ᴀᴍ ᴀ ꜰɪʟᴇ ꜱᴛᴏʀᴇ ʙᴏᴛ.\n"
    "🔐 ɪ ꜱᴛᴏʀᴇ ᴘʀɪᴠᴀᴛᴇ ꜰɪʟᴇꜱ ɪɴ ꜱᴘᴇᴄɪꜰɪᴇᴅ ᴄʜᴀɴɴᴇʟꜱ\n"
    "🔗 ᴀɴᴅ ᴀʟʟᴏᴡ ᴀᴄᴄᴇꜱꜱ ᴠɪᴀ ꜱᴇᴄᴜʀᴇ ꜱᴘᴇᴄɪᴀʟ ʟɪɴᴋꜱ.\n\n"
    "🤝 ᴡᴏʀᴋꜱ ꜰᴏʀ <b>@Linkz_Wallah</b>\n"
    "⚡ ᴘᴏᴡᴇʀᴇᴅ ʙʏ <b>@Neonghost_Network</b>"
    "</blockquote></b>"
)
FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "ʜᴇʟʟᴏ {mention} ✨\n\n"
    "<b><blockquote>"
    "🔔 ᴘʟᴇᴀꜱᴇ ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟꜱ ꜰɪʀꜱᴛ.\n"
    "📥 ᴀꜰᴛᴇʀ ᴊᴏɪɴɪɴɢ, ᴄʟɪᴄᴋ ᴛʜᴇ <u>ʀᴇʟᴏᴀᴅ</u> ʙᴜᴛᴛᴏɴ\n"
    "⚡ ᴛᴏ ᴜɴʟᴏᴄᴋ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛᴇᴅ ꜰɪʟᴇ."
    "</blockquote></b>"
)
CMD_TXT = """<blockquote><b>» ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅs:</b></blockquote>

<b>›› /dlt_time :</b> sᴇᴛ ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ ᴛɪᴍᴇ
<b>›› /check_dlt_time :</b> ᴄʜᴇᴄᴋ ᴄᴜʀʀᴇɴᴛ ᴅᴇʟᴇᴛᴇ ᴛɪᴍᴇ
<b>›› /dbroadcast :</b> ʙʀᴏᴀᴅᴄᴀsᴛ ᴅᴏᴄᴜᴍᴇɴᴛ / ᴠɪᴅᴇᴏ
<b>›› /ban :</b> ʙᴀɴ ᴀ ᴜꜱᴇʀ
<b>›› /unban :</b> ᴜɴʙᴀɴ ᴀ ᴜꜱᴇʀ
<b>›› /banlist :</b> ɢᴇᴛ ʟɪsᴛ ᴏꜰ ʙᴀɴɴᴇᴅ ᴜꜱᴇʀs
<b>›› /addchnl :</b> ᴀᴅᴅ ꜰᴏʀᴄᴇ sᴜʙ ᴄʜᴀɴɴᴇʟ
<b>›› /delchnl :</b> ʀᴇᴍᴏᴠᴇ ꜰᴏʀᴄᴇ sᴜʙ ᴄʜᴀɴɴᴇʟ
<b>›› /listchnl :</b> ᴠɪᴇᴡ ᴀᴅᴅᴇᴅ ᴄʜᴀɴɴᴇʟs
<b>›› /fsub_mode :</b> ᴛᴏɢɢʟᴇ ꜰᴏʀᴄᴇ sᴜʙ ᴍᴏᴅᴇ
<b>›› /pbroadcast :</b> sᴇɴᴅ ᴘʜᴏᴛᴏ ᴛᴏ ᴀʟʟ ᴜꜱᴇʀs
<b>›› /add_admin :</b> ᴀᴅᴅ ᴀɴ ᴀᴅᴍɪɴ
<b>›› /deladmin :</b> ʀᴇᴍᴏᴠᴇ ᴀɴ ᴀᴅᴍɪɴ
<b>›› /admins :</b> ɢᴇᴛ ʟɪsᴛ ᴏꜰ ᴀᴅᴍɪɴs
<b>›› /addpremium :</b> ᴀᴅᴅ ᴀ ᴘʀᴇᴍɪᴜᴍ ᴜꜱᴇʀ
<b>›› /premium_users :</b> ʟɪsᴛ ᴀʟʟ ᴘʀᴇᴍɪᴜᴍ ᴜꜱᴇʀs
<b>›› /remove_premium :</b> ʀᴇᴍᴏᴠᴇ ᴘʀᴇᴍɪᴜᴍ ꜰʀᴏᴍ ᴀ ᴜꜱᴇʀ
<b>›› /myplan :</b> ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴘʀᴇᴍɪᴜᴍ sᴛᴀᴛᴜs
<b>›› /count :</b> ᴄᴏᴜɴᴛ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴs
<b>›› /delreq :</b> Rᴇᴍᴏᴠᴇᴅ ʟᴇғᴛᴏᴠᴇʀ ɴᴏɴ-ʀᴇǫᴜᴇsᴛ ᴜsᴇʀs
"""
#--------------------------------------------
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>• ʙʏ @Linkz_Wallah</b>") #set your Custom Caption here, Keep None for Disable Custom Caption
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False #set True if you want to prevent users from forwarding files from bot
#--------------------------------------------
#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'
#--------------------------------------------
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!"

#==========================(BUY PREMIUM)====================#

OWNER_TAG = os.environ.get("OWNER_TAG", "NeonGhost")
UPI_ID = os.environ.get("UPI_ID", "kunaljaisinghpur@axl")
QR_PIC = os.environ.get("QR_PIC", "https://graph.org/file/4b8cf54757ba84a23f000-880a704ce5057adffa.jpg")
SCREENSHOT_URL = os.environ.get("SCREENSHOT_URL", f"t.me/NGPremiumXBot")
#--------------------------------------------

# ─── PREMIUM SUBSCRIPTION PRICES ─── #

# 7 Days (Trial – High Price)
PRICE1 = os.environ.get("PRICE1", "₹39")

# 1 Month (Basic)
PRICE2 = os.environ.get("PRICE2", "₹99")

# 3 Months (Value Pack)
PRICE3 = os.environ.get("PRICE3", "₹199")

# 6 Months (MOST POPULAR)
PRICE4 = os.environ.get("PRICE4", "₹299")

# 1 Year (BEST DEAL)
PRICE5 = os.environ.get("PRICE5", "₹399")


#===================(END)========================#

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   
