from decouple import config


API_KEY = config('API_KEY')

SECRET_KEY = config('SECRET_KEY')

DATABASE_CONNECTION = {
    "db_host": "localhost",
    "db_port": 5432,
    "db_name": "postgres",
    "db_user": "postgres",
    "db_password": "1234"
}

WSS_URL = "wss://stream.binance.com:9443/stream?streams=ethusdt@kline_1m"
HTTPS_URL = "https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT"

