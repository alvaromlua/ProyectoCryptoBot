from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

BINANCE_API_URL = "https://api.binance.com"

LISTA_COINS = [
    "BNBUSDT",
    "BTCUSDT",
    "ETHUSDT",
    "SOLUSDT",
    "WBTCUSDT",
]

## Sí funciona
@app.route('/get_crypto_price', methods=['GET'])
def get_crypto_price():
    
    # Obtén el símbolo de la criptomoneda de los parámetros de la consulta
    symbol = request.args.get('symbol', default='BTCUSDT', type=str)

    
    # Construye la consulta para el endpoint de la API de Binance
    response = requests.get(f"{BINANCE_API_URL}/api/v3/ticker/price?symbol={symbol}")

    # Verifica que la respuesta desde Binance sea exitosa
    if response.status_code == 200:
        # Retorna la respuesta en formato JSON
        return jsonify(response.json()), 200
    else:
        # En caso de error, retorna un mensaje de error
        return jsonify({"error": "Error al obtener la información de la criptomoneda"}), response.status_code


if __name__ == '__main__':
    # Ejecuta la aplicación en el puerto 5000
    app.run(port=5000)
