from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode
from aiogram.types import Message
import asyncio

from config import get_token


dp: Dispatcher = Dispatcher()


@dp.message(CommandStart())
async def start_com(message: Message):
    await message.answer(
        "The bot has been launched. You can upload videos that are less than 6 minutes long"
    )


@dp.message()
async def echo(message: Message):
    await message.answer(message.text)


async def main() -> None:
    bot: Bot = Bot(get_token(), parse_mode=ParseMode.MARKDOWN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
