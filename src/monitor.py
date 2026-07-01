import json
import time
import logging
from src.agente import evaluar_evento
from src.tools.telegram_bot import enviar_mensaje_telegram
from src.email_manager import enviar_email
from src.tools.search_tool import buscar_eventos

# Configuración de logs
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def cargar_configuracion():
    try:
        with open('data/user_config.json', 'r') as f:
            return json.load(f).get("preferencias", {})
    except FileNotFoundError:
        logging.error("Archivo de configuración no encontrado.")
        return {}

def monitorizar():
    logging.info("Iniciando ciclo de observación...")
    config = cargar_configuracion()
    
    if not config:
        return

    # Obtención de eventos
    eventos = buscar_eventos()
    
    for evento in eventos:
        resultado = evaluar_evento(evento, config)
        
        if resultado.get("relevante"):
            logging.info(f"¡Evento relevante detectado!: {resultado.get('nombre', 'Evento')}")
            
            # Extracción de datos del JSON devuelto por la IA
            nombre = resultado.get('nombre', 'No especificado')
            fecha = resultado.get('fecha', 'No especificada')
            lugar = resultado.get('lugar', 'No especificado')
            pais = resultado.get('pais', 'No especificado')
            detalle = resultado.get('detalle_especifico', 'No especificado')
            precio = resultado.get('precio', 'Consultar')
            
            # Construcción del mensaje con los detalles enriquecidos
            mensaje = (f"🔔 AURION: Nueva oportunidad!\n"
                       f"🎟 Evento: {nombre}\n"
                       f"📅 Fecha: {fecha}\n"
                       f"📍 Ubicación: {lugar}, {pais}\n"
                       f"🔥 Detalle: {detalle}\n"
                       f"💰 Precio: {precio}€")
            
            enviar_mensaje_telegram(mensaje)
            enviar_email(mensaje)
        else:
            logging.info(f"Evento descartado: {evento.get('nombre', 'Desconocido')}")

if __name__ == "__main__":
    # Ya no usamos el 'while True' porque GitHub Actions 
    # dispara este script cada vez que se cumple la hora.
    try:
        monitorizar()
    except Exception as e:
        logging.error(f"Error fatal: {e}")
        exit(1) # Esto avisa a GitHub que algo salió mal