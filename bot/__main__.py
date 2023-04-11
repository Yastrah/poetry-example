import logging
import os
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, executor, types

load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
PROXY_URL = "http://proxy.server:3128"
bot = Bot(token=os.getenv('TOKEN'), proxy=PROXY_URL)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    with open("data/file.txt", 'r') as file:
        data = file.read().strip()
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply(f"Hi!\nI'm EchoBot!\n{data}.")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
