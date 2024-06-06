"""File to handle integrations tests"""

from typing import List
from app.schemas.product_schema import ProductCreate
from app.models.product import Product


def test_create_product(client, db_session) -> None:
    """Def to test creation product"""
    create_response = client.post(
        "/products",
        json={
            "name": "Test Product",
            "description": "Test Description",
            "price": 9.99,
            "stock_quantity": 10,
        },
    )

    # * Assert the creation product response
    assert create_response.status_code == 201
    assert create_response.json() == {"success": "Product successfully created"}

    db_product: Product = (
        db_session.query(Product).filter(Product.name == "Test Product").first()
    )

    # * Make sure that the db is working
    assert db_product is not None
    assert db_product.name == "Test Product"
    assert db_product.description == "Test Description"
    assert db_product.price == 9.99
    assert db_product.stock_quantity == 10


def test_get_all_products(client, db_session) -> None:
    """Def to integration test for get all products"""
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
        Product(**product_data_one.model_dump()),
        Product(**product_data_two.model_dump()),
    ]

    db_session.add_all(all_products)
    db_session.commit()

    get_products = client.get("/products")

    assert get_products.status_code == 200
