"""File to configs"""

import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """
    This class represents the configuration for the application.

    Attributes:
    PROJECT_NAME (str): The name of the project.
    PROJECT_VERSION (str): The version of the project.
    POSTGRES_USER (str): The username for the PostgreSQL database.
    POSTGRES_PASSWORD (str): The password for the PostgreSQL database.
    POSTGRES_DB (str): The name of the PostgreSQL database.
    POSTGRES_HOST (str): The host of the PostgreSQL database.
    POSTGRES_PORT (int): The port of the PostgreSQL database.
    DATABASE_URL (str): The connection string for the PostgreSQL database.
    """

    PROJECT_NAME: str = "Inventory Management"
    PROJECT_VERSION: str = "1.0.0"

    # DB
    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB")
    POSTGRES_HOST: str = os.getenv("POSTGRES_HOST", "db")
    POSTGRES_PORT: int = int(os.getenv("POSTGRES_PORT", 5432))

    DATABASE_URL: str = (
        f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
    )


class TestConfig:
    """
    This class represents the configuration for the application during testing.

    Attributes:
    DATABASE_URL (str): The connection string for the SQLite database used during testing.
    """

    DATABASE_URL: str = "sqlite:///./test.db"
