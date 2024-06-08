"""Project Service FastAPI app.py config"""

from fastapi import FastAPI
from config import Config
from models.product import Base
from db.database import engine
from routes import router

config = Config()

app = FastAPI(title=config.PROJECT_NAME, version=config.PROJECT_VERSION)

Base.metadata.create_all(bind=engine)

app.include_router(router)
