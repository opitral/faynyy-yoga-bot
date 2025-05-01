import asyncio

from aiogram import Router
from aiogram.enums import ChatAction
from aiogram.filters import CommandStart
from aiogram.types import Message, FSInputFile, CallbackQuery

from application.keyboards import START_KB, WantInGroupCbData, RETURN_TO_START_KB, BackToStartCbData, \
    WantIndividuallyCbData, WANT_INDIVIDUALLY_KB, StartPracticeCbData, SUBSCRIBE_KB, START_PRACTICE_KB

router = Router()


@router.message(CommandStart())
async def start_command_handler(message: Message):
    await message.answer_photo(FSInputFile("resources/start_photo.jpg"), caption="💩Тисни кнопку нижче та отримуй короткий стато-динамічний комплекс для активації опорно-рухового апарату та зняття блоків та затисків в тазу", show_caption_above_media=True, reply_markup=START_KB)
    # await message.answer("start_message<a href=\"https://ibb.co/JSQ5ncd\">a</a>", reply_markup=START_KB, parse_mode=ParseMode.HTML, disable_web_page_preview=False)

@router.callback_query(BackToStartCbData.filter())
async def back_to_start_callback_handler(callback: CallbackQuery):
    await callback.message.answer_photo(FSInputFile("resources/start_photo.jpg"), caption="start_message", show_caption_above_media=True, reply_markup=START_KB)
    await callback.answer()

@router.callback_query(WantInGroupCbData.filter())
async def want_in_group_callback_handler(callback: CallbackQuery):
    await callback.message.answer("🦾Набір в онлайн «міні-групу» по йозі \n⚡️Швидкий результат у полі вмотивованих лідерів\n📲Формат тренувань, де вся моя увага на ваших корекціях асан та техніці\n⚡️Всього 5 місць. Знайдемо для тебе - пиши @faynyy\nЩо ти отримаєш?👇🏻\n✔️Налагодиш ранкові підйоми без будильника \n✔️Звільнення від стресу та тривожності\n✔️Покращення сну\n✔️Позбавлення від болей в шиї, спині та попереку\n✔️Корекція фігури та схуднення\n✔️Підвищення концентрації уваги та памʼяті\n\nЦіна зараз  - 350 грн/заняття\n⤵️ абонемент\nна 8 занять: всього 2800 грн.", reply_markup=RETURN_TO_START_KB)
    await callback.answer()

@router.callback_query(WantIndividuallyCbData.filter())
async def want_individually_callback_handler(callback: CallbackQuery):
    await callback.message.answer("📲Заповніть анкету для глибокої трансформації (займає 1 хв)", reply_markup=WANT_INDIVIDUALLY_KB)
    await callback.answer()

@router.callback_query(StartPracticeCbData.filter())
async def start_practice_callback_handler(callback: CallbackQuery):
    await callback.message.answer("⚡️Підпишись на мене в inst щоб отримати здорове тіло та психіку за 30 хв вдома", reply_markup=SUBSCRIBE_KB)
    await callback.bot.send_chat_action(callback.message.chat.id, action=ChatAction.TYPING)
    await callback.answer()
    await asyncio.sleep(10)
    await callback.message.answer("🤝Після підписки повернись сюди й натисни кнопку нижче, щоб отримати відео")
    await callback.bot.send_chat_action(callback.message.chat.id, action=ChatAction.TYPING)
    await asyncio.sleep(10)
    await callback.message.answer("Полетіли🚀", reply_markup=START_PRACTICE_KB)

@router.message()
async def unknown_commands_handler(message: Message):
    await message.answer("Не знаю такої команди. Спробуй ще раз")
