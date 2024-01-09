from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

chanel = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton("Muhiddin dev", url='https://t.me/muhiddindev'),
    ],
    [
        InlineKeyboardButton("✅ Tekshirish", callback_data='chanel'),
    ]
])

download_types = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('💫 Video', callback_data='video')
    ],
    [
        InlineKeyboardButton('⭐️ Video HD', callback_data='video_hd')
    ],
    [
        InlineKeyboardButton('🎧 Audio', callback_data='audio')
    ]
])