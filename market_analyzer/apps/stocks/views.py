from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .services.stock_service import StockService;

class StockViewSet(APIView):
    def __init__(self):
        self.stockService = StockService()

    def get(self, request):
        data = self.stockService.retriveTodaysData('TSLA')
        return Response({"status": "success", "data": data}, status=status.HTTP_200_OK)