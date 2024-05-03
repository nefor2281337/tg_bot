from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message 
import config_data

bot_config = config_data.load_config()


bot = Bot(token=bot_config.tg_bot.token)
dp = Dispatcher()


print(bot_config.tg_bot.admin_ids)  
