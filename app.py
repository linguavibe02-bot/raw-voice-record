import streamlit as st
import pandas as pd
from datetime import datetime
from streamlit_gsheets import GSheetsConnection

# 1. Configuración de la página
st.set_page_config(page_title="Raw Voice Record", page_icon="🎙️", layout="centered")

# 2. Inyección de CSS (Mantiene tu diseño intacto)
st.markdown("""
    <style>
    .stApp { background-color: #0a0a0a; }
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    
    .link-btn {
        display: block; width: 100%; padding: 15px; margin: 10px 0;
        text-align: center; background-color: transparent;
        border: 2px solid #D4AF37; border-radius: 30px;
        color: white !important; font-weight: bold; text-decoration: none;
        transition: all 0.3s ease; font-size: 16px; cursor: pointer;
    }
    .link-btn:hover { background-color: #D4AF37; color: black !important; transform: scale(1.02); box-shadow: 0 0 15px rgba(212, 175, 55, 0.5); }
    
    .link-btn-primary { border-color: #ff00cc; box-shadow: 0 0 10px rgba(255, 0, 204, 0.3); }
    .link-btn-primary:hover { background-color: #ff00cc; color: white !important; box-shadow: 0 0 20px rgba(255, 0, 204, 0.8); }

    .title { text-align: center; color: white; font-family: 'Helvetica Neue', sans-serif; font-size: 32px; font-weight: 900; margin-bottom: 0px; }
    .subtitle { text-align: center; color: #888; font-size: 14px; margin-bottom: 30px; }
    
    div[data-testid="stTextInput"] label p, div[data-testid="stSelectbox"] label p {
        color: #ffffff !important;
        font-weight: 600 !important;
        font-size: 15px !important;
    }
    
    div[data-testid="stTextInput"] input {
        color: #ffffff !important;
        background-color: #1a1a1a !important;
        -webkit-text-fill-color: #ffffff !important;
        border-radius: 10px !important;
    }
    
    .stButton > button { background-color: #ff00cc; color: white; border-radius: 30px; font-weight: bold; width: 100%; padding: 15px; border: none; }
    .stButton > button:hover { background-color: #D4AF37; color: black; }
    </style>
""", unsafe_allow_html=True)

# 3. Variables de estado
if "pagina" not in st.session_state:
    st.session_state.pagina = "inicio"

# ==========================================
# PÁGINA 1: EL INICIO
# ==========================================
if st.session_state.pagina == "inicio":
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        try:
            st.image("logo.png", use_container_width=True)
        except:
            pass 
            
    st.markdown("<p class='title'>Raw Voice Record</p>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Producimos artistas desde cero.<br>Sin costos iniciales. Ganamos si tú ganas.</p>", unsafe_allow_html=True)

    if st.button("🎙️ Aplica para grabar GRATIS", use_container_width=True, type="primary"):
        st.session_state.pagina = "formulario"
        st.rerun()

    st.markdown('<a href="https://tiktok.com/@raw.voice.record" target="_blank" class="link-btn">🎵 Síguenos en TikTok</a>', unsafe_allow_html=True)
    st.markdown('<a href="https://instagram.com/raw.voice.record" target="_blank" class="link-btn">📸 Síguenos en Instagram</a>', unsafe_allow_html=True)
    st.markdown('<a href="https://youtube.com/@tu_canal" target="_blank" class="link-btn">▶️ Mira nuestro canal de YouTube</a>', unsafe_allow_html=True)

    # --- SECCIÓN DE TRANSPARENCIA (La tabla de regalías) ---
    st.markdown("<br>", unsafe_allow_html=True)
    with st.expander("💸 ¿Cómo repartimos el dinero? (Transparencia total)"):
        st.markdown("""
        **Nuestra filosofía:** No cobramos por adelantado. Ganamos cuando tú ganas.
        
        | Vía de Ingreso | Artista | Producción / Sello | Notas |
        | :--- | :---: | :---: | :--- |
        | **DistroKid (Spotify/Apple)** | **40%** | **60%*** | *El estudio recupera su inversión (10%) los primeros 10 meses. |
        | **Canal YouTube (Tu cuenta)** | **50%** | **50%** | Tú eres el dueño de tu canal. |
        | **Canal Raw Voice (Historias)** | **18%** | **82%** | *64% Productor / 18% Presentadora. |
        | **TikTok / IG / Facebook** | **100%** | **0%** | Todo el dinero de tus redes es tuyo. |
        | **Conciertos / Shows** | **70%** | **30%** | Tú te llevas la mayor parte de la taquilla. |
        
        *Nota: El 18% del canal Raw Voice y el 50% de tu canal se dividen entre producción, presentación y estudio.*
        """)

# ==========================================
# PÁGINA 2: EL FORMULARIO
# ==========================================
elif st.session_state.pagina == "formulario":
    
    conn = st.connection("gsheets", type=GSheetsConnection)
    
    st.markdown("<p class='title'>Audición 🎤</p>", unsafe_allow_html=True)
    
    if st.button("← Volver al inicio"):
        st.session_state.pagina = "inicio"
        st.rerun()
        
    st.markdown("<p class='subtitle'>Déjanos tus datos. Si tu perfil encaja, te contactaremos.</p>", unsafe_allow_html=True)

    # 1. EL PERFIL VA FUERA DEL FORMULARIO PARA QUE ACTUALICE LA CIUDAD EN TIEMPO REAL
    perfil = st.selectbox("¿Cuál es tu perfil?", ["Cantante", "Escritor (Letras)", "Beatmaker / Productor", "Estudio de Grabación"])
    
    st.info("💡 **Nota:** Si eres **Cantante**, debes estar en Cali, Jamundí o S/der de Quilichao. Si eres **Escritor, Beatmaker o Estudio**, puedes aplicar desde cualquier parte del mundo. 🌎")

    # 2. EL RESTO DE LOS DATOS VAN DENTRO DEL FORMULARIO
    with st.form("mi_formulario", clear_on_submit=True):
        
        nombre = st.text_input("Nombre completo")
        
        # 3. AQUÍ ESTÁ LA MAGIA DEL IF
        if perfil == "Cantante":
            ciudad = st.selectbox("¿En qué ciudad vives?", ["Cali", "Jamundí", "Santander de Quilichao"])
        else:
            ciudad = st.text_input("¿En qué ciudad y país estás?")
            
        whatsapp = st.text_input("Número de WhatsApp")
        email = st.text_input("Correo electrónico") 
        link_audio = st.text_input("Link de un audio o muestra (Drive, Vocaroo, etc.)")
        
        submitted = st.form_submit_button("Enviar mi audición 🚀", use_container_width=True)

    if submitted:
        if nombre and whatsapp and email and link_audio: 
            fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            try:
                # Leemos las 7 columnas (A a la G)
                existing_data = conn.read(worksheet="Sheet1", usecols=list(range(7)), ttl=0)
                existing_data = existing_data.dropna(how="all")
                
                nuevo_dato = pd.DataFrame([{
                    "Fecha": fecha_actual, 
                    "Nombre": nombre, 
                    "Ciudad": ciudad, 
                    "WhatsApp": whatsapp, 
                    "Link Audio": link_audio,
                    "Correo": email,
                    "Perfil": perfil 
                }])
                
                updated_df = pd.concat([existing_data, nuevo_dato], ignore_index=True)
                conn.update(worksheet="Sheet1", data=updated_df)
                
                st.success("¡Recibido! Nuestro equipo se pondrá en contacto contigo muy pronto. 🎶")
                st.balloons() 
                
            except Exception as e:
                st.error(f"Error de conexión con Google Sheets: {e}")
        else:
            st.error("Por favor, llena todos los campos (Nombre, WhatsApp, Correo y Link del audio).")
