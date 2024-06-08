"""File to handle all product-service routes"""

from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse
from .schemas.product_schema import ProductCreate, ProductOut, ProductUpdate
from .exceptions.product_execptions import ProductException
from .dependencies.product_dependencies import get_product_controller
from .controllers.products_controllers import ProductController


router = APIRouter()


@router.post("/products")
def create_product(
    product: ProductCreate,
    product_controller: ProductController = Depends(get_product_controller),
) -> JSONResponse:
    """Def to create product

    Args:
        product (ProductCreate): Body from request
        product_controller: ProductController

    Returns:
        JSONResponse: Json response with message of success or error
    """
    try:
        response: str = product_controller.create(product)
        return JSONResponse(status_code=201, content={"success": response})

    except ProductException as e:
        return JSONResponse(status_code=404, content={"error": str(e.message)})

    except HTTPException as e:
        return JSONResponse(status_code=400, content={"error": str(e.detail)})

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": f"Internal Server Error \n Message: {str(e)}"},
        )


@router.get("/products")
def get_products(
    product_controller: ProductController = Depends(get_product_controller),
) -> JSONResponse:
    """Route to get all products from db

    Args:
        product_controller (ProductController, optional): _description_. Defaults to Depends(get_product_controller).

    Returns:
        JSONResponse: return as json with "success" and the response (all products)
    """
    try:
        response = product_controller.get_products()
        print(response)
        return JSONResponse(status_code=200, content={"success": response})

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": f"Internal Server Error \n Message: {str(e)}"},
        )


@router.get("/product/{product_id}")
def get_product_by_id(
    product_id: int,
    product_controller: ProductController = Depends(get_product_controller),
) -> JSONResponse:
    """Def to get product by id

    Args:
        product_id (str): product_id from path paramets
        product_controller (ProductController, optional): ProductController to use get_product_by_id method.
        Defaults to Depends(get_product_controller).

    Returns:
        JSONResponse: Return a json with "success" or "error"
    """
    try:
        product: ProductOut = product_controller.get_product_by_id(
            product_id=product_id
        )
        return JSONResponse(status_code=200, content={"success": product})

    except ProductException as e:
        return JSONResponse(status_code=404, content={"error": str(e.message)})
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": f"Internal Server Error \n Message: {str(e)}"},
        )


@router.put("/product/{product_id}")
def update_product_by_id(
    product_id: int,
    product: ProductUpdate,
    product_controller: ProductController = Depends(get_product_controller),
) -> JSONResponse:
    """
    Updates an existing product identified by product_id with the new data provided.

    Args:
        product_id (int): The ID of the product to update.
        product (ProductCreate): The new product data for update.
        product_controller (ProductController, optional): ProductController to use update_product_by_id method.
        Defaults to Depends(get_product_controller).

    Returns:
        JSONResponse: Returns a JSON response with status code 200 and a "success" key containing the updated product
                      if the update is successful. Returns a JSON response with status code 404 and an "error" key if
                      no product with the provided product_id is found. Returns a JSON response with status code 500
                      and an "error" key if an internal server error occurs.
    """
    try:
        response: ProductOut = product_controller.update_product_by_id(
            product_id=product_id, data=product
        )

        return JSONResponse(status_code=200, content={"success": response})

    except ProductException as e:
        return JSONResponse(status_code=404, content={"error": str(e.message)})
    except Exception as e:
        return JSONResponse(
            status_code=500, content={f"Internal Server Error \n Message: {str(e)}"}
        )


@router.delete("/product/{product_id}")
def delete_product_by_id(
    product_id: int,
    product_controller: ProductController = Depends(get_product_controller),
) -> None:
    """
    Deletes a product by its ID.

    This function receives a product ID as a path parameter and uses the ProductController to delete the product.
    If the product is successfully deleted, it returns a JSON response with a status code of 204 and a success message.
    If a ProductException is raised during the process, it returns a JSON response with a status code of 404 and the error message.
    For any other exceptions, it returns a JSON response with a status code of 500 and the error message.

    Args:
        product_id (int): The ID of the product to be deleted.
        product_controller (ProductController): The controller used to perform the delete operation. This is injected by the FastAPI Depends mechanism.

    Returns:
        None
    """
    try:
        response: str = product_controller.delete_product_by_id(product_id)
        return JSONResponse(status_code=204, content={})

    except ProductException as e:
        return JSONResponse(status_code=404, content={"error": str(e)})
    except Exception as e:
        return JSONResponse(
            status_code=500, content={f"Internal Server Error \n Message: {str(e)}"}
        )
