import asyncio
import logging

from aiogram import Router, F
from aiogram.enums import ChatAction, ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile, CallbackQuery

from application.database import UserDatabase
from application.keyboards import START_KB, WantInGroupCbData, RETURN_TO_START_KB, BackToStartCbData, \
    WantIndividuallyCbData, WANT_INDIVIDUALLY_KB, StartPracticeCbData, SUBSCRIBE_KB, START_PRACTICE_KB, REMEMBER_KB
from application.settings import settings

router = Router()


@router.message(CommandStart())
async def start_command_handler(message: Message, db: UserDatabase):
    if not db.get_user(message.from_user.id):
        db.add_user(
            telegram_id=message.from_user.id,
            first_name=message.from_user.first_name,
            last_name=message.from_user.last_name,
            username=message.from_user.username
        )
        logging.info("New user added: %s", message.from_user.id)
    await message.answer_photo(FSInputFile("resources/media/start_photo.jpg"), caption="⚡️Тисни кнопку нижче та отримуй короткий стато-динамічний комплекс для активації опорно-рухового апарату та зняття блоків та затисків в тазу", show_caption_above_media=True, reply_markup=START_KB)

@router.callback_query(BackToStartCbData.filter())
async def back_to_start_callback_handler(callback: CallbackQuery):
    await callback.message.answer_photo(FSInputFile("resources/media/start_photo.jpg"), caption="⚡️Тисни кнопку нижче та отримуй короткий стато-динамічний комплекс для активації опорно-рухового апарату та зняття блоків та затисків в тазу", show_caption_above_media=True, reply_markup=START_KB)
    await callback.answer()

@router.callback_query(WantInGroupCbData.filter())
async def want_in_group_callback_handler(callback: CallbackQuery, db: UserDatabase):
    user = db.get_user(callback.from_user.id)
    if not user["wants_group"]:
        db.update_user_field(callback.from_user.id, "wants_group", 1)
    await callback.message.answer("🦾*Набір в онлайн «міні-групу» по йозі*\n\n⚡️*Швидкий результат у полі вмотивованих лідерів*\n📲*Формат тренувань, де вся моя увага на ваших корекціях асан та техніці*\n⚡️*Всього 5 місць. Знайдемо для тебе - пиши @faynyy*\n\nЩо ти отримаєш?👇🏻\n✔️Налагодиш ранкові підйоми без будильника \n✔️Звільнення від стресу та тривожності\n✔️Покращення сну\n✔️Позбавлення від болей в шиї, спині та попереку\n✔️Корекція фігури та схуднення \n✔️Підвищення концентрації уваги та памʼяті\n\n*Ціна зараз  - 350 грн/заняття*\n⤵️ Місячний абонемент\n*на 8 занять: всього 2800 грн.*", reply_markup=RETURN_TO_START_KB, parse_mode=ParseMode.MARKDOWN)
    await callback.answer()

@router.callback_query(WantIndividuallyCbData.filter())
async def want_individually_callback_handler(callback: CallbackQuery, db: UserDatabase):
    user = db.get_user(callback.from_user.id)
    if not user["wants_individually"]:
        db.update_user_field(callback.from_user.id, "wants_individually", 1)
    await callback.message.answer("📲Заповніть анкету для глибокої трансформації (займає 1 хв)", reply_markup=WANT_INDIVIDUALLY_KB)
    await callback.answer()

@router.callback_query(StartPracticeCbData.filter())
async def start_practice_callback_handler(callback: CallbackQuery, db: UserDatabase):
    user = db.get_user(callback.from_user.id)
    await callback.answer()
    if not user["started_practice"]:
        await callback.message.answer("⚡️Підпишись на мене в inst щоб отримати здорове тіло та психіку за 30 хв вдома",
                                      reply_markup=SUBSCRIBE_KB)
        await callback.bot.send_chat_action(callback.message.chat.id, action=ChatAction.TYPING)
        await asyncio.sleep(10)
        await callback.message.answer("🤝Після підписки повернись сюди й натисни кнопку нижче, щоб отримати відео")
        await callback.bot.send_chat_action(callback.message.chat.id, action=ChatAction.TYPING)
        await asyncio.sleep(10)
        db.update_user_field(callback.from_user.id, "started_practice", 1)

    await callback.message.answer("Полетіли🚀", reply_markup=START_PRACTICE_KB)

    async def delayed_message():
        await asyncio.sleep(1800)
        await callback.message.answer("<i>Я супроводжуватиму тебе цього місяця, слідкуй за сповіщеннями, які мотивують до практики⚡️</i>\n\nХочеш розширити свої можливості, заспокоїти психіку та отримати здорове тіло👇🏻", parse_mode=ParseMode.HTML, reply_markup=REMEMBER_KB)

    asyncio.create_task(delayed_message())


@router.message(Command("export"), F.from_user.id.in_(settings.ADMINS_TELEGRAM_ID))
async def export_command_handler(message: Message, db: UserDatabase):
    await message.answer("Експортую базу користувачів у xlsx...")
    file_path = db.export_to_xlsx()
    logging.info("Exported user database to %s", file_path)
    await message.answer_document(FSInputFile(file_path), caption="База користувачів")


@router.message()
async def unknown_commands_handler(message: Message):
    await message.answer("Не знаю такої команди. Спробуй ще раз")
