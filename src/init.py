from src.config import settings
from src.http_client import CMCHTTPClient

cmc_client = CMCHTTPClient(
    base_url="https://pro-api.coinmarketcap.com",
    api_key=settings.CMC_API_KEY,  # Assuming settings.CMC_API_KEY is defined in config.py and loaded in main.py
)