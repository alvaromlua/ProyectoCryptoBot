from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

BINANCE_API_URL = "https://api.binance.com"



## Sí funciona
@app.route('/get_crypto_price', methods=['GET'])
def get_crypto_price():
    
    _subURL= 'api/v3/ticker/tradingDay'


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



## aun no funciona
@app.route('/get_multi_crypto_prices', methods=['GET'])
def get_multi_crypto_prices():
    symbols = request.args.get('symbols')

    if symbols:
        # Se están pasando varios símbolos, necesitamos formatearlos como un arreglo JSON.
        symbols_list = symbols.split(',')
        params = {'symbols': str(symbols_list).replace("'", '"')}  # JSON array as string
    else:
        # Si no se pasan símbolos, se usa un símbolo por defecto.
        params = {'symbol': 'BTCUSDT'}

    response = requests.get(f"{BINANCE_API_URL}/api/v3/ticker/price", params=params)

    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({"error": "Error al obtener la información de las criptomonedas"}), response.status_code

## aun no funciona
@app.route('/get_crypto_price_day', methods=['GET'])
def get_crypto_price_day():
    
    # Obtén el símbolo de la criptomoneda de los parámetros de la consulta
    symbol = request.args.get('symbol', default='BTCUSDT', type=str)

    
    # Construye la consulta para el endpoint de la API de Binance
    response = requests.get(f"{BINANCE_API_URL}api/v3/ticker/tradingDay?symbol={symbol}")

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
