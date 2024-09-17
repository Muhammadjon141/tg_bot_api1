import requests
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor

# Telegram bot tokenini o'rnating
TELEGRAM_TOKEN = '7385548735:AAGF6oj1S65hDMoPqmCHI5fuMnbeKACekA8'

# Bot va Dispatcher ni yaratish
bot = Bot(token=TELEGRAM_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("""Salom! Bizning markaz botiga xush kelibsiz! Videolar haqida ma'lumot olish uchun 
                        /get_comments - Kurslar ro'yhati
                        /get_likes - O'qituvchilar ro'yhati
                        /get_posts - Talabalar ro'yhati
                        buyrug‘ini yuboring.""")

@dp.message_handler(commands=['get_courses'])
async def get_artists(message: types.Message):
    response = requests.get('http://127.0.0.1:8001/comment/comments')
    if response.status_code == 200:
        comments = response.json()
        if comments:
            for comment,i in zip(comments, range(1, (len(comments)+1))):
                comments_list = comment['content']
                await message.reply(f"Commentlar ro'yhati:\n{i}. {comments_list}")
        else:
            await message.reply("Commentlar topilmadi.")
    else:
        await message.reply("Commentlarni olishda xatolik yuz berdi.")


@dp.message_handler(commands=['get_likes'])
async def get_alboms(message: types.Message):
    response = requests.get('http://127.0.0.1:8001/likes/likes')
    if response.status_code == 200:
        likes = response.json()
        if likes:
            for like,i in zip(likes, range(1, (len(likes)+1))):
                likes_list = f"{like['user_id']} {like['post_id']}"
                await message.reply(f"Like kim tomonidan qo'yilgan id:\n{i}. {likes_list}")
        else:
            await message.reply("Likelar topilmadi.")
    else:
        await message.reply("Likelarni olishda xatolik yuz berdi.")

@dp.message_handler(commands=['get_posts'])
async def get_songs(message: types.Message):
    response = requests.get('http://127.0.0.1:8001/posts/posts')
    if response.status_code == 200:
        posts = response.json()
        if posts:
            for post,i in zip(posts, range(1, (len(posts)+1))):
                posts_list = f"{post['user_id']}"
                await message.reply(f"Postni egasining id:\n{i}. {posts_list}")
        else:
            await message.reply("postlar topilmadi.")
    else:
        await message.reply("Postlarni olishda xatolik yuz berdi.")


if name == 'main':
    executor.start_polling(dp, skip_updates=True)