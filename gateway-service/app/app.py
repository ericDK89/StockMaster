from fastapi import FastAPI, Request, HTTPException, Response
from fastapi.responses import JSONResponse
import httpx

app = FastAPI()


async def proxy(request: Request, service_url: str) -> JSONResponse:
    async with httpx.AsyncClient() as client:
        try:
            response: Response = await client.request(
                method=request.method,
                url=f"{service_url}{request.url.path}",
                json=(
                    await request.json() if request.method in ["POST", "PUT"] else None
                ),
            )

            return JSONResponse(
                status_code=response.status_code, content=response.json()
            )

        except httpx.HTTPStatusError as exc_info:
            raise HTTPException(
                status_code=exc_info.response.status_code, detail=exc_info.response.text
            )


@app.get("/products")
@app.post("/products")
async def proxy_products(request: Request) -> JSONResponse:
    return await proxy(request=request, service_url="http://product-service:8001")


@app.get("/product/{product_id}")
@app.put("/product/{product_id}")
@app.delete("/product/{product_id}")
async def proxy_product(request: Request) -> JSONResponse:
    return await proxy(request=request, service_url="http://product-service:8001")
