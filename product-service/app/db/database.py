"""File to handle db creation from product-service"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..config import config

SQLALCHEMY_DATABASE_URL = config.DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """Def to start and close db"""
    with SessionLocal() as db:
        yield db
