"""File to handle product-service controller"""

from ..schemas.product_schema import ProductCreate, ProductOut, ProductUpdate
from ..exceptions.product_execptions import ProductException
from ..services.product_service import ProductService
from ..models.product import Product


class ProductController:
    """Class to validate data and raise errors if necessary"""

    def __init__(self, product_service: ProductService) -> None:
        self.__product_service: ProductService = product_service

    def create(self, product: ProductCreate) -> str:
        """Def to create product

        Args:
            product (ProductCreate): Body from response that comes in ProductCreate format

        Raises:
            ProductException: If there is an error on while tying to creare product
        """
        response: Product | str = self.__product_service.create(product)

        if not isinstance(response, Product):
            raise ProductException(name="AlreadyExists", message=response)

        return "Product successfully created"

    def get_products(self):
        """Method to return all products from db

        Returns:
            str: All products from db in str formatted
        """
        products = self.__product_service.get_products()

        if not products:
            return "Empty"

        return products

    def get_product_by_id(self, product_id: int) -> ProductOut:
        """Method to get product by id

        Args:
            product_id (str): Product Id from path parameters

        Raises:
            ProductException: If product is None raise ProductException

        Returns:
            Product: Return product found
        """
        product: ProductOut | None = self.__product_service.get_product_by_id(
            product_id=product_id
        )

        if not product:
            raise ProductException(name="Not found", message="Product not found")

        return product

    def update_product_by_id(self, product_id: int, data: ProductUpdate) -> Product:
        product: ProductOut | None = self.__product_service.update_product_by_id(
            product_id=product_id, data=data
        )

        """
        Updates an existing product identified by product_id with the new data provided.

        Args:
            product_id (int): The ID of the product to update.
            data (ProductCreate): The new product data for update.

        Raises:
            ProductException: If no product with the provided product_id is found.

        Returns:
            Product: Returns the updated product if the update is successful.
        """

        if not product:
            raise ProductException(
                message="Product not found", name="Product not found"
            )

        return product

    def delete_product_by_id(self, product_id: int):
        """
        Deletes a product by its ID.

        This method uses the ProductService to delete the product with the given ID.
        If the product does not exist, it raises a ProductException.
        If the product is successfully deleted, it returns a success message.

        Args:
            product_id (int): The ID of the product to be deleted.

        Returns:
            str: A success message if the product is deleted.

        Raises:
            ProductException: If the product does not exist.
        """
        response: str | None = self.__product_service.delete_product_by_id(
            product_id=product_id
        )

        if not response:
            raise ProductException(
                message="Product doesn't exist", name="Product doesn't exist"
            )

        return response
