"""File to test all product_service methods"""

from typing import List
from unittest.mock import MagicMock
import pytest
from app.services.product_service import ProductService
from app.schemas.product_schema import ProductCreate, ProductOut, ProductUpdate
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


def test_get_products_service(
    product_service: ProductService, product_repository_mock: MagicMock
) -> None:
    """Test to assert service to get products return a list of produtcs"""
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

    product_repository_mock.get_products.return_value = [
        Product(id=1, **product_data_one.model_dump()),
        Product(id=2, **product_data_two.model_dump()),
    ]

    products: List[Product] = product_service.get_products()

    assert len(products) == 2
    assert products[0]["name"] == product_data_one.name
    assert products[1]["name"] == product_data_two.name

    product_repository_mock.get_products.assert_called_once()


def test_get_product_by_id(
    product_service: ProductService, product_repository_mock: MagicMock
) -> None:
    """Def to test get product by id service

    Args:
        product_service (ProductService): Product Service
        product_repository_mock (MagicMock): Mock Product Repository
    """

    product_data_one = ProductCreate(
        name="Test Product",
        description="Test Description",
        price=9.99,
        stock_quantity=10,
    )

    product_id = 1
    product = Product(id=product_id, **product_data_one.model_dump())

    product_repository_mock.get_product_by_id.return_value = product

    response: ProductOut = product_service.get_product_by_id(product_id=product_id)

    assert response.get("name") == product_data_one.name

    product_repository_mock.get_product_by_id.assert_called_once_with(
        product_id=product_id
    )


def test_update_product_by_id(
    product_service: ProductService, product_repository_mock: MagicMock
) -> None:
    """
    Unit test for the 'update_product_by_id' method of the ProductService class.

    This test checks if the 'update_product_by_id' method of the ProductService class calls the
    'update_product_by_id' method of the product repository with the correct arguments and returns the expected product.

    Args:
        product_service (ProductService): An instance of ProductService to test.
        product_repository_mock (MagicMock): A mock product repository to simulate its behavior.

    Raises:
        AssertionError: If the test fails.
    """
    product_data_one = ProductCreate(
        name="Test Product",
        description="Test Description",
        price=9.99,
        stock_quantity=10,
    )

    product_id = 1
    product = Product(id=product_id, **product_data_one.model_dump())

    product_repository_mock.get_product_by_id.return_value = product

    updated_product = ProductUpdate(name="Update Product")

    expected_product = ProductOut(
        id=product_id,
        name="Update Product",
        description="Test Description",
        price=9.99,
        stock_quantity=10,
    )

    product_repository_mock.update_product_by_id.return_value = expected_product

    response: ProductOut = product_service.update_product_by_id(
        product_id=product_id, data=updated_product
    )

    print(response)

    assert response.get("name") == expected_product.name

    product_repository_mock.update_product_by_id.assert_called_once_with(
        product_id=product_id, data=updated_product
    )


def test_delete_product_by_id(
    product_service: ProductService, product_repository_mock: MagicMock
) -> None:
    """
    Testa o método delete_product_by_id do ProductService.

    Este teste verifica se o método delete_product_by_id do ProductService chama o método delete_product_by_id do ProductRepository com os argumentos corretos e se lida corretamente com o valor de retorno.

    Args:
        product_service (ProductService): O ProductService a ser testado.
        product_repository_mock (MagicMock): Um mock do ProductRepository.

    Returns:
        None
    """
    product_id = 1

    product_repository_mock.delete_product_by_id.return_value = (
        "Product successfully deleted"
    )

    response: str = product_service.delete_product_by_id(product_id=product_id)

    assert response == "Product successfully deleted"

    product_repository_mock.delete_product_by_id.assert_called_once_with(
        product_id=product_id
    )
