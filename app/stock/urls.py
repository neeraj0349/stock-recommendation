from django.urls import path

from stock.views import StockRecommendationView

urlpatterns = [
    path('recommendation/<str:ticker>/', StockRecommendationView.as_view(), name='stock_recommendation'),
]
