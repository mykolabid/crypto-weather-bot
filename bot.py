import asyncio

from aiogram import Bot, Dispatcher
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config

from services.crypto import get_btc_price
from services.gold import get_gold_price
from services.weather import get_weather
from services.currency import get_usd_uah
from services.quotes import get_quote
bot = Bot(token=config.BOT_TOKEN)

dp = Dispatcher()


menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="📊 Bitcoin",
                callback_data="btc"
            )
        ],
        [
            InlineKeyboardButton(
                text="🥇 Gold",
                callback_data="gold"
            )
        ],
        [
            InlineKeyboardButton(
                text="🌦 Weather Wrocław",
                callback_data="weather"
            )
        ],
        [
            InlineKeyboardButton(
                text="💵 USD → UAH",
                callback_data="usd"
            )
        ],  # <- Здесь была пропущена закрывающая скобка рядов
        [
            InlineKeyboardButton(
                text="💡Шахи факти",
                callback_data="quote"
            )
        ]
    ]
)

@dp.message(Command("start"))
async def start(message: Message):

    await message.answer(
        "Привіт 👋\nОбери інформацію:",
        reply_markup=menu
    )


@dp.callback_query()
async def buttons(callback: CallbackQuery):


    if callback.data == "btc":

        price = get_btc_price()

        await callback.message.answer(
            f"📊 Bitcoin: {price}$",
            reply_markup=menu
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



    await callback.answer()



async def main():

    await dp.start_polling(bot)



if __name__ == "__main__":

    asyncio.run(main())