"""File to handle db creation from product-service"""

import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker
from app.config import Config, TestConfig

load_dotenv()

config = TestConfig() if os.getenv("TESTING") else Config()

SQLALCHEMY_DATABASE_URL: str = config.DATABASE_URL

engine: Engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """Def to start and close db"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
