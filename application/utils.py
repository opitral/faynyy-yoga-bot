import logging

from aiogram import Bot
from aiogram.enums import ParseMode
from aiogram.exceptions import TelegramBadRequest

from application.database import UserDatabase
from application.settings import settings


async def notify_admins(bot: Bot, message: str, parse_mode: ParseMode = ParseMode.MARKDOWN):
    for admin_telegram_id in settings.ADMINS_TELEGRAM_ID:
        try:
            await bot.send_message(admin_telegram_id, message, parse_mode=parse_mode, disable_web_page_preview=True)
        except TelegramBadRequest:
            logging.warning(f"Failed to send message to admin {admin_telegram_id}")


NOTIFICATIONS = [
    "Кожного дня ти маєш 1140 хвилин життя⏰\nТому знайди 25 хвилин і приділи їх своєму тілу та здоров‘ю",
    "Ти маєш тренувати своє тіло, щоб воно не заважало тобі реалізовувати плани душі🪬",
    "В тебе все вийде! Найтяжче зробити перший крок, а далі відкривається новий, чудовий шлях. 🙏🏻",
    "Практики Йоги роблять твоє тіло молодим та здоровим\nі покращують пам‘ять та роботу мозку🧘🏻‍♂️",
    "Зверни увагу на своє дихання. Прямо зараз зупинись,\nі відчуй життя всередині себе🫁\nВідчуй як ти дихаєш",
    "Всі проблеми не тільки в голові - вони у тілі\nУ кожній з 30 трильйонів клітин які є в тобі\nЖени геть стрес і апатію і практикуй",
    "Ментальне здоров‘я так само важливе як і фізичне.\nПрацюєш над тілом - покращуєш роботу мозку🧠",
    "Страх, стрес і апатія.\nНе давай цим словам заважати тобі жити.\nПрактикуй і позбувайся негативу зі свого життя",
    "Тільки у спокійному та сприятливому розумі -\nможливо реалізовувати геніальні ідеї😊",
    "Залиште у своєму житті тільки те що надихає Вас\nі наповнює Енергією⚡️\nЗ усім іншим - прощайтесь без жалю",
    "Знаходь світло у собі та лови свій РИТМ -\nнавіть під час лютої пітьми🤍",
    "Цінуй кожен свій день,\nцінуй кожну хвилину свого життя - і ти будеш щасливий😊",
    "Твої мрії важливі - МРІЙ\nРухайся вперед, дій, досягай, здійснюй⚡️\nНе слухай тих хто каже негатив про тебе\nПрактикуй щоб стати сильним та наповненим",
    "Ми прагнемо Любові, Шукаємо Часу і боїмося Смерті🥺\nБудь сильним і незламним разом з йогою",
    "Ідеальності не існує - ти такий який є🤍\nІ в цьому твоя унікальність",
    "Прийми себе зі всіма недоліками\nШлях розвитку починається з любові до себе, а не з критики",
    "Дозволь собі падати🙏🏻\nДозволь собі допускати помилки\nНе бійся здаватися\nВсе що зараз відбувається - це шлях😊\nБез поразок - немає успіху.",
    "Не варто зациклюватися на тому чого вам бракує -\nне забувайте насолоджуватися тим що маєте.",
    "Годі хвилюватися за те що ВИ не контролюєте🙏🏻\nРозслабтесь. Практики йоги допоможуть в цьому.",
    "Це теж мине😊\nТобі погано, розлютився, злишся, не знаєш що робити.\nПрактикуй. І ти відчуєш кайф та енергію для життя та дій⚡️"
]

async def daily_notify(bot: Bot, db: UserDatabase):
    users = db.get_all_users_with_notifications()
    logging.info(users)
    for user in users:
        try:
            await bot.send_message(chat_id=user["telegram_id"], text=NOTIFICATIONS[user["next_notification_index"]])
            db.update_user_field(user["telegram_id"], "next_notification_index", user["next_notification_index"] + 1)
        except TelegramBadRequest as e:
            logging.warning(f"Failed to send message to user {user['telegram_id']}: {e}")
