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

@app.route('/', methods=['GET', 'POST'])
def home():
    return "Hola soy CryptoBot!",200


@app.route('/ListaCryptos', methods=['GET'])
def listaCryptos():
    return jsonify(
        {
            'fulfillment_response': {
                'messages': [
                    {
                        'text': {
                            'text': ['Bitcoin, BNB, Ethereum']
                        }
                    }
                ]
            }
        }
    )
    
@app.route('/get_crypto_price', methods=['GET'])
def get_crypto_price():
    symbol = request.args.get('symbol', default='BTCUSDT', type=str)
    binance_url = f"{BINANCE_API_URL}/api/v3/ticker/price?symbol={symbol}"

    response = requests.get(binance_url)

    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        # Imprimimos el código de estado y el cuerpo de la respuesta para depuración
        print("Error Code:", response.status_code)
        try:
            print("Error Body:", response.json())  # Intentamos imprimir el cuerpo del error como JSON
        except ValueError:  # En caso de que no sea JSON, lo imprimiremos como texto plano
            print("Error Body:", response.text)
        return jsonify({"error": "Error al obtener la información de la criptomoneda"}), response.status_code

if __name__ == '__main__':
    app.run(port=5000)
