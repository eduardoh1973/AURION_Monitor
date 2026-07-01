import sys
import os
import asyncio
from telethon import TelegramClient

# Esto asegura que pueda encontrar el config.py aunque esté en la carpeta de al lado
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import config

async def main():
    # Creamos el cliente
    client = TelegramClient('AURION_session', config.API_ID, config.API_HASH)
    
    print("Iniciando conexión con Telegram...")
    await client.start(phone=config.PHONE_NUMBER)
    
    print("¡Conexión exitosa!")
    
    # Obtenemos info del usuario para verificar que funciona
    me = await client.get_me()
    print(f"Sesión iniciada correctamente como: {me.first_name}")
    
    await client.disconnect()

if __name__ == '__main__':
    asyncio.run(main())