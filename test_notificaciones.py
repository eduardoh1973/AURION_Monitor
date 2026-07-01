from src.tools.telegram_bot import enviar_mensaje_telegram
from src.email_manager import enviar_email

print("Probando notificaciones...")

try:
    enviar_mensaje_telegram("Test de AURION: Sistema operativo y conectado.")
    print("Telegram: OK")
except Exception as e:
    print(f"Telegram falló: {e}")

try:
    enviar_email()
    print("Email: OK")
except Exception as e:
    print(f"Email falló: {e}")