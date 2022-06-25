import requests
from apps.util.services.stats_service import StatsService

class StockService:
    def __init__(self):
        self.url = 'https://api.polygon.io/v2/aggs/ticker/{}/range/1/hour/{}/{}?adjusted=true&sort=asc&limit=120&apiKey={}'
        self.apiKey = "AgS3US1ZxCt9srKb609DtZRKnEfXGdFI"
        self.statsService = StatsService()

    def getStockDayStats(self, ticker, fromDate, toDate):
        response = requests.get(f"{self.url.format(ticker, fromDate, toDate, self.apiKey)}")
        data = response.json()
        return {
            "ticker" : data.ticker,
            "data":  self.statsService.getStockAverages(data["results"]) if data.resultsCount > 0 else []
        }
    