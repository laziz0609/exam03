from .ImageService import ImageService

from aiogram import types, Router, F
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import Command
from aiogram.exceptions import TelegramBadRequest

router = Router()
image_service = ImageService()

# Qo'llab-quvvatlanadigan formatlar
SUPPORTED_FORMATS = (".jpg", ".jpeg", ".png", ".gif", ".webp")

animals_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🐱 Cat", callback_data="cat")],
        [InlineKeyboardButton(text="🐕 Dog", callback_data="dog")],
        [InlineKeyboardButton(text="🦊 Fox", callback_data="fox")],
        [InlineKeyboardButton(text="🔄 Yana tanlash", callback_data="restart")]
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


@router.callback_query(F.data == "restart")
async def restart(callback: types.CallbackQuery):
    """Qaytadan tanlash"""
    await callback.message.edit_text(
        "🖼 <b>Hayvonlar rasmlari boti</b>\n\n"
        "Kerakli hayvonni tanlang:",
        reply_markup=animals_keyboard,
        parse_mode="HTML"
    )
    await callback.answer()


@router.callback_query(F.data.in_(["cat", "dog", "fox"]))
async def handle_animal_button(callback: types.CallbackQuery):
    """Tugma bosilganda rasm yuborish"""
    
    animal = callback.data
    
    # Loading animatsiyasi
    await callback.answer(f"🔍 {animal.capitalize()} rasmi yuklanmoqda...", show_alert=False)
    
    # Xabar yuborish
    loading_msg = await callback.message.answer(f"⏳ Yuklanmoqda...")
    
    try:
        # API dan rasm URL ni olish
        image_url = await image_service.fetch_random_image(animal)
        
        if not image_url:
            await loading_msg.edit_text(
                "❌ Serverda xatolik yuz berdi\n\n"
                "Iltimos, qayta urinib ko'ring",
                reply_markup=animals_keyboard
            )
            return
        
        # URL formatini tekshirish
        is_valid_format = any(
            image_url.lower().endswith(fmt) 
            for fmt in SUPPORTED_FORMATS
        )
        
        if not is_valid_format:
            await loading_msg.edit_text(
                f"❌ Noto'g'ri rasm formati: {image_url}\n\n"
                f"Qo'llab-quvvatlanadigan: {', '.join(SUPPORTED_FORMATS)}",
                reply_markup=animals_keyboard
            )
            return
        
        # Loading xabarini o'chirish
        await loading_msg.delete()
        
        # Rasmni yuborish
        await callback.message.answer_photo(
            photo=image_url,
            caption=f"🎉 {animal.capitalize()} rasmi!\n\n"
                    f"Yana rasm olish uchun tugmani bosing 👇",
            reply_markup=animals_keyboard
        )
        
    except TelegramBadRequest as e:
        # Telegram rasm yuborishni rad etdi
        await loading_msg.edit_text(
            f"❌ Telegram xatosi: {str(e)}\n\n"
            "Bu rasm yuborib bo'lmaydi",
            reply_markup=animals_keyboard
        )
        
    except Exception as e:
        # Boshqa xatoliklar
        await loading_msg.edit_text(
            f"❌ Kutilmagan xatolik: {str(e)}",
            reply_markup=animals_keyboard
        )


@router.message(Command("cat", "dog", "fox"))
async def animal_command(message: types.Message):
    """Buyruq orqali rasm olish"""
    
    animal = message.text.replace("/", "")
    await message.answer(f"🔍 {animal.capitalize()} rasmi yuklanmoqda...")
    
    try:
        image_url = await image_service.fetch_random_image(animal)
        
        if not image_url:
            await message.answer("❌ Serverda xatolik")
            return
        
        # Format tekshirish
        is_valid = any(image_url.lower().endswith(fmt) for fmt in SUPPORTED_FORMATS)
        
        if not is_valid:
            await message.answer("❌ Noto'g'ri rasm formati")
            return
        
        await message.answer_photo(
            photo=image_url,
            caption=f"🎉 {animal.capitalize()} rasmi!"
        )
        
    except Exception as e:
        await message.answer(f"❌ Xatolik: {str(e)}")