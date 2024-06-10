"""File to start database"""

import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker, Session
from config import TestConfig, Config

load_dotenv()

config = TestConfig() if os.getenv("TESTING") else Config()

SQLALCHEMY_DATABASE_URL: str = config.DATABASE_URL

engine: Engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """
    This function creates a new SQLAlchemy session and yields it for use.

    After the session is used, it is closed.

    Yields:
    Session: The SQLAlchemy session.
    """
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
