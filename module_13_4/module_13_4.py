import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ParseMode
from aiogram.utils import executor
from aiogram.dispatcher.filters.state import State, StatesGroup  # Исправили импорт
from aiogram.dispatcher import FSMContext

logging.basicConfig(level=logging.INFO)

API_TOKEN = 'TOKEN'

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()  # Используем MemoryStorage для хранилища состояний
dp = Dispatcher(bot, storage=storage)

class UserState(StatesGroup):
    age = State()   # Для возраста
    growth = State()  # Для роста
    weight = State()  # Для веса

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Привет! Для начала напишите 'Calories', чтобы начать расчет нормы калорий.")

@dp.message_handler(lambda message: message.text.lower() == "calories", state=None)
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

    calories = 10 * weight + 6.25 * growth - 5 * age - 161

    await message.reply(f"Ваша норма калорий: {calories} ккал в день.")
    await state.finish()

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
