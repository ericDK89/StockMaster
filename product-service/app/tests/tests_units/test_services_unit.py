"""File to test all product_service methods"""

from unittest.mock import MagicMock
import pytest
from app.services.product_service import ProductService
from app.schemas.product_schema import ProductCreate
from app.models.product import Product


@pytest.fixture(scope="function")
def product_repository_mock() -> MagicMock:
    """Def to create the MagicMock to be used on all the code"""
    return MagicMock()


@pytest.fixture(scope="function")
def product_service(product_repository_mock: MagicMock) -> ProductService:
    """Def to generate product_service to be used on all the code"""
    return ProductService(product_repository_mock)


def test_create_product_when_product_already_exists(
    product_service: ProductService, product_repository_mock: MagicMock
) -> None:
    """Def to test if it's possible to create a product with a name that already exists

    Args:
        product_service (ProductService): Product Service
        product_repository_mock (MagicMock): Magic Mock
    """

    # * Define the product data of type ProductCreate
    product_data = ProductCreate(
        name="Test Product",
        description="Test Description",
        price=9.99,
        stock_quantity=10,
    )

    # * Create an instance of Product to simulate an existing product in the database
    existing_product = Product(id=1, **product_data.model_dump())

    # * Mock the repository to return the existing_product when find_by_name is called
    product_repository_mock.find_by_name.return_value = existing_product

    # * Attempt to create a product with the same data
    result: Product = product_service.create(product_data)

    # * Assert that the method find_by_name was called
    product_repository_mock.find_by_name.assert_called_once()

    # * Assert that the result has the name of product
    assert product_data.name in result


def test_create_product_when_product_dont_exists(
    product_service: ProductService, product_repository_mock: MagicMock
) -> None:
    """Def to test if it's possible to create a product if there is no other with the same name on db

    Args:
        product_service (ProductService): ProductService
        product_repository_mock (MagicMock): MockRepository
    """

    # * Define the product data of type ProductCreate
    product_data = ProductCreate(
        name="Test Product",
        description="Test Description",
        price=9.99,
        stock_quantity=10,
    )

    # * Mock the repository to return None when find_by_name is called, indicating that the product does not exist
    product_repository_mock.find_by_name.return_value = None

    # * Mock the repository to call the create method
    product_repository_mock.create.return_value = Product(**product_data.model_dump())

    # * Call the create method of the service
    result: Product = product_service.create(product_data)

    # * Assert that the repository's find_by_name method was called once with the product name and didn't find anything
    product_repository_mock.find_by_name.assert_called_once_with(product_data.name)

    # * Assert that the repository's create method was called once
    product_repository_mock.create.assert_called_once()

    # * Assert that the result is the new product
    assert result.name == product_data.name
    assert result.description == product_data.description
    assert result.price == product_data.price
    assert result.stock_quantity == product_data.stock_quantity