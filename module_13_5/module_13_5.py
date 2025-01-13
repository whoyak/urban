import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ParseMode, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

logging.basicConfig(level=logging.INFO)

API_TOKEN = '6778452587:AAFYxjiVINBwwxlJYaeYDlSTbwbK36Znd64'

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()  # Используем MemoryStorage для хранилища состояний
dp = Dispatcher(bot, storage=storage)

class UserState(StatesGroup):
    age = State()   # Для возраста
    growth = State()  # Для роста
    weight = State()  # Для веса

# Создание клавиатуры
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button_calculate = KeyboardButton("Рассчитать")
button_info = KeyboardButton("Информация")
keyboard.add(button_calculate, button_info)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply(
        "Привет! Выберите действие:",
        reply_markup=keyboard  # Отправка клавиатуры при старте
    )

@dp.message_handler(lambda message: message.text.lower() == "рассчитать", state=None)
async def set_age(message: types.Message):
    await UserState.age.set()
    await message.reply("Введите свой возраст:")

@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await UserState.growth.set()
    await message.reply("Введите свой рост:")

@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await UserState.weight.set()
    await message.reply("Введите свой вес:")

@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()

    # Простой расчет калорий (можно заменить на более сложную формулу)
    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])

    # Формула для женщин (можно заменить на вашу логику)
    calories = 10 * weight + 6.25 * growth - 5 * age - 161

    await message.reply(f"Ваша норма калорий: {calories} ккал в день.")
    await state.finish()  # Завершаем процесс

@dp.message_handler(lambda message: message.text.lower() == "информация")
async def info(message: types.Message):
    await message.reply(
        "Этот бот помогает вам рассчитать суточную норму калорий в зависимости от ваших данных. "
        "Для этого выберите 'Рассчитать' и следуйте инструкциям.",
        reply_markup=keyboard  # Отправка клавиатуры с кнопками
    )

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
