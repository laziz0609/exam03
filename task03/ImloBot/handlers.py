from .ImageService import ImageService

from aiogram import types, Router, F
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import Command
from aiogram.exceptions import TelegramBadRequest

router = Router()
image_service = ImageService()


animals_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🐱 Cat", callback_data="cat")],
        [InlineKeyboardButton(text="🐕 Dog", callback_data="dog")],
        [InlineKeyboardButton(text="🦊 Fox", callback_data="fox")],
    ]
)


@router.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "🖼 <b>Hayvonlar rasmlari boti</b>\n\n"
        "Kerakli hayvonni tanlang:",
        reply_markup=animals_keyboard,
        parse_mode="HTML"
    )


@router.callback_query(F.data.in_(["cat", "dog", "fox"]))
async def handle_animal_button(callback: types.CallbackQuery):    
    animal = callback.data
    while True:

        image_url = await image_service.fetch_random_image(animal)

        if not image_url:
            await callback.message.answer("❌ Serverda xatolik")
            return

    
        if  image_url.lower().endswith("jpg") or  image_url.lower().endswith("png"):
            await callback.message.answer_photo(
                photo=image_url,
            )
            await callback.message.answer(
                "Kerakli hayvonni tanlang:",
                reply_markup=animals_keyboard,
                parse_mode="HTML"
            )
            return
        
        else:
            continue


@router.message(Command("cat", "dog", "fox"))
async def animal_command(message: types.Message):    
    animal = message.text.replace("/", "")
    while True:

        image_url = await image_service.fetch_random_image(animal)

        if not image_url:
            await message.answer("❌ Serverda xatolik")
            return

    
        if  image_url.lower().endswith("jpg") or  image_url.lower().endswith("png"):
            await message.answer_photo(
                photo=image_url,
            )
            await message.answer(
                "Kerakli hayvonni tanlang:",
                reply_markup=animals_keyboard,
                parse_mode="HTML"
            )
            return
        
        else:
            continue
         