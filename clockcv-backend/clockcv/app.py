import asyncio
import logging

import sentry_sdk
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exception_handlers import request_validation_exception_handler
from fastapi.exceptions import RequestValidationError
from sentry_sdk.integrations.fastapi import FastApiIntegration

import clockcv.conf as conf
import clockcv.log as log
import clockcv.middlewares as middlewares
import clockcv.migrations_runner as migrations_runner
from clockcv.state import app_state
from clockcv.views.content.views import router as content_router

log.setup_logging()
logger = logging.getLogger(__name__)

sentry_sdk.init(
    dsn=conf.SENTRY_DSN,
    integrations=[FastApiIntegration()],
    environment=conf.ENVIRONMENT,
)

app = FastAPI()
app.middleware("http")(middlewares.access_log_middleware)
app.middleware("http")(middlewares.request_time_middleware)
app.middleware("http")(middlewares.request_status_middleware)
app.middleware("http")(middlewares.request_id_middleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://0.0.0.0:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"])
app.include_router(content_router)


@app.on_event("startup")
async def setup():
    if conf.ENVIRONMENT == "dev":
        await asyncio.sleep(10)
    migrations_runner.apply()
    await app_state.startup()


@app.on_event("shutdown")
async def shutdown():
    await app_state.shutdown()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    logger.info("Validation error=%s", {"url": request.url, "err": exc})
    return await request_validation_exception_handler(request, exc)


if __name__ == "__main__":
    uvicorn.run(
        app="clockcv.app:app",
        host="0.0.0.0",
        port=8000,
        reload=conf.AUTO_RELOAD,
        access_log=False,
    )
