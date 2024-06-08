"""File to takes unit tests for product-repository"""

from typing import List
from unittest.mock import MagicMock
import pytest
from sqlalchemy.orm import Session
from app.models.product import Product
from app.schemas.product_schema import ProductCreate, ProductOut
from app.repositories.product_repository import ProductRepository


@pytest.fixture(scope="function")
def db_session() -> MagicMock:
    """Define the MagicMock to be a spec of Session"""
    return MagicMock(spec=Session)


@pytest.fixture(scope="function")
def product_repository(db_session: MagicMock) -> ProductRepository:
    """Define the Product Repository with mock session db"""
    return ProductRepository(db=db_session)


def test_create_product(
    product_repository: ProductRepository, db_session: MagicMock
) -> None:
    """Def to test create product from repository"""
    product_data = Product(
        name="Test Product",
        description="Test Description",
        price=9.99,
        stock_quantity=10,
    )

    db_session.add.return_value = None
    db_session.commit.return_value = None
    db_session.refresh.return_value = None

    created_product: Product = product_repository.create(product_data)

    assert created_product == product_data
    db_session.add.assert_called_once_with(created_product)
    db_session.commit.assert_called_once()
    db_session.refresh.assert_called_once()


def test_find_by_name_if_product_exists(
    product_repository: ProductRepository, db_session: MagicMock
) -> None:
    """Def to test find by name"""

    product_data = Product(
        name="Test Product",
        description="Test Description",
        price=9.99,
        stock_quantity=10,
    )

    # ! Necessary to configure each step of the Session (SQLAlchemy) call
    db_session.query().filter().first.return_value = product_data

    found_product: Product = product_repository.find_by_name(product_data.name)

    assert found_product == product_data

    db_session.query().filter().first.assert_called_once()


def test_get_all_products(
    product_repository: ProductRepository, db_session: MagicMock
) -> None:
    """Def to test the repository get_all_products"""
    product_data_one = ProductCreate(
        name="Test Product",
        description="Test Description",
        price=9.99,
        stock_quantity=10,
    )

    product_data_two = ProductCreate(
        name="Test Product two",
        description="Test Description two",
        price=9.99,
        stock_quantity=10,
    )

    db_session.query().all.return_value = [
        Product(id=1, **product_data_one.model_dump()),
        Product(id=2, **product_data_two.model_dump()),
    ]

    response: List[Product] = product_repository.get_products()

    assert len(response) == 2
    assert response[0].name == product_data_one.name
    assert response[1].name == product_data_two.name

    db_session.query().all.assert_called_once()


def test_get_product_by_id(
    product_repository: ProductRepository, db_session: MagicMock
) -> None:
    """Def to test get_product_by_id from repository

    Args:
        product_repository (ProductRepository): ProductRepository
        db_session (MagicMock): Mock for db_session
    """

    product_data_one = ProductCreate(
        name="Test Product",
        description="Test Description",
        price=9.99,
        stock_quantity=10,
    )

    product_id = 1
    product = Product(id=product_id, **product_data_one.model_dump())

    db_session.query().filter().first.return_value = product

    response: ProductOut = product_repository.get_product_by_id(product_id=product_id)

    print(response)

    assert response.name == product_data_one.name

    db_session.query().filter().first.assert_called_once()
