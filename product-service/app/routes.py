"""File to handle all product-service routes"""

from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from .schemas.product_schema import ProductCreate, ProductOut
from typing import List
from .controllers import create_products_controllers
from .exceptions.product_execptions import ProductException

router = APIRouter()


@router.post("/products")
def create_product(product: ProductCreate):
    """Def to create product

    Args:
        product (ProductCreate): Body from request

    Returns:
        JSONResponse: Json response with message of success or error
    """
    try:
        create_products_controllers.execute(product)

        return JSONResponse(
            status_code=201, content={"success": "Product successfully created"}
        )
    except ProductException as e:
        return JSONResponse(status_code=400, content={"error": str(e.message)})
    except HTTPException as e:
        return JSONResponse(status_code=400, content={"error": str(e.detail)})
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": f"Internal Server Error \n Message: {str(e)}"},
        )
