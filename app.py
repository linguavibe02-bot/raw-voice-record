import streamlit as st
import pandas as pd
from datetime import datetime
from streamlit_gsheets import GSheetsConnection

# 1. Configuración de la página
st.set_page_config(page_title="Raw Voice Record", page_icon="🎙️", layout="centered")

# 2. Inyección de CSS (Mantiene tu diseño oscuro y botones neón)
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
    
    /* Estilos para el formulario nativo */
    .stTextInput > div > div > input { background-color: #1a1a1a; color: white; border-radius: 10px; }
    .stButton > button { background-color: #ff00cc; color: white; border-radius: 30px; font-weight: bold; width: 100%; padding: 15px; border: none; }
    .stButton > button:hover { background-color: #D4AF37; color: black; }
    </style>
""", unsafe_allow_html=True)

# 3. Variables de estado para navegar entre páginas
if "pagina" not in st.session_state:
    st.session_state.pagina = "inicio"

# ==========================================
# PÁGINA 1: EL INICIO (Landing Page)
# ==========================================
if st.session_state.pagina == "inicio":
    
    # Logo
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        try:
            st.image("logo.png", use_container_width=True)
        except:
            st.write("*(Sube tu logo.png a GitHub para verlo aquí)*") 
            
    st.markdown("<p class='title'>Raw Voice Record</p>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Producimos artistas desde cero.<br>Sin costos iniciales. Ganamos si tú ganas.</p>", unsafe_allow_html=True)

    # Botón principal que cambia de página
    if st.button("🎙️ Aplica para grabar GRATIS", use_container_width=True, type="primary"):
        st.session_state.pagina = "formulario"
        st.rerun()

    # TUS ENLACES RESTAURADOS
    st.markdown('<a href="https://tiktok.com/@raw.voice.record" target="_blank" class="link-btn">🎵 Síguenos en TikTok</a>', unsafe_allow_html=True)
    st.markdown('<a href="https://instagram.com/tu_instagram" target="_blank" class="link-btn">📸 Síguenos en Instagram</a>', unsafe_allow_html=True)
    st.markdown('<a href="https://youtube.com/@tu_canal" target="_blank" class="link-btn">▶️ Mira nuestro canal de YouTube</a>', unsafe_allow_html=True)
    st.markdown('<a href="https://wa.me/TU_NUMERO" target="_blank" class="link-btn">💬 Habla directo con el productor</a>', unsafe_allow_html=True)

# ==========================================
# PÁGINA 2: EL FORMULARIO DE APLICACIÓN
# ==========================================
elif st.session_state.pagina == "formulario":
    
    # ¡AQUÍ ESTÁ LA CONEXIÓN AHORA! Para que el inicio cargue rápido.
    conn = st.connection("gsheets", type=GSheetsConnection)
    
    st.markdown("<p class='title'>Audición 🎤</p>", unsafe_allow_html=True)
    
    # Botón para volver atrás
    if st.button("← Volver al inicio"):
        st.session_state.pagina = "inicio"
        st.rerun()
        
    st.markdown("<p class='subtitle'>Déjanos tus datos. Si tu perfil encaja, te contactaremos por WhatsApp.</p>", unsafe_allow_html=True)

    # El formulario nativo de Streamlit
    with st.form("mi_formulario", clear_on_submit=True):
        nombre = st.text_input("Nombre completo")
        ciudad = st.text_input("Ciudad en Colombia")
        whatsapp = st.text_input("Número de WhatsApp")
        link_audio = st.text_input("Link de un audio cantando (Drive, Vocaroo, etc.)")
        
        # Botón de enviar dentro del formulario
        submitted = st.form_submit_button("Enviar mi audición 🚀", use_container_width=True)

    if submitted:
        if nombre and whatsapp and link_audio: # Validación básica
            fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            try:
                # Leer datos existentes
                existing_data = conn.read(worksheet="Sheet1", usecols=list(range(5)), ttl=0)
                existing_data = existing_data.dropna(how="all")
                
                # Crear el nuevo registro
                nuevo_dato = pd.DataFrame([{
                    "Fecha": fecha_actual, 
                    "Nombre": nombre, 
                    "Ciudad": ciudad, 
                    "WhatsApp": whatsapp, 
                    "Link Audio": link_audio
                }])
                
                # Combinar y actualizar la hoja
                updated_df = pd.concat([existing_data, nuevo_dato], ignore_index=True)
                conn.update(worksheet="Sheet1", data=updated_df)
                
                st.success("¡Recibido! Nuestro equipo se pondrá en contacto contigo muy pronto. Gracias por mostrar interés en Raw Voice Record. 🎶")
                st.balloons() # Animación de celebración
                
            except Exception as e:
                # ESTO NOS DIRÁ EL ERROR EXACTO EN PANTALLA
                st.error(f"Error de conexión con Google Sheets: {e}")
        else:
            st.error("Por favor, llena al menos tu nombre, WhatsApp y el link del audio.")
