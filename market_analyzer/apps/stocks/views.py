from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .services.stock_service import StockService;

class StockViewSet(APIView):
    def __init__(self):
        self.stockService = StockService()

    def get(self, request):
        ticker = request.query_params.get('ticker')
        date = request.query_params.get('date')
        data = self.stockService.getStockDayStats(ticker, date)
        return Response({"status": "success", "data": data}, status=status.HTTP_200_OK)