from datetime import date
from django.core.cache import cache
from polygon import RESTClient


class PolygonService:
    def __init__(self):
        self.client = RESTClient()

    def get_rsi_data(self, ticker):
        """
        Fetches the RSI data for a given stock ticker.

        Input:
        - ticker (str): The stock ticker symbol (e.g., 'AAPL').

        Output:
        - float or None: The latest RSI value for the stock if available, otherwise None.
        """
        # Generate a cache key based on the stock ticker
        cache_key = f'rsi_data_{ticker}'
        cached_rsi = cache.get(cache_key)

        if cached_rsi:
            return cached_rsi
        try:
            rsi_data = self.client.get_rsi(ticker)
            print(rsi_data, "data")
            if rsi_data and hasattr(rsi_data, 'values') and len(rsi_data.values) > 0:
                # Extract the latest RSI value
                latest_rsi = rsi_data.values[0].value
                cache.set(cache_key, latest_rsi, timeout=900)  # Cache for 15 minutes
                return latest_rsi
            return None
        except Exception as e:
            print(f"Error fetching RSI data for {ticker}: {e}")
            return None

    def generate_recommendation(self, ticker, rsi_value):
        """
        Generates a stock recommendation based on the RSI value.

        Input:
        - ticker (str): The stock ticker symbol (e.g., 'AAPL').
        - rsi_value (float): The RSI value for the stock.

        Output:
        - dict: A dictionary containing:
            - 'ticker' (str): The stock ticker symbol.
            - 'recommendation' (str): The recommendation ('BUY', 'SELL', or 'HOLD').
            - 'message' (str): The message for the recommendation.
            - 'date' (str): The current date in ISO format.
        """

        if rsi_value is not None:
            if rsi_value < 30:
                recommendation = 'BUY'
                message = 'RSI indicates the stock is oversold.'
            elif rsi_value > 70:
                recommendation = 'SELL'
                message = 'RSI indicates the stock is overbought.'
            else:
                recommendation = 'HOLD'
                message = 'RSI indicates the stock is neither overbought nor oversold.'
        else:
            recommendation = 'HOLD'
            message = 'RSI data not available, defaulting to HOLD.'

        return {
            'ticker': ticker,
            'recommendation': recommendation,
            'message': message,
            'date': date.today().isoformat()
        }
