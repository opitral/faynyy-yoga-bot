from aiogram import Bot
from aiogram.enums import ParseMode

from application.settings import settings


async def notify_admins(bot: Bot, message: str, parse_mode: ParseMode = ParseMode.MARKDOWN):
    for admin_telegram_id in settings.ADMINS_TELEGRAM_ID:
        await bot.send_message(admin_telegram_id, message, parse_mode=parse_mode, disable_web_page_preview=True)
