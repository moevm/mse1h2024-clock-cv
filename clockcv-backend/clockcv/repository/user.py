import logging

from asyncpg import Pool
from pydantic import BaseModel

logger = logging.getLogger(__name__)


class User(BaseModel):
    id: int
    name: str
    email: str
    password: str


class UserRepository:
    def __init__(self, db: Pool):
        self._db = db

    async def create_user(self, name: str, email: str, password: str) -> User | None:
        """
        Создание пользователя
        """
        sql = """
            INSERT INTO users (name, email, password)
            VALUES ($1, $2, $3)
            RETURNING *
        """
        async with self._db.acquire() as c:
            row = await c.fetchrow(sql, name, email, password)

        if not row:
            return

        return User(**dict(row))

    async def get_user_by_id(self, id_: int) -> User | None:
        """
        Получение пользователя по id
        """
        sql = """
            SELECT *
            FROM users
            WHERE id = $1
        """
        async with self._db.acquire() as c:
            row = await c.fetchrow(sql, id_)

        if not row:
            return

        return User(**dict(row))

    async def get_user_by_email(self, email: str) -> User | None:
        """
        Получение пользователя по email
        """
        sql = """
            SELECT *
            FROM users
            WHERE email = $1
        """
        async with self._db.acquire() as c:
            row = await c.fetchrow(sql, email)

        if not row:
            return

        return User(**dict(row))

    async def check_user_by_password(self, email: str, password: str) -> User | None:
        """
        Проверка пароля
        """
        sql = """
            SELECT *
            FROM users
            WHERE email = $1 AND password = $2
        """
        async with self._db.acquire() as c:
            row = await c.fetchrow(sql, email, password)

        if not row:
            return

        return User(**dict(row))
