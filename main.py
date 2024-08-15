from aiogram import Bot, Dispatcher, types
import logging
import functions
import asyncio


logging.basicConfig(level=logging.INFO)
TOKEN = '7474508608:AAFlexXt3-wKR-9qdZV6y8IRHLe76dcH3Jo'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer("Привет! Я бот для удобного просматривания расписания для Северского Промышленного колледжа. Для того чтобы узнать расписание напиши неделюю, группу, день. Пример 'Нечётная Д192 Понедельник' ")


async def main():
    # Регистрируем обработчики для каждого дня недели
    dp.register_message_handler(functions.odd_D192_monday, text=["Нечётная Д192 понедельник"])
    dp.register_message_handler(functions.odd_D192_tuesday, text=["Нечётная Д192 вторник"])
    dp.register_message_handler(functions.odd_D192_wednesday, text=["Нечётная Д192 среда"])
    await dp.start_polling()

if __name__ == "__main__":
    asyncio.run(main())
