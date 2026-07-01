import streamlit as st
import json
import os
import datetime

# Configuración
CONFIG_FILE = "data/user_config.json"
if not os.path.exists("data"):
    os.makedirs("data")

st.set_page_config(page_title="AURION Monitor", page_icon="🎫", layout="wide")
st.title("🎫 AURION: Monitor Inteligente")

# --- LÓGICA DE CARGA ---
def cargar_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            try:
                return json.load(f).get("preferencias", {})
            except:
                pass
    return {
        "deportes": [], "artistas": [], "precio_maximo": 100, 
        "intereses": [], "fecha_inicio": str(datetime.date.today()),
        "fecha_fin": str(datetime.date.today() + datetime.timedelta(days=30)),
        "pais": "Todas", "provincia": "Todas"
    }

config = cargar_config()

# --- SIDEBAR DE CONFIGURACIÓN ---
st.sidebar.header("⚙️ Configuración")

with st.sidebar.form("config_form"):
    deportes = st.multiselect("Deportes favoritos", ["baloncesto", "tenis", "fútbol", "fórmula 1"], default=config.get("deportes", []))
    artistas = st.text_input("Artistas (separados por coma)", value=", ".join(config.get("artistas", [])))
    precio = st.slider("Precio máximo (€)", 0, 500, config.get("precio_maximo", 100))
    intereses = st.multiselect("Intereses generales", ["rock", "arte moderno", "tecnología", "cine"], default=config.get("intereses", []))
    
    # Selección de País con "Todas"
    lista_paises = ["Todas", "España", "Francia", "Portugal", "Alemania", "Italia"]
    pais_actual = config.get("pais", "Todas")
    pais = st.selectbox("País europeo", lista_paises, index=lista_paises.index(pais_actual) if pais_actual in lista_paises else 0)
    
    # Selección de Provincia con "Todas"
    if pais == "España":
        lista_provincias = ["Todas", "Madrid", "Barcelona", "Valencia", "Sevilla", "Vizcaya"]
        prov_actual = config.get("provincia", "Todas")
        provincia = st.selectbox("Provincia española", lista_provincias, index=lista_provincias.index(prov_actual) if prov_actual in lista_provincias else 0)
    else:
        provincia = st.text_input("Provincia / Región (o 'Todas')", value=config.get("provincia", "Todas"))
    
    st.subheader("📅 Rango de Fechas")
    inicio_def = datetime.datetime.strptime(config.get("fecha_inicio", str(datetime.date.today())), "%Y-%m-%d").date()
    fin_def = datetime.datetime.strptime(config.get("fecha_fin", str(datetime.date.today() + datetime.timedelta(days=30))), "%Y-%m-%d").date()
    
    fecha_inicio = st.date_input("Desde", value=inicio_def)
    fecha_fin = st.date_input("Hasta", value=fin_def)
    
    submitted = st.form_submit_button("Guardar Preferencias")
    if submitted:
        lista_artistas = [a.strip() for a in artistas.split(",")] if artistas else []
        nuevos_datos = {
            "preferencias": {
                "deportes": deportes,
                "artistas": lista_artistas,
                "precio_maximo": precio,
                "intereses": intereses,
                "fecha_inicio": str(fecha_inicio),
                "fecha_fin": str(fecha_fin),
                "pais": pais,
                "provincia": provincia
            }
        }
        with open(CONFIG_FILE, "w") as f:
            json.dump(nuevos_datos, f, indent=4)
        st.success("¡Preferencias actualizadas!")

