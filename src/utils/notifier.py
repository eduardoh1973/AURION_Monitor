import smtplib
import requests
from email.message import EmailMessage
# Importamos tus credenciales desde tu archivo config.py
from src.utils.config import EMAIL_USER, EMAIL_PASSWORD, EMAIL_RECEIVER

# --- CONFIGURACIÓN TELEGRAM ---
# Añade esto a tu config.py o defínelo aquí
TELEGRAM_TOKEN = "TU_TOKEN_AQUI" 
TELEGRAM_CHAT_ID = "TU_ID_NUMERICO_AQUI"

def enviar_notificacion(evento):
    """Envía la notificación por Email y Telegram."""
    mensaje = (
        f"¡NUEVO EVENTO RELEVANTE!\n"
        f"📍 Lugar: {evento.get('lugar', 'No especificado')}\n"
        f"📅 Fecha: {evento.get('fecha', 'No especificada')}\n"
        f"💰 Precio: {evento.get('precio', 'N/A')}€\n"
        f"🔗 Link: {evento.get('link', 'No disponible')}"
    )

    # 1. Enviar Email
    try:
        msg = EmailMessage()
        msg['Subject'] = f"AURION: {evento.get('lugar', 'Nuevo Evento')}"
        msg['From'] = EMAIL_USER
        msg['To'] = EMAIL_RECEIVER
        msg.set_content(mensaje)
        
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_USER, EMAIL_PASSWORD)
            smtp.send_message(msg)
        print("✅ Email enviado correctamente.")
    except Exception as e:
        print(f"❌ Error al enviar email: {e}")

    # 2. Enviar Telegram
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        params = {"chat_id": TELEGRAM_CHAT_ID, "text": mensaje}
        response = requests.post(url, data=params)
        if response.status_code == 200:
            print("🤖 Notificación de Telegram enviada.")
        else:
            print(f"❌ Error en Telegram: {response.text}")
    except Exception as e:
        print(f"❌ Error al conectar con Telegram: {e}")

    return True