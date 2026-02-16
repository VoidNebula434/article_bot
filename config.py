
# config.py


from functools import lru_cache


from environs import Env
from pydantic import BaseModel, SecretStr




# создаем модель конфига бота
class BotConfig(BaseModel):
   token: SecretStr




# конфиг для БД
class DbConfig(BaseModel):
   path: str




# конфиг для карточки
class CardConfig(BaseModel):
   photo: str | None = None




# и модель конфига приложения
class ConfigModel(BaseModel):
   bot: BotConfig
   db: DbConfig
   card: CardConfig




# функция в которой собираем конфиг
@lru_cache
def get_config(path: str | None = None) -> ConfigModel:
   env = Env()
   env.read_env(path)


   return ConfigModel(
       bot=BotConfig(
           token=env.str("BOT_TOKEN"),
       ),
       db=DbConfig(path=env.str("DB_PATH")),
       card=CardConfig(photo=env.str("CARD_PHOTO", default="") or None),
   )



