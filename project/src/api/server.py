from typing import Optional

from fastapi import Depends, FastAPI, Request, Response
from sqlalchemy.orm import Session

from ..db.session import SessionLocal
from ..scraper import SUPPORTED_SCRAPERS
from .crud import get_client_product
from .schemas import ResponseSchema, ScraperSchema

app = FastAPI()


# The middleware will create a new SQLAlchemy SessionLocal for each request,
# add it to the request and then close it once the request is finished.
# https://fastapi.tiangolo.com/tutorial/sql-databases/#__tabbed_2_1
@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


# Dependency
def get_db(request: Request):
    return request.state.db


@app.get("/health")
async def health_check():
    """
    # Health check endpoint.
    """
    return {
        "message": "API is running",
        "supported_scrapers": SUPPORTED_SCRAPERS,
    }


@app.get("/data/{scraper_name}", response_model=ResponseSchema | dict)
async def get_data(
    scraper_name: str,
    db: Session = Depends(get_db),
    page: Optional[int] = 0,
    size: Optional[int] = 10,
):
    scraper_name = scraper_name.lower()

    if scraper_name not in SUPPORTED_SCRAPERS:
        return {"error": f"Unsupported scraper name: {scraper_name}"}

    client_products, metadata = get_client_product(
        db, client_name=scraper_name, page=page, size=size
    )

    return {"items": client_products.items, "metadata": metadata}
