import logging
from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, User
from fluentogram import TranslatorHub

from db import get_user_language


logger = logging.getLogger(__name__)


class TranslatorRunnerMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        # получаем объект пользователя из апдейта
        user: User | None = data.get("event_from_user")

        if user is None:
            return await handler(event, data)

        # достаем переданный при старте поллинга объект TranslatorHub
        hub: TranslatorHub = data.get("translator_hub")

        # достаем переданный из первой миддлвари экземпляр соединения с БД
        db = data.get("db")

        # базовая локаль по умолчанию
        locale = "en"

        # в случае, если запрос - это нажатие на inline-кнопку смены языка,
        # текущей локалью становится локаль нажатой кнопки
        # это нужно чтобы в реальном времени менять язык отображаемого текста пользователю
        if (
            getattr(event, "callback_query")
            and event.callback_query
            and event.callback_query.data.startswith("lang")
        ):
            locale = event.callback_query.data.split("_")[1]

        # в случае если экземпляр соединения передан и пользователь зарегистрирован мы достаем его язык из БД
        elif db is not None:
            try:
                storage_locale = await get_user_language(db, user.id)
                if storage_locale:
                    locale = storage_locale
            except Exception:
                logger.exception("Failed to fetch user language")

        # получаем прокидываем дальше в обработчики TranslatorRunner с текстами в зависимости от локали пользователя
        data["i18n"] = hub.get_translator_by_locale(locale=locale)

        return await handler(event, data)
