from email.message import EmailMessage
from ssl import SSLContext
from typing import Sequence

import aiosmtplib


class MailClient:
    def __init__(self, host: str, port: int, username: str, password: str):
        self._host = host
        self._port = port
        self._username = username
        self._password = password

    async def send_message(
        self, to: str | Sequence[str], subject: str, text: str
    ):
        message = EmailMessage()
        message.set_content(text, "html")
        message["Subject"] = subject
        message["From"] = self._username
        message["To"] = to
        await aiosmtplib.send(
            message,
            sender=self._username,
            recipients=to,
            hostname=self._host,
            port=self._port,
            username=self._username,
            password=self._password,
            use_tls=False,
            tls_context=SSLContext(),
            timeout=10,
        )
