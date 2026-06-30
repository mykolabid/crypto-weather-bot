import asyncio

from aiogram import Bot, Dispatcher
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


from services.handel import get_handlowe
from services.crypto import get_price
from services.gold import get_gold_price
from services.weather import get_weather
from services.currency import get_usd_uah
from services.quotes import get_quote
import os
from dotenv import load_dotenv

load_dotenv()

bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()


menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="📊 Bitcoin, Еthereum",
                callback_data="btc"
            )
        ],
        [
            InlineKeyboardButton(
                text="🥇 Золото ціна",
                callback_data="gold"
            )
        ],
        [
            InlineKeyboardButton(
                text="🌦 Погода Вроцлав",
                callback_data="weather"
            )
        ],
        [
            InlineKeyboardButton(
                text="💵 USD → UAH",
                callback_data="usd"
            )
        ],
        [
            InlineKeyboardButton(
                text="💡Шахи факти",
                callback_data="quote"
            )
        ],
        [InlineKeyboardButton(
            text="🛒 Niedziela handlowa",
            callback_data="handel"
        )
        ],

        [InlineKeyboardButton(
            text="💬 Побажання",
            callback_data="wishes"
        )


        ]
    ]
)

class Wishes(StatesGroup):
    waiting = State()

@dp.message(Command("start"))
async def start(message: Message):

    await message.answer(
        "Привіт 👋\nОбери інформацію:",
        reply_markup=menu
    )

@dp.callback_query(lambda c: c.data == "wishes")
async def wishes_button(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(
        "💬 Напиши своє побажання для бота:"
    )
    await state.set_state(Wishes.waiting)
    await callback.answer()


@dp.callback_query()
async def buttons(callback: CallbackQuery):
    if callback.data == "btc":

        btc = get_price("bitcoin")
        eth = get_price("ethereum")

        await callback.message.answer(
            f"""
        ₿ Bitcoin: {btc}$

        Ξ Ethereum: {eth}$
        """
        )

    elif callback.data == "gold":

        price = get_gold_price()

        await callback.message.answer(
            f"🥇 Gold: {price}$",
            reply_markup=menu
        )


    elif callback.data == "weather":

        temp = get_weather()

        await callback.message.answer(
            f"🌦 Wrocław: {temp}°C",
            reply_markup=menu
        )


    elif callback.data == "usd":

        rate = get_usd_uah()

        await callback.message.answer(

            f"💵 1 USD = {rate} грн",
            reply_markup=menu

        )

    elif callback.data == "quote":

        quote = get_quote()

        await callback.message.answer(
            f"💡 {quote}",
            reply_markup=menu
        )
    elif callback.data == "handel":

        result = get_handlowe()

        await callback.message.answer(
            result,
            reply_markup=menu
        )

@dp.message(Wishes.waiting)
async def wishes_text(message: Message, state: FSMContext):

    text = message.text

    await message.answer(
        "✅ Дякую! Твоє побажання збережено."
    )


    await bot.send_message(
        898190826,
        f"""
💬 Нове побажання:

👤 {message.from_user.full_name}

📝 {text}
"""
    )

    await state.clear()

async def main():

    await dp.start_polling(bot)



if __name__ == "__main__":

    asyncio.run(main())