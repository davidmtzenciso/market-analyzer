from django.urls import path
from .views import StockViewSet

urlpatterns = [
    path('avrg', StockViewSet.as_view())
]