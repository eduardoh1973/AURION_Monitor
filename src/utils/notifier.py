import smtplib
import requests
import os
from email.message import EmailMessage

def enviar_notificacion(evento):
    """Envía la notificación por Email y Telegram usando variables de entorno."""
    
    # 1. Obtenemos credenciales desde las variables de entorno (locales o GitHub Secrets)
    EMAIL_USER = os.getenv("EMAIL_USER")
    EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
    EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
    TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

    mensaje = (
        f"¡NUEVO EVENTO RELEVANTE!\n"
        f"📍 Lugar: {evento.get('lugar', 'No especificado')}\n"
        f"📅 Fecha: {evento.get('fecha', 'No especificada')}\n"
        f"💰 Precio: {evento.get('precio', 'N/A')}€\n"
        f"🔗 Link: {evento.get('link', 'No disponible')}"
    )

    # 2. Enviar Email
    if EMAIL_USER and EMAIL_PASSWORD:
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

    # 3. Enviar Telegram
    if TELEGRAM_TOKEN and TELEGRAM_CHAT_ID:
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