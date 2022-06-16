from django.urls import path
from .views import StockViewSet

urlpatterns = [
    path('today', StockViewSet.as_view())
]