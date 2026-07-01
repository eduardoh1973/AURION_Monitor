import os
from groq import Groq
from dotenv import load_dotenv

# Carga las variables de entorno
load_dotenv()

def get_client():
    """Inicializa el cliente de Groq buscando la API KEY en el entorno."""
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("La variable de entorno GROQ_API_KEY no está configurada.")
    return Groq(api_key=api_key)

def es_evento_relevante_ia(evento, preferencias_usuario):
    """
    Analiza un evento usando el modelo llama-3.3-70b-versatile.
    """
    client = get_client()
    
    # Prompt optimizado para ser directo y eficiente
    prompt = f"""
    Eres un asistente personal experto. Analiza si el evento cumple con las preferencias del usuario.
    Evento: {evento}
    Preferencias del usuario: {preferencias_usuario}
    
    Responde solo 'SI' si es relevante o 'NO' si no lo es. No incluyas explicaciones.
    """
    
    try:
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile", # Modelo actualizado
            temperature=0.1 # Muy baja temperatura para evitar alucinaciones
        )
        
        respuesta = chat_completion.choices[0].message.content.strip().upper()
        return "SI" in respuesta
        
    except Exception as e:
        print(f"Error en la llamada a la IA: {e}")
        return False