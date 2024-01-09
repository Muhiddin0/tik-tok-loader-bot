
import asyncio
import os

import requests
from loader import app
from utils import texts, buttons
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram .enums import MessageEntityType
from pyrogram import Client

async def send(app:Client, message:Message):
    user_id = message.from_user.id

    try:
        await app.get_chat_member(chat_id="@itkentuz", user_id=user_id)
    except:
        await app.send_message(
            chat_id=user_id,
            text=texts.not_member, 
            reply_markup=buttons.chanel
        )
        return
    
    cnt = message.message.caption_entities
    data = [i.url for i in cnt if i.type == MessageEntityType.TEXT_LINK]
    
    if message.data == 'video':
        url = data[0]
    elif message.data == 'video_hd':
        url = data[1]
    elif message.data == 'audio':
        url = data[2]

    await app.edit_message_reply_markup(
        chat_id=user_id,
        message_id=message.message.id,
        reply_markup=None
    )

    await app.edit_message_caption(
        user_id,
        message.message.id,
        f"Laoding: start..."
    )

    response = requests.get(url=url)
    
    print(response.headers)

    resoponse_type = response.headers.get('Content-Type')
    if resoponse_type == 'text/plain; charset=utf-8':
        await app.delete_messages(user_id, message.message.id)
        await app.send_message(
            user_id,
            text=texts.timebad_url
        )
        return 
    
    if resoponse_type == 'video/mp4':
        save_path = 'vd_{}_{}.{}'.format(user_id, message.message.id, 'mp4')
    else:
        save_path = 'vd_{}_{}.{}'.format(user_id, message.message.id, 'mp3')
        

    with open(save_path, 'wb') as file:
        file.write(response.content)
    
    async def progress(current, total):
            
        await app.edit_message_caption(
            user_id,
            message.message.id,
            f"Laoding: {current * 100 / total:.1f}%"
        )
        
    await app.send_video(
        chat_id=user_id,
        video=save_path,
        caption=texts.succesfuly_download,
        progress=progress
    )

    await app.delete_messages(user_id, message.message.id)

    os.remove(save_path)

@app.on_callback_query()
async def send_task(app, message):
    asyncio.create_task(send(app, message))
    