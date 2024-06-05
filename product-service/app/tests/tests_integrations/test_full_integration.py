from ..tests_integrations.conftest import client, db_session
from app.models.product import Product


def test_create_product(client, db_session) -> None:
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
