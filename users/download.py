
import requests
from loader import app
from utils import buttons, texts
from downloader import Loader
from pyrogram import filters
from pyrogram.types import Message
from pyrogram import Client
from pyrogram.types import InputMediaPhoto, InputMediaVideo

import asyncio

async def start_task(app:Client, message:Message):

    user_id = message.from_user.id
    url = message.text
    
    try:
        await app.get_chat_member(chat_id="@itkentuz", user_id=user_id)
    except:
        await app.send_message(
            chat_id=user_id,
            text=texts.not_member, 
            reply_markup=buttons.chanel
        )
        return

        
    loading_message:Message = await app.send_message(
        chat_id=user_id,
        text='⏳'
    )

    data = Loader.loading(url)

    if not data['status']: #error
        await loading_message.edit_text('⭕️ Xato TikTok linki')
        return
    

    if data['type'] == 'single':

        qualitys = ''
        for i in data['links']:
            qualitys += "<a href='{}'>{}</a> ".format(i['href'], i.text) 

        await app.send_photo(
            chat_id=user_id,
            photo=data['img'],
            caption=texts.single_caption.format(data['title'], qualitys),
            reply_markup=buttons.download_types
        )
    
    elif data['type'] == 'albom':
        
        mc = len(data['links']) // 6
        start = 0
        for i in range(mc):
            end = start + 6
            
            medias = []
            for c, a in enumerate(data['links'][start:end]):
                response = requests.get(a['src'])

                save_path = 'img_{}_{}_{}_{}.jpg'.format(user_id, message.id, i, c)
                with open(save_path, "wb") as file:
                    file.write(response.content)

                medias.append(InputMediaPhoto(save_path))

            await asyncio.sleep(2)
            await app.send_media_group(
                user_id,
                medias
            )
            start = end
    await app.delete_messages(
        chat_id=user_id,
        message_ids=loading_message.id
    )


@app.on_message(filters.text)
async def download(client, message):
    asyncio.create_task(start_task(client, message))