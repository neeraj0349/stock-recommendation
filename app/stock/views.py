from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .schema_definitions import stock_recommendation_schema
from .services import PolygonService

polygon_service = PolygonService()


class StockRecommendationView(APIView):

    @stock_recommendation_schema
    def get(self, request, ticker):
        """
        Handles GET requests to fetch stock recommendations based on RSI data.

        Input:
        - request (HttpRequest): The HTTP request object.
        - ticker (str): The stock ticker symbol from the URL path.

        Output:
        - Response: :
            - Recommendation data (dict) with the stock ticker, recommendation, message, and current date if RSI data is available.
            - Error message (dict) with an 'error' key if RSI data is not found.
        """
        ticker = ticker.upper()
        rsi_value = polygon_service.get_rsi_data(ticker)
        if rsi_value:
            recommendation = polygon_service.generate_recommendation(ticker, rsi_value)
            return Response(recommendation, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'RSI data not found'}, status=status.HTTP_404_NOT_FOUND)
