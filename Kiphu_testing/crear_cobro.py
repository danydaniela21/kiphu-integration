import requests
import json


API_KEY = 'API_KEY_AQUI'
RECEIVER_ID = 'RECEIVER_ID_AQUI'

url = 'https://payment-api.khipu.com/v3/payments'

headers = {
    'x-api-key': API_KEY,
    'Content-Type': 'application/json'
}

data = {
    "receiver_id": RECEIVER_ID,
    "subject": "Pago de prueba Khipu",
    "amount": 100,
    "currency": "CLP",
    "transaction_id": "pedido-123456",
    "payer_email": "cliente@correo.com",
    "return_url": "https://tusitio.com/exito",
    "cancel_url": "https://tusitio.com/cancelado",
    "notify_url": "https://tusitio.com/webhook",
    "custom": "Este es un pago de prueba",
    "body": "Gracias por tu compra :)"
}

response = requests.post(url, headers=headers, json=data)

print("Código de estado HTTP:", response.status_code)

respuesta = response.json()
print("Respuesta formateada:")
print(json.dumps(respuesta, indent=4, ensure_ascii=False))
