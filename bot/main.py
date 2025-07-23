from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
import asyncio
from config import BotToken

bot = Bot(token=BotToken)
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name}!")


async def main():
    import datetime

    print(f"Бот запущен в {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
