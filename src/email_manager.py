import smtplib
from email.message import EmailMessage
from src.config import EMAIL_USER, EMAIL_PASSWORD, EMAIL_RECEIVER

def enviar_email(contenido_mensaje):
    """
    Envía un email con el contenido del mensaje recibido.
    """
    msg = EmailMessage()
    msg.set_content(contenido_mensaje) # Usamos el mensaje que le pasamos desde monitor.py
    msg['Subject'] = "🔔 AURION: Nueva oportunidad detectada"
    msg['From'] = EMAIL_USER
    msg['To'] = EMAIL_RECEIVER

    try:
        # Conexión con los servidores de Gmail
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_USER, EMAIL_PASSWORD)
            smtp.send_message(msg)
        print("Email enviado correctamente.")
    except Exception as e:
        print(f"Error al enviar email: {e}")

if __name__ == '__main__':
    # Esta parte es solo para probar el envío manualmente
    enviar_email("Esta es una prueba de envío desde el módulo de email.")