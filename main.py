import asyncio
import logging


from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage


from config import get_config
from db import init_db
from handlers import get_routers
from i18n.translator_hub import create_translator_hub
from middlewares.db import DatabaseMiddleware
from middlewares.i18n import TranslatorRunnerMiddleware


# настраиваем и инициализируем логирование
logging.basicConfig(
   level=logging.INFO, format="[%(asctime)s] %(levelname)s:%(name)s: %(message)s"
)


logger = logging.getLogger(__name__)




# получаем конфиг приложения и стартуем бота
async def main():
   config = get_config()


   # инициализируем БД, создаем таблицу для пользователей
   db = await init_db(config.db.path)


   bot = Bot(
       token=config.bot.token.get_secret_value(),
       default=DefaultBotProperties(parse_mode=ParseMode.HTML),
   )
   dp = Dispatcher(storage=MemoryStorage())


   # регистрируем миддлвари БД и i18n
   dp.update.middleware(DatabaseMiddleware(db))
   dp.update.middleware(TranslatorRunnerMiddleware())


   # регистрируем хендлеры
   dp.include_routers(*get_routers())


   # создаем объект TranslatorHub
   hub = create_translator_hub()


   # запускаем поллинг бота
   try:
       await dp.start_polling(bot, translator_hub=hub)
   finally:
       await db.close()




if __name__ == "__main__":
   asyncio.run(main())







