# Stock Recommendation API

## Getting Started

### Dependencies
- **Docker**: See [Get Docker](https://docs.docker.com/get-docker/)
- **Docker Compose**: Installed with Docker Desktop, See [Install Docker Compose](https://docs.docker.com/compose/install/)
- **Polygon.io API Key**: Required for fetching stock data. Replace  in the  class with your actual API key.

### Running the Project
1. **Start the Services**:
   With Docker and Docker Compose installed, run the following command to start the project:
   ```bash
   docker-compose up --build
   ```
   This command will pull the required Docker images, build the Django application, and start the services. Your API will be accessible at [http://localhost:8000](http://localhost:8000).

2. **Stopping the Services**:
   To stop the services, press `Ctrl+C` in the terminal where Docker Compose is running.

### API Overview
This project provides a simple API for stock recommendations based on the Relative Strength Index (RSI) using the Polygon.io Stocks API.

#### Available Endpoints
- **GET /api/recommendation/{ticker}/**
  - **Description**: Fetches stock recommendations based on the RSI value for the provided ticker symbol.
  - **Parameters**:
    - `ticker` (str): The stock ticker symbol (e.g., 'AAPL').
  - **Response**:
    - **Success (200 OK)**: Returns a JSON object with the recommendation, message, ticker, and current date.
    - **Error (404 NOT FOUND)**: Returns a JSON object with an error message if RSI data is not found.

#### Example Request
```http
GET /api/recommendation/AAPL/
```

#### Example Response
**Success (200 OK)**:
```json
{
  "ticker": "AAPL",
  "recommendation": "HOLD",
  "message": "RSI indicates the stock is neither overbought nor oversold.",
  "date": "2024-07-26"
}
```

**Error (404 NOT FOUND)**:
```json
{
  "error": "RSI data not found"
}
```

### Caching
RSI data is cached using Redis for 15 minutes to improve performance and reduce API calls.

### Project Details
- **Problem Statement**: The API provides stock recommendations based on the RSI value, helping users decide whether to buy, sell, or hold a stock.
- **Integration**: Integrates with Polygon.io for fetching stock data and uses Django for API implementation.
- **Database**: PostgreSQL is included but not directly involved in the stock recommendation logic.
- **Caching**: Redis is used for caching RSI data.

### Additional Information
- **Redis**: Ensure Redis is running and configured in your  file.
- **Polygon.io API**: Ensure you replace  with your actual API key in the  class.

### Documentation
- **Swagger UI**: [http://localhost:8000/swagger/](http://localhost:8000/swagger/)
- **ReDoc UI**: [http://localhost:8000/redoc/](http://localhost:8000/redoc/)

