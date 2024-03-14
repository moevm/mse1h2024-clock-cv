import os

BACKEND_BASE_URL = os.environ["BACKEND_BASE_URL"]
STORAGE_DIR = os.environ["STORAGE_DIR"]
SENTRY_DSN = os.environ["SENTRY_DSN"]

SESSION_TTL_HOURS = 10
DATABASE_DSN = os.environ["DATABASE_DSN"]

AUTO_RELOAD = bool(os.environ.get("AUTO_RELOAD"))

ENVIRONMENT = os.environ.get("ENVIRONMENT", "unknown")

STATIC_DIR = os.path.join("/app", "clockcv", "static")

APP_NAME = os.environ.get("APP_NAME")