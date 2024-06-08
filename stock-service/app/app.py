from fastapi import FastAPI
from config import Config

config = Config()

app = FastAPI(title=config.PROJECT_NAME, version=config.PROJECT_VERSION)
