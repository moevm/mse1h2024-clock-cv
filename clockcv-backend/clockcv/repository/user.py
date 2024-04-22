import logging

from asyncpg import Pool
from pydantic import BaseModel
from datetime import datetime, date

logger = logging.getLogger(__name__)


class User(BaseModel):
    id: int
    name: str
    email: str
    password: str


class UserTest(BaseModel):
    id: int
    user_id: int
    points: int
    description: str
    date: datetime | date


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

    async def record_user_test(self, user_id: int, recognise_result: int, description: str) -> UserTest | None:
        """
        Создание истории
        """
        sql = """
            INSERT INTO user_tests (user_id, points, description)
            VALUES ($1, $2, $3)
            RETURNING *
        """
        async with self._db.acquire() as c:
            row = await c.fetchrow(sql, user_id, recognise_result, description)

        if not row:
            return

        result = UserTest(**dict(row))
        result.date = result.date.date()
        return result

    async def get_user_history(self, user_id: int) -> list[UserTest] | None:
        """
        Создание истории
        """
        sql = """
        SELECT * 
        FROM user_tests
        WHERE user_id=$1
        """
        async with self._db.acquire() as c:
            data = await c.fetch(sql, user_id)

        if not data:
            return

        result = [UserTest(**dict(row)) for row in data]
        for i in result:
            i.date = i.date.date()
        return result
