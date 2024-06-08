FROM python:3.9-slim

WORKDIR /app

COPY ./app /app

RUN pip install --no-cache-dir fastapi uvicorn httpx

CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
