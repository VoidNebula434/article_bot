
# handlers/common.py


from datetime import date
from typing import TYPE_CHECKING


import aiosqlite
from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message


from config import get_config
from db import create_user, get_user_language, update_user_language
from keyboards import build_main_keyboard


# импорт сгенерированного нами stub файла для подсказок IDE
if TYPE_CHECKING:
   from i18n.stub import TranslatorRunner
else:
   from fluentogram import TranslatorRunner


# создаем роутер
router = Router()


# заглушки для настроек карточки, у вас может быть реализован собственный способ получения этих данных
YEARS_EXP = 7
PROJECTS_COUNT = 3
AVAILABILITY = "available"
CONTACT_PREFERENCE = "email"
UPDATED_AT = date(2026, 1, 15)




# обработчик команды '/start'
@router.message(Command("start"))
async def start_process(
   message: Message,
   # из миддлвари прокидываем в обработчики экземпляры соединения с БД и локализации пользователя
   db: aiosqlite.Connection,
   i18n: TranslatorRunner,
):
   # получаем язык пользователя
   lang = message.from_user.language_code or "en"


   # создаем нового пользователя в БД, если он первый раз запустил бота
   await create_user(db, message.from_user.id, lang)


   # определяем текущую локаль
   locale = await get_user_language(db, message.from_user.id)


   # формируем текст карточки
   intro = i18n.card.greeting(username=message.from_user.full_name)
   body = i18n.card.body(
       years_exp=YEARS_EXP,
       projects_count=PROJECTS_COUNT,
       availability=AVAILABILITY,
       contact_preference=CONTACT_PREFERENCE,
       updated_at=UPDATED_AT,
   )


   card_text = i18n.command.start_message(intro=intro, body=body)


   # отображаем карточку пользователю
   config = get_config()
   if config.card.photo:
       await message.answer_photo(
           photo=config.card.photo,
           caption=card_text,
           reply_markup=build_main_keyboard(i18n, locale),
       )
   else:
       await message.answer(
           card_text,
           reply_markup=build_main_keyboard(i18n, locale),
       )




# обработчик нажатия кнопки смены языка
@router.callback_query(F.data.startswith("lang"))
async def update_language(
   cb: CallbackQuery,
   db: aiosqlite.Connection,
   i18n: TranslatorRunner,
):
   # получаем выбранный язык и обновляем запись о пользователе в БД
   lang = cb.data.split("_")[1] if "_" in cb.data else cb.data
   await update_user_language(db, tg_id=cb.from_user.id, lang=lang)


   # формируем текст карточки
   intro = i18n.card.greeting(username=cb.from_user.full_name)
   body = i18n.card.body(
       years_exp=YEARS_EXP,
       projects_count=PROJECTS_COUNT,
       availability=AVAILABILITY,
       contact_preference=CONTACT_PREFERENCE,
       updated_at=UPDATED_AT,
   )


   card_text = i18n.command.start_message(intro=intro, body=body)


   # редактируем сообщение, отображая карточку на выбранном языке
   if cb.message:
       if cb.message.photo:
           await cb.message.edit_caption(
               caption=card_text,
               reply_markup=build_main_keyboard(i18n, lang),
           )
       else:
           await cb.message.edit_text(
               text=card_text,
               reply_markup=build_main_keyboard(i18n, lang),
           )


   await cb.answer()







