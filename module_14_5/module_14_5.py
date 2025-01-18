import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

from crud_functions import initiate_db, get_all_products, add_user, is_included, add_product

# Настройки логирования
logging.basicConfig(level=logging.INFO)

# Токен бота
API_TOKEN = 'ВАШ_API_ТОКЕН'

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


initiate_db()


if not get_all_products():
    test_products = [
        ("Продукт1", "Описание продукта 1", 100),
        ("Продукт2", "Описание продукта 2", 200),
        ("Продукт3", "Описание продукта 3", 300),
        ("Продукт4", "Описание продукта 4", 400),
    ]
    for product in test_products:
        add_product(*product)


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()



keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button_register = KeyboardButton("Регистрация")
button_buy = KeyboardButton("Купить")
keyboard.add(button_register, button_buy)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Привет! Выберите действие:", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text.lower() == "регистрация")
async def sing_up(message: types.Message):
    await RegistrationState.username.set()
    await message.reply("Введите имя пользователя (только латинский алфавит):")


@dp.message_handler(state=RegistrationState.username)
async def set_username(message: types.Message, state: FSMContext):
    username = message.text

    if is_included(username):
        await message.reply("Пользователь существует, введите другое имя:")
    else:
        await state.update_data(username=username)
        await RegistrationState.email.set()
        await message.reply("Введите свой email:")


@dp.message_handler(state=RegistrationState.email)
async def set_email(message: types.Message, state: FSMContext):

    email = message.text
    await state.update_data(email=email)
    await RegistrationState.age.set()
    await message.reply("Введите свой возраст:")


@dp.message_handler(state=RegistrationState.age)
async def set_age(message: types.Message, state: FSMContext):

    try:
        age = int(message.text)
        if age <= 0:
            raise ValueError

        data = await state.get_data()
        username = data['username']
        email = data['email']

        add_user(username, email, age)
        await message.reply(f"Регистрация завершена! Ваш баланс: 1000₽.")
        await state.finish()

    except ValueError:
        await message.reply("Возраст должен быть положительным числом. Попробуйте снова.")


@dp.message_handler(lambda message: message.text.lower() == "купить")
async def get_buying_list(message: types.Message):
    """Вывод списка продуктов из базы данных."""
    products = get_all_products()
    for product in products:
        await message.answer(f'Название: {product[1]} | Описание: {product[2]} | Цена: {product[3]}₽')

    await message.reply("Выберите продукт для покупки.")


if __name__ == '__main__':
    from aiogram import executor

    executor.start_polling(dp, skip_updates=True)
