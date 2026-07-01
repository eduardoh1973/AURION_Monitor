@echo off
:: Cambia al directorio del proyecto
cd /d "%~dp0"
:: Activa el entorno virtual
call venv\Scripts\activate
:: Ejecuta Streamlit
start streamlit run app.py