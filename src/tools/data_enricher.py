from groq import Groq
import json
import os

def extraer_datos_evento(texto_evento):
    """Extrae fecha, lugar y precio usando la IA."""
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    
    prompt = f"""
    Extrae la información del siguiente evento y devuélvela en formato JSON estricto:
    {{
        "fecha": "YYYY-MM-DD",
        "lugar": "Nombre del sitio",
        "precio": "Solo el número",
        "link": "URL si existe, sino null"
    }}
    Evento: {texto_evento}
    """
    
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.3-70b-versatile",
        temperature=0.0
    )
    
    try:
        # Limpiamos la respuesta para asegurar que sea JSON
        content = response.choices[0].message.content
        return json.loads(content.replace("```json", "").replace("```", ""))
    except:
        return None