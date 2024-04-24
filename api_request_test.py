import requests

BASE_URL = 'http://127.0.0.1:5000/ListaCryptos'
#BASE_URL = 'https://cryptobot-api.onrender.com/get_crypto_price'
#BASE_URL = 'https://proyectocryptobot.onrender.com/ListaCryptos'

#params = {"symbol":"BNBUSDT"}

response = requests.get(BASE_URL)

print (response.json())