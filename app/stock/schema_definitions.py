from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

# Define response schema directly without using serializers
stock_recommendation_schema = swagger_auto_schema(
    operation_description="Get stock recommendation based on RSI value.",
    manual_parameters=[
        openapi.Parameter('ticker', openapi.IN_PATH, description="Stock ticker symbol", type=openapi.TYPE_STRING)
    ],
    responses={
        200: openapi.Response(
            description="Successful response with stock recommendation",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'ticker': openapi.Schema(type=openapi.TYPE_STRING, description='Stock ticker symbol'),
                    'recommendation': openapi.Schema(type=openapi.TYPE_STRING, description='Recommended action based on RSI'),
                    'message': openapi.Schema(type=openapi.TYPE_STRING, description='Message behind the recommendation'),
                    'date': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATE, description='Date of the recommendation'),
                }
            )
        ),
        404: openapi.Response(
            description="RSI data not found",
            examples={
                'application/json': {
                    'error': 'RSI data not found'
                }
            }
        )
    }
)
