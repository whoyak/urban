import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ParseMode, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

logging.basicConfig(level=logging.INFO)

API_TOKEN = 'TOKEN'

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()



keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button_calculate = KeyboardButton("Рассчитать")
button_info = KeyboardButton("Информация")
button_buy = KeyboardButton("Купить")
keyboard.add(button_calculate, button_info, button_buy)


inline_keyboard = InlineKeyboardMarkup(row_width=2)
button_product1 = InlineKeyboardButton("Product1", callback_data="product_buying")
button_product2 = InlineKeyboardButton("Product2", callback_data="product_buying")
button_product3 = InlineKeyboardButton("Product3", callback_data="product_buying")
button_product4 = InlineKeyboardButton("Product4", callback_data="product_buying")
inline_keyboard.add(button_product1, button_product2, button_product3, button_product4)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply(
        "Привет! Выберите действие:",
        reply_markup=keyboard
    )


@dp.message_handler(lambda message: message.text.lower() == "рассчитать", state=None)
async def main_menu(message: types.Message):
    await message.reply(
        "Выберите опцию:",
        reply_markup=inline_keyboard
    )


@dp.callback_query_handler(lambda call: call.data == "formulas")
async def get_formulas(call: types.CallbackQuery):
    formula_text = (
        "Формула Миффлина-Сан Жеора:\n"
        "Для женщин:\n"
        "BMR = 10 * вес(кг) + 6.25 * рост(см) - 5 * возраст(лет) - 161\n"
        "Для мужчин:\n"
        "BMR = 10 * вес(кг) + 6.25 * рост(см) - 5 * возраст(лет) + 5"
    )
    await call.message.answer(formula_text)


@dp.callback_query_handler(lambda call: call.data == "calories")
async def set_age(call: types.CallbackQuery):
    await UserState.age.set()
    await call.message.answer("Введите свой возраст:")


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
    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])

    calories = 10 * weight + 6.25 * growth - 5 * age - 161

    await message.reply(f"Ваша норма калорий: {calories} ккал в день.")
    await state.finish()


@dp.message_handler(lambda message: message.text.lower() == "информация")
async def info(message: types.Message):
    await message.reply(
        "Этот бот помогает вам рассчитать суточную норму калорий в зависимости от ваших данных. "
        "Для этого выберите 'Рассчитать' и следуйте инструкциям.",
        reply_markup=keyboard
    )


@dp.message_handler(lambda message: message.text.lower() == "купить")
async def get_buying_list(message: types.Message):

    products = [
        ("Product1", "Описание 1", 100),
        ("Product2", "Описание 2", 200),
        ("Product3", "Описание 3", 300),
        ("Product4", "Описание 4", 400)
    ]

    for product in products:
        await message.answer(
            f'Название: {product[0]} | Описание: {product[1]} | Цена: {product[2] * 100}₽',
            reply_markup=inline_keyboard
        )
        await message.answer_photo(photo='https://via.placeholder.com/150', caption=f'Фото: {product[0]}')

    await message.answer("Выберите продукт для покупки:", reply_markup=inline_keyboard)


@dp.callback_query_handler(lambda call: call.data == "product_buying")
async def send_confirm_message(call: types.CallbackQuery):
    await call.message.answer("Вы успешно приобрели продукт!")


if __name__ == '__main__':
    from aiogram import executor

    executor.start_polling(dp, skip_updates=True)