import logging

def buscar_eventos():
    """
    Herramienta de búsqueda de eventos.
    Devuelve una lista de diccionarios, cada uno con los campos necesarios 
    para el análisis del agente.
    """
    logging.info("Iniciando búsqueda de eventos...")
    
    # Esta es la estructura de datos que espera tu sistema
    # En el futuro, aquí sustituiremos esta lista por la lógica de scraping (ej. BeautifulSoup)
    eventos_simulados = [
        {
            "id": "evento_001", 
            "nombre": "Concierto de Rock", 
            "precio": 85.00
        },
        {
            "id": "evento_002", 
            "nombre": "Partido de Fútbol", 
            "precio": 150.00
        },
        {
            "id": "evento_003", 
            "nombre": "Exposición de Arte", 
            "precio": 20.00
        }
    ]
    
    return eventos_simulados

if __name__ == "__main__":
    # Prueba rápida si ejecutas el script directamente
    datos = buscar_eventos()
    for e in datos:
        print(f"Evento encontrado: {e['nombre']} - Precio: {e['precio']}€")