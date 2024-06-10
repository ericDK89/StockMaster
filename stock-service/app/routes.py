from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from dependencies.stock_dependencies import get_stock_controller
from controllers.stock_controller import StockController
from models.stock import Stock
from exceptions.stock_exceptions import StockException
from schemes.stock_schema import StockUpdate, StockOut

router = APIRouter()


@router.get("/stock/{product_id}")
def get_stock_by_product_id(
    product_id: int,
    stock_controller: StockController = Depends(get_stock_controller),
) -> JSONResponse:
    try:
        response: Stock = stock_controller.get_stock_by_product_id(
            product_id=product_id
        )
        return JSONResponse(status_code=200, content={"success": response})

    except StockException as e:
        return JSONResponse(status_code=404, content={"error": str(e.message)})

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": f"Internal Server Error \n Message: {str(e)}"},
        )


@router.put("/stock/{stock_id}")
def update(
    stock_id: int,
    data: StockUpdate,
    stock_controller: StockController = Depends(get_stock_controller),
) -> JSONResponse:
    try:
        response: StockOut = stock_controller.update(stock_id=stock_id, data=data)

        return JSONResponse(status_code=200, content={"success": response})

    except StockException as e:
        return JSONResponse(status_code=404, content={"error": str(e.message)})

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": f"Internal Server Error \n Message: {str(e)}"},
        )
