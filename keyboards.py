
# keyboards.py


from typing import TYPE_CHECKING


from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


if TYPE_CHECKING:
   from i18n.stub import TranslatorRunner
else:
   from fluentogram import TranslatorRunner




# функция создания клавиатуры для карточки
def build_main_keyboard(
   i18n: TranslatorRunner, current_lang: str
) -> InlineKeyboardMarkup:
   is_ru = current_lang == "ru"
   ru_checked = "yes" if is_ru else "no"
   en_checked = "yes" if not is_ru else "no"
   return InlineKeyboardMarkup(
       inline_keyboard=[
           # кнопки смены языка
           [
               InlineKeyboardButton(
                   text=i18n.lang.ru(checked=ru_checked),
                   callback_data="lang_ru",
               ),
               InlineKeyboardButton(
                   text=i18n.lang.en(checked=en_checked),
                   callback_data="lang_en",
               ),
           ]
       ]
   )







