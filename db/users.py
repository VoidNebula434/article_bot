
# db/users.py


import aiosqlite




# получение языка пользователя
async def get_user_language(db: aiosqlite.Connection, tg_id: int) -> str | None:
   async with db.execute(
       "SELECT language FROM users WHERE tg_id = ?", (tg_id,)
   ) as cursor:
       row = await cursor.fetchone()
       return row[0] if row else None




# создание нового пользователя
async def create_user(db: aiosqlite.Connection, tg_id: int, lang: str) -> None:
   await db.execute(
       "INSERT OR IGNORE INTO users (tg_id, language) VALUES (?, ?)", (tg_id, lang)
   )




# обновление языка пользователя
async def update_user_language(db: aiosqlite.Connection, tg_id: int, lang: str) -> None:
   await db.execute(
       """
       INSERT INTO users (tg_id, language)
       VALUES (?, ?)
       ON CONFLICT(tg_id) DO UPDATE SET language = excluded.language
       """,
       (tg_id, lang),
   )







