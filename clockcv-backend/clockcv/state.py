import json
from concurrent.futures import ThreadPoolExecutor

from asyncpg import Pool, create_pool

import clockcv.conf as conf

from clockcv.repository.user import UserRepository
from clockcv.clients.mailing import MailClient


class AppState:
    def __init__(self) -> None:
        self._db = None
        self._user_repo = None
        self._mail_client = None

    async def init_connection(self, conn):
        await conn.set_type_codec(
            "jsonb",
            encoder=json.dumps,
            decoder=json.loads,
            schema="pg_catalog",
        )

    async def startup(self, from_tasks: bool = False) -> None:
        self._db = await create_pool(
            dsn=conf.DATABASE_DSN, init=self.init_connection
        )
        self._user_repo = UserRepository(db=self._db)
        self._mail_client = MailClient(
            host="smtp.yandex.ru",
            port=587,
            username="clockcv@yandex.ru",
            password="icevxksmpnnhbbdq"
        )

    async def shutdown(self) -> None:
        if self._db:
            await self._db.close()

    @property
    def db(self) -> Pool:
        assert self._db
        return self._db

    @property
    def user_repo(self) -> UserRepository:
        assert self._user_repo
        return self._user_repo

    @property
    def mail_client(self) -> MailClient:
        assert self._mail_client
        return self._mail_client


app_state = AppState()
