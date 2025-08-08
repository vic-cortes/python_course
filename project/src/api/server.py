from fastapi import FastAPI

from ..scraper import SUPPORTED_SCRAPERS
from ..scraper.constants import DATA_PATH

app = FastAPI()


@app.get("/health")
async def health_check():
    return {
        "message": "API is running",
        "supported_scrapers": SUPPORTED_SCRAPERS,
    }


@app.get("/data/{script_name}")
async def get_data(script_name: str):
    script_name = script_name.lower()

    if script_name not in SUPPORTED_SCRAPERS:
        return {"error": "Unsupported scraper"}

    data_path = DATA_PATH / script_name

    data_files = list(data_path.glob("*.json"))
    if not data_files:
        return {"error": "No data files found"}
