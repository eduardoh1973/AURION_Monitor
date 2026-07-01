import requests
from config import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID

def enviar_mensaje_prueba():
    # Usamos TELEGRAM_TOKEN tal como está en tu config.py
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": "¡Hola Eduardo! AURION Monitor está operativo y conectado correctamente. ✅"
    }
    
    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()
        print("✅ Mensaje enviado correctamente a Telegram.")
    except Exception as e:
        print(f"❌ Error al enviar el mensaje: {e}")

if __name__ == "__main__":
    enviar_mensaje_prueba()