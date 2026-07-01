import time
import os
import logging
from dotenv import load_dotenv

# Importaciones de tus herramientas
from src.tools.search_tool import buscar_eventos
from src.tools.telegram_bot import enviar_mensaje_telegram
from src.email_manager import enviar_email
from src.utils.guardrails import es_evento_valido
from src.utils.ai_analyzer import es_evento_relevante_ia

# Cargar variables de entorno (.env)
load_dotenv()

# Configuración de logs
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def ya_notificado(evento_id):
    if not os.path.exists('data/historial.txt'):
        return False
    with open('data/historial.txt', 'r') as f:
        return str(evento_id) in f.read().splitlines()

def marcar_como_notificado(evento_id):
    with open('data/historial.txt', 'a') as f:
        f.write(f"{evento_id}\n")

def monitorizar():
    logging.info("AURION: Iniciando ciclo de observación...")
    
    # 1. Fase de Observación
    eventos = buscar_eventos()
    
    # Preferencias para la IA (esto podrías moverlo a un archivo de configuración)
    preferencias_usuario = "Me gusta el rock, el arte moderno y odio el fútbol."
    
    for evento in eventos:
        e_id = evento.get("id", evento.get("nombre"))
        
        # 2. Fase de Razonamiento (Filtro técnico + Filtro IA)
        if es_evento_valido(evento):
            if not ya_notificado(e_id):
                
                # Análisis de relevancia por IA (Groq)
                if es_evento_relevante_ia(evento, preferencias_usuario):
                    logging.info(f"¡Evento relevante detectado!: {evento['nombre']}")
                    
                    # 3. Fase de Acción
                    mensaje = f"AURION ha detectado una oportunidad: {evento['nombre']} a {evento['precio']}€."
                    
                    enviar_mensaje_telegram(mensaje)
                    enviar_email() 
                    
                    marcar_como_notificado(e_id)
                    logging.info("Notificación enviada y registrado en memoria.")
                else:
                    logging.info(f"Evento {evento['nombre']} descartado por la IA (No relevante).")
            else:
                logging.debug(f"Evento {evento['nombre']} ya notificado.")
        else:
            logging.info(f"Evento {evento.get('nombre')} descartado por guardrails técnicos.")

    logging.info("AURION: Ciclo completado. Esperando 60 segundos...")

if __name__ == "__main__":
    while True:
        try:
            monitorizar()
        except Exception as e:
            logging.error(f"Error crítico en el bucle: {e}")
        time.sleep(60)