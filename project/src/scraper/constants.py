from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent.parent.parent

# https://geckodriver.com/download/
GECKO_DRIVER_PATH = ROOT_DIR / "geckodriver"
CHROMEDRIVER_PATH = ROOT_DIR / "chromedriver"
