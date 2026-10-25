import streamlit as st

# 1. Configuración de la página (Debe ser lo primero)
st.set_page_config(page_title="Raw Voice Record", page_icon="🎙️", layout="centered")

# 2. Inyección de CSS para hacerlo ver como Linktree/Beacons
st.markdown("""
    <style>
    /* Fondo oscuro general */
    .stApp {
        background-color: #0a0a0a;
    }
    
    /* Ocultar menú y footer de Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Estilo de los botones tipo Linktree */
    .link-btn {
        display: block;
        width: 100%;
        padding: 15px;
        margin: 10px 0;
        text-align: center;
        background-color: transparent;
        border: 2px solid #D4AF37; /* Dorado del logo */
        border-radius: 30px;
        color: white !important;
        font-weight: bold;
        text-decoration: none;
        transition: all 0.3s ease;
        font-size: 16px;
    }
    
    /* Efecto hover (al pasar el dedo o mouse) */
    .link-btn:hover {
        background-color: #D4AF37;
        color: black !important;
        transform: scale(1.02);
        box-shadow: 0 0 15px rgba(212, 175, 55, 0.5);
    }
    
    /* Botón destacado (Aplicar) */
    .link-btn-primary {
        border-color: #ff00cc; /* Magenta neón */
        box-shadow: 0 0 10px rgba(255, 0, 204, 0.3);
    }
    .link-btn-primary:hover {
        background-color: #ff00cc;
        color: white !important;
        box-shadow: 0 0 20px rgba(255, 0, 204, 0.8);
    }

    /* Estilo del título */
    .title {
        text-align: center;
        color: white;
        font-family: 'Helvetica Neue', sans-serif;
        font-size: 32px;
        font-weight: 900;
        margin-bottom: 0px;
    }
    .subtitle {
        text-align: center;
        color: #888;
        font-size: 14px;
        margin-bottom: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Mostrar Banner (Si lo tienes, quita el comentario)
# st.image("banner.jpg", use_container_width=True)

# 4. Mostrar Logo centrado
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("logo.png", use_container_width=True)

# 5. Títulos
st.markdown("<p class='title'>Raw Voice Record</p>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Producimos artistas desde cero.<br>Sin costos iniciales. Ganamos si tú ganas.</p>", unsafe_allow_html=True)

# 6. Botones (Reemplaza los enlaces de ejemplo con los tuyos reales)
# Botón principal
st.markdown('<a href="https://docs.google.com/forms/d/e/TU_FORMULARIO_AQUI/viewform" target="_blank" class="link-btn link-btn-primary">🎙️ Aplica para grabar GRATIS</a>', unsafe_allow_html=True)

# Otros botones
st.markdown('<a href="https://tiktok.com/@raw.voice.record" target="_blank" class="link-btn">🎵 Síguenos en TikTok</a>', unsafe_allow_html=True)

st.markdown('<a href="https://instagram.com/tu_instagram" target="_blank" class="link-btn">📸 Síguenos en Instagram</a>', unsafe_allow_html=True)
import streamlit.components.v1 as components

# ... (Aquí está todo tu código anterior: el logo, los títulos y los botones) ...

st.markdown("---") # Una línea divisoria para que se vea bonito
st.markdown("<h3 style='text-align: center; color: white;'>Aplica para grabar tu canción</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888;'>Déjanos tus datos y te contactaremos por WhatsApp.</p>", unsafe_allow_html=True)

# Pega aquí el link de tu Google Form (asegúrate de que termine en embedded=true)
url_formulario = "https://docs.google.com/forms/d/e/TU_LINK_AQUI/viewform?embedded=true"

# Esto incrusta el formulario en tu página
components.iframe(url_formulario, height=800)

st.markdown('<a href="https://youtube.com/@tu_canal" target="_blank" class="link-btn">▶️ Mira nuestro canal de YouTube</a>', unsafe_allow_html=True)

st.markdown('<a href="https://wa.me/TU_NUMERO" target="_blank" class="link-btn">💬 Habla directo con el productor</a>', unsafe_allow_html=True)
