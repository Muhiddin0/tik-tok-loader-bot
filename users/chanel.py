
from loader import app
from utils import texts, buttons
from pyrogram.handlers import CallbackQueryHandler
from pyrogram.types import Message
from pyrogram import filters


async def chanel_filter(_, __, query):
    return query.data == "chanel"

static_data_filter = filters.create(chanel_filter)

@app.on_callback_query(static_data_filter)
async def chanel(app, message:Message):
    
    user_id = message.from_user.id
    name = message.from_user.first_name

    try:
        await app.get_chat_member(chat_id="@muhiddindev", user_id=user_id)
    except:
        await app.send_message(
            chat_id=user_id,
            text=texts.not_member, 
            reply_markup=buttons.chanel
        )
        return
    
    await app.send_message(text=texts.start, chat_id=user_id)