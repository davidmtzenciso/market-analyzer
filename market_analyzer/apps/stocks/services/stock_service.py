import requests
import json


class StockService:
    def __init__(self):
        self.url = 'https://api.polygon.io/v1/open-close/{}/{}?adjusted=true&apiKey={}'
        self.apiKey = "AgS3US1ZxCt9srKb609DtZRKnEfXGdFI"

    def retriveTodaysData(self, stock):
        today = '2022-06-14'
        response = requests.get(f"{self.url.format(stock, today, self.apiKey)}")
        data = response.json()
        return data


