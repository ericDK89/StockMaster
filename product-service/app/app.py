"""Project Service FastAPI app.py config"""

from fastapi import FastAPI
from .models.product import Base
from app.config import Config
from .db.database import engine
from .routes import router

config = Config()

app = FastAPI(title=config.PROJECT_NAME, version=config.PROJECT_VERSION)

Base.metadata.create_all(bind=engine)

app.include_router(router)
