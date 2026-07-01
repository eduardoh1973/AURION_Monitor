from email.message import EmailMessage
import smtplib
from src.config import EMAIL_USER, EMAIL_PASSWORD, EMAIL_RECEIVER

def enviar_email(asunto, cuerpo):
    msg = EmailMessage()
    msg.set_content(cuerpo)
    msg['Subject'] = asunto
    msg['From'] = EMAIL_USER
    msg['To'] = EMAIL_RECEIVER

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_USER, EMAIL_PASSWORD)
        smtp.send_message(msg)