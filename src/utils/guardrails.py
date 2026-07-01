def es_evento_valido(evento):
    """
    Verifica que el evento cumpla con las restricciones de seguridad.
    """
    # 1. No permite compras automáticas (Límite: el agente solo informa)
    # 2. No permite procesar eventos con datos incompletos
    if not evento.get("nombre") or not evento.get("precio"):
        return False
        
    # 3. Control de relevancia básica
    if evento.get("precio", 0) > 1000:  # Ejemplo de guardrail de precio máximo
        return False
        
    return True