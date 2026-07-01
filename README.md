<<<<<<< HEAD

# 🎫 AURION: Monitor Inteligente de Eventos

AURION es una plataforma de monitorización automatizada diseñada para filtrar, extraer y notificar eventos en tiempo real. Este proyecto integra Inteligencia Artificial Generativa para transformar datos brutos en información de valor, enviando alertas personalizadas a través de múltiples canales.

## 🚀 Arquitectura del Sistema
El sistema sigue una arquitectura modular orientada a servicios:

* **Frontend:** Panel de configuración construido en **Streamlit** para la gestión dinámica de preferencias.
* **Cerebro (IA):** Agente inteligente basado en **Llama-3.3 (Groq API)**, responsable de filtrar eventos según criterios geográficos y de interés, y extraer entidades clave.
* **Motor de Monitorización:** Orquestador en Python (`main.py`) que ejecuta el ciclo ETL (Extract, Transform, Load) de forma continua.
* **Integraciones:** Notificaciones multicanal mediante **Telegram Bot API** y protocolos **SMTP** para correo electrónico.

## 🛠 Características Técnicas
- **ETL Inteligente:** Captura de eventos seguida de una fase de transformación mediada por LLM para limpieza y enriquecimiento de datos.
- **Filtrado Flexible:** Capacidad de aplicar filtros geográficos específicos (País/Provincia) o modo global ("Todas").
- **Automatización:** Configurado para ejecución local y preparado para despliegue en la nube mediante **GitHub Actions** (CI/CD).
- **Manejo de Errores:** Implementación de logs y gestión robusta de excepciones para asegurar la persistencia del servicio.

## 🔒 Seguridad y Buenas Prácticas
- **Variables de Entorno:** Gestión segura de claves mediante archivos locales o `Secrets` en GitHub.
- **Entornos Virtuales:** Aislamiento total de dependencias para asegurar la reproducibilidad del entorno.
- **Logging Estructurado:** Seguimiento en tiempo real de errores y eventos detectados.

## 🧠 ¿Por qué este enfoque?
El valor diferencial de AURION reside en la transición de un monitor estático a un **sistema inteligente**:
1. **Reducción de Ruido:** La IA filtra basándose en el contexto, superando las limitaciones de las palabras clave simples.
2. **Desacoplamiento:** La separación de la lógica de búsqueda, inteligencia y notificación permite un mantenimiento escalable.

## 📂 Estructura del Proyecto
```text
AURION_Monitor/
├── app.py                # Interfaz de usuario (Streamlit)
├── main.py               # Orquestador principal
├── src/
│   ├── agente.py         # Lógica de IA y filtrado
│   ├── monitor.py        # Ciclo de vigilancia y notificaciones
│   └── tools/            # Integraciones (Telegram, Search)
├── requirements.txt      # Dependencias del proyecto
└── README.md
=======
# AURION_Monitor
Agente de aviso de disponibilidad de entradas
>>>>>>> d5bba3faefeab1af388e8379f48b0e3f510437dd
