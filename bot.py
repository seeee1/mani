import os
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

app = Client("edit_delete_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_edited_message(filters.group)
async def delete_edited(client: Client, message: Message):
    chat_id = message.chat.id
    user = await client.get_chat_member(chat_id, message.from_user.id)
    username = message.from_user.username or message.from_user.first_name

    if user.status in ["creator", "administrator"]:
        return

    await message.delete()
    await message.reply_text(f"🚨 المستخدم @{username}, لا يُسمح للأعضاء بتعديل الرسائل! 🛑")



@app.on_message(filters.command("start"))
def start(client, message):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🌐 القناه الرسميه", url="https://t.me/senzir2")],
        [InlineKeyboardButton("المطور 🧑‍💻", url="https://t.me/senzir1")]
    ])
    message.reply_text("اهلا وسهلا فيك ببوت سينزر لحماية الجروبات من التبنيد", reply_markup=keyboard)
    

print("✅ البوت يعمل...")
app.run()
