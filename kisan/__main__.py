import os
import logging
from os import getenv
from pyrogram import Client, filters, idle
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import ChatAdminRequired

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

# config vars
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER = os.getenv("OWNER")

# pyrogram client
app = Client(
            "banall",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
)

@app.on_message(
filters.command("start")
& filters.private            
)
async def start_command(client, message: Message):
  await message.reply_photo(
                            photo = f"https://telegra.ph/file/fff2ee6f504bc061cb7d3.jpg",
                            caption = f"ʜᴇʏ, ᴛʜɪs ɪs ᴀ sɪᴍᴘʟᴇ ʙᴀɴ ᴀʟʟ ʙᴏᴛ ᴡʜɪᴄʜ ɪs ʙᴀsᴇᴅ ᴏɴ ᴘʏʀᴏɢʀᴀᴍ ʟɪʙᴇʀᴀʀʏ ᴛᴏ ʙᴀɴ ᴏʀ ᴅᴇsᴛʀᴏʏ ᴀʟʟ ᴛʜᴇ ᴍᴇᴍʙᴇʀs ғʀᴏᴍ ᴀ ɢʀᴏᴜᴘ ᴡɪᴛʜ ɪɴ ᴀ ғᴇᴡ  sᴇᴄᴏɴᴅs!\n\nᴛᴏ ᴄʜᴇᴄᴋ ᴍʏ ᴀʙɪʟɪᴛʏ ɢɪʙ me ғᴜʟʟ ᴘᴏᴡᴇʀs\n\nᴛʏᴘᴇ /ʙᴀɴᴀʟʟ ᴛᴏ ꜱᴇᴇ ᴍᴀɢɪᴄ ɪɴ ɢʀᴏᴜᴘ.",
  reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᴏᴡɴᴇʀ", url=f"https://t.me/{OWNER}")
                ]       
           ]
      )
)

@app.on_message(
    filters.command("banall") 
    & (filters.group | filters.channel)
)
async def banall_command(client, message: Message):
    chat_id = message.chat.id
    if message.chat.type == "channel":
        async for member in app.iter_chat_members(chat_id):
            try:
                await app.kick_chat_member(chat_id, member.user.id)
                print("Kicked {} from channel {}".format(member.user.id, chat_id))
            except Exception as e:
                print("Failed to kick {} from channel {}: {}".format(member.user.id, chat_id, e))
        print("Ban all process completed for channel {}".format(chat_id))
    else:
        async for member in app.iter_chat_members(chat_id):
            try:
                await app.ban_chat_member(chat_id, member.user.id)
                print("Banned {} from group {}".format(member.user.id, chat_id))
            except Exception as e:
                print("Failed to ban {} from group {}: {}".format(member.user.id, chat_id, e))
        print("Ban all process completed for group {}".format(chat_id))
        
    

# start bot client
app.start()
print("Banall-Bot Booted Successfully")
idle()
