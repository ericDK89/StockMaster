"""File to handle all product-service routes"""

from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse
from .schemas.product_schema import ProductCreate
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
        return JSONResponse(status_code=400, content={"error": str(e.message)})

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
