"""File to create a config test for integration tests"""

import os

os.environ["TESTING"] = "1"

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app.app import app
from app.dependencies.product_dependencies import get_product_repository
from app.models.product import Base
from app.db.database import engine, SessionLocal as TestingSessionLocal


Base.metadata.create_all(bind=engine)


@pytest.fixture(scope="function")
def db_session():
    """Def to create TestSession db"""
    Base.metadata.create_all(bind=engine)
    with TestingSessionLocal() as session:
        yield session
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def client(db_session: Session):
    """Def to override the original get_db to the test db_session"""
    client = TestClient(app)
    yield client
    app.dependency_overrides[get_product_repository] = get_product_repository
