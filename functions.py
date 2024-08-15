import pandas as pd
from aiogram import types
from aiogram.types import ParseMode
import transformation as tf


async def odd_D192_monday(message: types.Message):
    # Загрузка файла Excel и извлечение нужных данных
    rasp = pd.read_excel(
        io='rasp.xlsx',  # Укажите путь к вашему файлу
        engine='openpyxl',
        usecols='EB:EE',  # Укажите нужные столбцы
        header=6,  # Укажите нужную строку заголовка
        nrows=11  # Укажите количество строк для чтения
    )
    # Генерация сообщения
    final_message_text = tf.generate_message(rasp)
    await message.answer(final_message_text, parse_mode=ParseMode.HTML)


async def odd_D192_tuesday(message: types.Message):
    # Загрузка файла Excel и извлечение нужных данных
    rasp = pd.read_excel(
        io='rasp.xlsx',  # Укажите путь к вашему файлу
        engine='openpyxl',
        usecols='EB:EE',  # Укажите нужные столбцы
        header=18,  # Укажите нужную строку заголовка
        nrows=11  # Укажите количество строк для чтения
    )
    # Генерация сообщения
    final_message_text = tf.generate_message(rasp)
    await message.answer(final_message_text, parse_mode=ParseMode.HTML)


async def odd_D192_wednesday(message: types.Message):
    # Загрузка файла Excel и извлечение нужных данных
    rasp = pd.read_excel(
        io='rasp.xlsx',  # Укажите путь к вашему файлу
        engine='openpyxl',
        usecols='EB:EE',  # Укажите нужные столбцы
        header=30,  # Укажите нужную строку заголовка
        nrows=11  # Укажите количество строк для чтения
    )
    # Генерация сообщения
    final_message_text = tf.generate_message(rasp)
    await message.answer(final_message_text, parse_mode=ParseMode.HTML)
