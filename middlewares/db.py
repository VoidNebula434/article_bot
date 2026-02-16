import logging
from typing import Any, Awaitable, Callable, Dict

import aiosqlite
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject


logger = logging.getLogger(__name__)


class DatabaseMiddleware(BaseMiddleware):
    def __init__(self, db: aiosqlite.Connection):
        self._db = db

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        # прокидываем соединение с БД в обработчики
        data["db"] = self._db

        # создаем транзакцию на уровне апдейта
        try:
            result = await handler(event, data)
            await self._db.commit()
            logger.info(f"Transaction committed for event: {event}")
            return result
        except Exception:
            await self._db.rollback()
            logger.exception(f"Transaction rolled back for event: {event}")
            raise
