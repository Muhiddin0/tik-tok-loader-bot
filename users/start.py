
from loader import app
from pyrogram import filters
from pyrogram.types import Message

from data.model import Model
from utils import buttons, texts


import asyncio

async def start_task(app, message:Message):

    user_id = message.from_user.id
    name = message.from_user.first_name

    Model().addUser(user_id)

    try:
        await app.get_chat_member(chat_id="@muhiddindev", user_id=user_id)
    except:
        await app.send_message(
            chat_id=user_id,
            text=texts.chanel.format(name),
            reply_markup=buttons.chanel
        )
        return
    await app.send_message(text=texts.start, chat_id=user_id)

@app.on_message(filters.command(['start', 'help']))
async def send_welcome(client, message):
    asyncio.create_task(start_task(client, message))