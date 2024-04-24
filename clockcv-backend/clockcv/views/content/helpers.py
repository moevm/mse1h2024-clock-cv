import hashlib
import os


def generate_password_sha256():
    password = os.urandom(16)  # Генерируем случайную последовательность байтов
    password_hash = hashlib.sha256(password).hexdigest()  # Хешируем пароль с помощью SHA-256
    password_hash = password_hash[0:10]
    return password_hash
