import requests
import json

API_KEY = 'API_KEY_AQUI'
PAYMENT_ID = 'zozk2gw4fasd' # Mi payment ID

url = f"https://payment-api.khipu.com/v3/payments/{PAYMENT_ID}"

headers = {
    'x-api-key': API_KEY
}

response = requests.get(url, headers=headers)

print("Código de estado:", response.status_code)

respuesta = response.json()
print("Respuesta formateada:")
print(json.dumps(respuesta, indent=4, ensure_ascii=False))

