"""File to create app and start FastAPI on stock service"""

import threading
from contextlib import asynccontextmanager
from fastapi import FastAPI
from config import Config
from db.database import engine
from models.stock import Base
from routes import router
import messaging

config = Config()

app = FastAPI(title=config.PROJECT_NAME, version=config.PROJECT_VERSION)

Base.metadata.create_all(bind=engine)

consumer_thread = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    This function is an asynchronous context manager that manages the lifespan of the application.
    It starts a new thread for consuming messages when the application starts and stops consuming messages when the application stops.

    Parameters:
    app (FastAPI): The FastAPI application.

    Yields:
    None

    The function starts a new thread for consuming messages when entering the context and stops consuming messages and joins the thread when exiting the context.
    """
    global consumer_thread
    consumer_thread = threading.Thread(target=messaging.start_consuming)
    consumer_thread.start()
    yield
    messaging.stop_consuming()
    consumer_thread.join()


app.router.lifespan_context = lifespan

app.include_router(router)
