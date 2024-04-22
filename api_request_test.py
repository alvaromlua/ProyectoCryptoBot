import requests

#BASE_URL = 'http://127.0.0.1:5000/get_crypto_price'
BASE_URL = 'https://cryptobot-api.onrender.com/get_crypto_price'

params = {"symbol":"BNBUSDT"}

response = requests.get(BASE_URL, params=params)

print (response.json())