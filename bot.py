import asyncio
import logging
import os
from datetime import datetime

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.client.default import DefaultBotProperties

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_CHAT_ID = int(os.getenv("ADMIN_CHAT_ID"))

bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode="HTML")
)

dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "👋 <b>Добро пожаловать в Ящик Доверия!</b>\n\n"
        "Здесь ты можешь анонимно отправить:\n"
        "жалобу, предложение, вопрос или любое сообщение."
    )

@dp.message()
async def handle_message(message: types.Message):
    if message.chat.type != "private":
        return

    now = datetime.now().strftime("%d.%m.%Y в %H:%M:%S")

    await bot.send_message(
        ADMIN_CHAT_ID,
        f"🔔 <b>Новое обращение</b>\n\n"
        f"Время: <b>{now}</b>\n\n"
        f"<b>Текст:</b>\n{message.text}"
    )

    await message.answer("✅ <b>Сообщение отправлено анонимно!</b>\nСпасибо за доверие.")

async def main():
    logging.basicConfig(level=logging.INFO)
    print("🚀 Ящик Доверия запущен на Koyeb!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
