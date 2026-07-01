import logging
import os
from dotenv import load_dotenv
from src.monitor import monitorizar

# 1. Carga las variables del archivo .env (solo para desarrollo local)
# En GitHub Actions, estas variables se inyectan directamente al entorno,
# por lo que load_dotenv() simplemente no encontrará el archivo y no pasará nada (es seguro).
load_dotenv()

# 2. Configuración del Logging Estructurado
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)

def verificar_configuracion():
    """
    Verifica que las variables críticas existan. 
    Esto evita que el script falle a mitad del proceso si falta un token.
    """
    claves_necesarias = ["GROQ_API_KEY"]
    for clave in claves_necesarias:
        if not os.getenv(clave):
            logging.warning(f"La variable de entorno {clave} no está configurada.")

def main():
    logging.info("--- AURION Monitor: Iniciando ciclo de barrido ---")
    
    # Verificamos credenciales antes de empezar
    verificar_configuracion()
    
    try:
        # Ejecutamos la monitorización.
        # Asumimos que tu función 'monitorizar' dentro de src.monitor 
        # ya está preparada para recoger las variables de entorno mediante os.getenv()
        monitorizar()
        
        logging.info("--- AURION Monitor: Ciclo finalizado con éxito ---")
        
    except Exception as e:
        # Capturamos el error detallado para verlo en los logs de GitHub Actions
        logging.error(f"Error crítico durante el ciclo de monitorización: {e}", exc_info=True)
        # Salimos con código 1 para que el workflow de GitHub marque el proceso como fallido
        exit(1)

if __name__ == "__main__":
    main()