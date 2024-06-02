"""Project Service FastAPI app.py config"""

from fastapi import FastAPI
from .models.product import Base
from .config import config
from .db.database import engine
from .routes import router

app = FastAPI(title=config.PROJECT_NAME, version=config.PROJECT_VERSION)

Base.metadata.create_all(bind=engine)

app.include_router(router)
