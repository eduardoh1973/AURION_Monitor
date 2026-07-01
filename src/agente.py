import json
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def evaluar_evento(evento, config):
    pais = config.get('pais', 'Todas')
    provincia = config.get('provincia', 'Todas')

    prompt = f"""
    Eres un analista de datos. Analiza el siguiente evento: {evento}
    
    Tus reglas:
    1. Filtro: Si país/provincia no son 'Todas', el evento DEBE coincidir.
    2. Detalle: Debes identificar el protagonista (equipo de fútbol, artista, autor).
    
    Devuelve estrictamente un JSON con este formato:
    {{"relevante": true, "nombre": "{evento.get('nombre')}", "fecha": "2026-07-01", "lugar": "Ciudad", "pais": "España", "detalle_especifico": "NOMBRE EXACTO DEL ARTISTA O EQUIPOS QUE JUEGAN", "precio": 50}}
    
    Si el evento no es relevante, devuelve: {{"relevante": false}}
    """

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"}
        )
        return json.loads(response.choices[0].message.content)
    except Exception as e:
        return {"relevante": False, "error": str(e)}