from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from typing import Callable, Dict, Any

from application.database import UserDatabase


class DBMiddleware(BaseMiddleware):
    def __init__(self, db: UserDatabase):
        self.db = db

    async def __call__(
        self,
        handler: Callable,
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        data["db"] = self.db
        return await handler(event, data)
