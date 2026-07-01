import logging
import os
from src.monitor import monitorizar

# 1. Configuración del Logging Estructurado (Fase 5)
# Esto guardará un registro de qué hace el agente cada vez que se ejecuta
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    # Nota: En GitHub Actions, los logs se ven en la pestaña "Actions"
    # pero puedes imprimir a consola para que queden registrados allí.
    handlers=[
        logging.StreamHandler() 
    ]
)

def main():
    logging.info("--- AURION Monitor: Iniciando ciclo de barrido ---")
    
    try:
        # Ejecutamos la monitorización una sola vez.
        # GitHub Actions se encargará de volver a disparar este script cada hora.
        monitorizar()
        logging.info("--- AURION Monitor: Ciclo finalizado con éxito ---")
        
    except Exception as e:
        # Captura cualquier error para que el log te diga qué falló
        logging.error(f"Error crítico durante el ciclo de monitorización: {e}")
        # Finalizamos con un código de error para que GitHub detecte el fallo
        exit(1)

if __name__ == "__main__":
    main()