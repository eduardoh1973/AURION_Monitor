from telethon import TelegramClient
import asyncio
from src import config

async def _enviar(mensaje):
    client = TelegramClient('AURION_session', config.API_ID, config.API_HASH)
    await client.start(phone=config.PHONE_NUMBER)
    await client.send_message('me', mensaje) # Envía el mensaje a tu chat guardado
    await client.disconnect()

def enviar_mensaje_telegram(mensaje):
    asyncio.run(_enviar(mensaje))