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


@asynccontextmanager
async def lifespan(app: FastAPI):
    thread = threading.Thread(target=messaging.start_consuming)
    thread.start()
    yield
    thread.join()


app.router.lifespan_context = lifespan

app.include_router(router)
