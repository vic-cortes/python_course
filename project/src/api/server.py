import json

from fastapi import FastAPI

from ..scraper import SUPPORTED_SCRAPERS
from ..scraper.constants import DATA_PATH

app = FastAPI()


@app.get("/health")
async def health_check():
    """
    # Health check endpoint.
    """
    return {
        "message": "API is running",
        "supported_scrapers": SUPPORTED_SCRAPERS,
    }


@app.get("/data/{scraper_name}")
async def get_data(scraper_name: str):
    scraper_name = scraper_name.lower()

    if scraper_name not in SUPPORTED_SCRAPERS:
        return {"error": "Unsupported scraper"}

    data_path = DATA_PATH / scraper_name

    data_files = list(data_path.glob("*.json"))
    if not data_files:
        return {"error": "No data files found"}

    # Read each json file and return its content
    data_contents = []
    for file in data_files:
        with open(file, "r") as f:
            json_data = json.load(f)
            data_contents.append(json_data)

    return {"data": data_contents, "status": "success"}
