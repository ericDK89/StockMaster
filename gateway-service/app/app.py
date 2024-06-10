"""File to start up the gateway"""

from fastapi import FastAPI, Request, HTTPException, Response
from fastapi.responses import JSONResponse
import httpx

app = FastAPI()


async def proxy(request: Request, service_url: str) -> JSONResponse:
    """
    This function acts as a proxy to forward requests to a specified service URL.

    Parameters:
    request (Request): The incoming request to be forwarded.
    service_url (str): The base URL of the service to which the request should be forwarded.

    Returns:
    JSONResponse: The response from the service to which the request was forwarded.

    Raises:
    HTTPException: If there is an error while making the request or processing the response.
    """
    async with httpx.AsyncClient() as client:
        try:
            response: Response = await client.request(
                method=request.method,
                url=f"{service_url}{request.url.path}",
                json=(
                    await request.json()
                    if request.method in ["POST", "PUT", "PATCH"]
                    else None
                ),
            )

            return JSONResponse(
                status_code=response.status_code, content=response.json()
            )

        except httpx.HTTPStatusError as exc_info:
            print(f"error: {exc_info.response.text}")
            raise HTTPException(
                status_code=exc_info.response.status_code, detail=exc_info.response.text
            )
        except httpx.RequestError as exc_info:
            print(f"error while requesting url: {exc_info.request.url}")
            print(f"error message: {exc_info}")
            raise HTTPException(
                status_code=500, detail="Internal server error while proxyng"
            )
        except Exception as e:
            print(f"error: {str(e)}")
            raise HTTPException(status_code=500, detail=str(e))


@app.get("/products")
@app.post("/products")
async def proxy_products(request: Request) -> JSONResponse:
    """
    This function acts as a proxy for product-related requests.

    Parameters:
    request (Request): The incoming request to be forwarded.

    Returns:
    JSONResponse: The response from the product service.
    """
    return await proxy(request=request, service_url="http://product-service:8001")


@app.get("/product/{product_id}")
@app.put("/product/{product_id}")
@app.delete("/product/{product_id}")
async def proxy_product(request: Request) -> JSONResponse:
    """
    This function acts as a proxy for specific product-related requests.

    Parameters:
    request (Request): The incoming request to be forwarded.

    Returns:
    JSONResponse: The response from the product service.
    """
    return await proxy(request=request, service_url="http://product-service:8001")


@app.get("/stock/{product_id}")
@app.put("/stock/{stock_id}")
async def proxy_stock(request: Request) -> JSONResponse:
    """
    This function acts as a proxy for stock-related requests.

    Parameters:
    request (Request): The incoming request to be forwarded.

    Returns:
    JSONResponse: The response from the stock service.
    """
    return await proxy(request=request, service_url="http://stock-service:8002")
