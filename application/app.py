import logging

from aiogram import Bot, Dispatcher

from application.handlers import router
from application.middlewares import DBMiddleware
from application.settings import settings
from application.utils import notify_admins
from application.database import UserDatabase


async def on_startup(bot: Bot):
    logging.info("Bot started")
    await notify_admins(bot, "Bot started")


async def on_shutdown(bot: Bot):
    logging.info("Bot stopped")
    await notify_admins(bot, "Bot stopped")


async def run():
    bot = Bot(token=settings.BOT_API_TOKEN.get_secret_value())
    dp = Dispatcher()

    db = UserDatabase()

    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    dp.update.middleware(DBMiddleware(db))
    dp.include_router(router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
