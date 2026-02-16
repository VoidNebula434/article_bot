
# db/connection.py


import aiosqlite


# SQL запрос создания таблицы users
CREATE_USERS_TABLE = """
CREATE TABLE IF NOT EXISTS users (
   tg_id BIGINT PRIMARY KEY,
   language VARCHAR(3) NOT NULL
);
"""




# инициализация БД
async def init_db(db_path: str) -> aiosqlite.Connection:
   db = await aiosqlite.connect(db_path)
   try:
       await db.execute(CREATE_USERS_TABLE)
       await db.commit()
       return db
   except Exception:
       await db.close()
       raise







