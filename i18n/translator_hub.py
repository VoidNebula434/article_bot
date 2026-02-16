from fluent_compiler.bundle import FluentBundle
from fluentogram import FluentTranslator, TranslatorHub


# создание TranslatorHub
def create_translator_hub() -> TranslatorHub:
    translator_hub = TranslatorHub(
        # указываем карту локалей для нашего приложения
        locales_map={"ru": ("ru", "en"), "en": ("en", "ru")},
        # указываем список FluentTranslator для каждой локали
        translators=[
            FluentTranslator(
                locale="ru",  # локаль за которую отвечает объект
                translator=FluentBundle.from_files(  # указание локали и путей к файлам содержащим текста
                    locale="ru-RU", filenames=["i18n/locales/ru/LC_MESSAGES/txt.ftl"]
                ),
            ),
            FluentTranslator(
                locale="en",
                translator=FluentBundle.from_files(
                    locale="en-US", filenames=["i18n/locales/en/LC_MESSAGES/txt.ftl"]
                ),
            ),
        ],
    )
    return translator_hub
