import os 
 
from aiogram import * 
from pytube import YouTube 
 
bot = Bot("TOKEN") 
dp = Dispatcher(bot) 
 
 
@dp.message_handler(commands=['start']) 
async def start_message(message: types.Message): 
 chat_id = message.chat.id 
 await bot.send_message(chat_id, "Привет! Я помогу скачать тебе видосы с YouTube)\n" 
         "Отправь мне ссылку на видео") 
 
 
@dp.message_handler() 
async def text_message(message:types.Message): 
 chat_id = message.chat.id 
 url = message.text 
 yt = YouTube(url) 
 if message.text.startswith == 'https://youtu.be/' or 'https://www.youtube.com/': 
  await bot.send_message(chat_id, f"*Подожди, видео уже загружаеться* : {yt.title}\n" 
          f"*C Канала *: {yt.author}", parse_mode="Markdown") 
  await download_youtube_video(url, message,bot) 
 
 
async def download_youtube_video(url, message,bot): 
 yt = YouTube(url) 
 stream = yt.streams.filter(progressivw=True, file_extension="mp4") 
 stream.get_highest_resolution().download(f'{message.chat.id}',  f'{message.chat.id}_{yt.title}') 
 with open(f"{message.chat.id}/{message.chat.id}_{yt.title}", 'rb') as video: 
  await bot.send_video(message.chat.id, video, caption="*Вот твоё видео *", parse_mode="Markdown") 
  os.remove(f"{message.chat.id}/{message.chat.id}_{yt.title}") 
 
 
 
async def download_youtube_video(url,message,bot): 
