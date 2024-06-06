"""File to takes unit tests for product-controller"""

from typing import List
from unittest.mock import MagicMock
import pytest
from app.controllers.products_controllers import ProductController
from app.services.product_service import ProductService
from app.schemas.product_schema import ProductCreate
from app.models.product import Product
from app.exceptions.product_execptions import ProductException


@pytest.fixture(scope="function")
def product_service_mock():
    """Def to create MagicMock"""
    return MagicMock(spec=ProductService)


@pytest.fixture(scope="function")
def product_controller(product_service_mock: MagicMock) -> ProductController:
    """Def to create product_service_mock"""
    return ProductController(product_service=product_service_mock)


def test_create_product(
    product_controller: ProductController, product_service_mock: MagicMock
) -> None:
    """Test to assert that is possible to create a producto"""
    product_data = ProductCreate(
        name="Test Product",
        description="Test Description",
        price=9.99,
        stock_quantity=10,
    )

    # * Make sure that the service mock return is a Product
    product_service_mock.create.return_value = Product(**product_data.model_dump())

    # * Takes the controller return
    response: str = product_controller.create(product_data)

    # * Assert that the return is a successfully message
    assert response == "Product successfully created"

    # * Assert that the service_mock was called
    product_service_mock.create.assert_called_once_with(product_data)


def test_try_to_create_product_with_the_same_name(
    product_controller: ProductController, product_service_mock: MagicMock
) -> None:
    """Test to assert that isn't possible to create a product with the same name"""
    product_data = ProductCreate(
        name="Test Product",
        description="Test Description",
        price=9.99,
        stock_quantity=10,
    )

    # * Create the exception message
    exception_message: str = f"Product with name '{product_data.name}' already exists"

    # * Make the mock service return the exception_message
    product_service_mock.create.return_value = exception_message

    # * Assert that the controller create raises a ProductException
    with pytest.raises(ProductException) as exc_info:
        product_controller.create(product_data)

    # * Assert the messagem from exception
    assert exc_info.value.message == exception_message

    # * Assert that the service mock create was called
    product_service_mock.create.assert_called_once_with(product_data)


def test_get_all_products(
    product_controller: ProductController, product_service_mock: MagicMock
) -> None:
    """Test to assert that it will return all products"""
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

    all_products: List[Product] = [
        Product(id=1, **product_data_one.model_dump()),
        Product(id=2, **product_data_two.model_dump()),
    ]

    product_service_mock.get_products.return_value = all_products

    response: List[Product] = product_controller.get_products()

    assert len(response) == 2

    assert response[0].name == product_data_one.name
    assert response[1].name == product_data_two.name

    product_service_mock.get_products.assert_called_once()
