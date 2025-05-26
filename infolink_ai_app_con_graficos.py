
import streamlit as st
import feedparser
import random
import streamlit.components.v1 as components
from PIL import Image

st.set_page_config(page_title="InfoLink AI", layout="wide")

st.title("🤖 InfoLink AI – Comunicación inteligente para decisiones informadas")

# Sección 1: Noticias financieras confiables
st.header("📰 Noticias confiables del mercado")
feeds = [
    "https://feeds.finance.yahoo.com/rss/2.0/headline?s=^GSPC&region=US&lang=en-US",
    "https://www.investing.com/rss/news_285.rss"
]

for url in feeds:
    feed = feedparser.parse(url)
    st.subheader(feed.feed.title)
    for entry in feed.entries[:3]:
        st.markdown(f"- [{entry.title}]({entry.link})")

st.divider()

# Sección 2: Indicador PIN
st.header("📈 Indicador de Trading Informado (PIN)")
pin_value = round(random.uniform(0.10, 0.30), 3)
st.metric(label="Probabilidad de Informed Trading", value=f"{pin_value}")

if pin_value < 0.15:
    st.warning("⚠️ Atención: Bajo nivel de decisiones informadas.")
elif pin_value < 0.25:
    st.info("ℹ️ Nivel moderado. Seguir observando.")
else:
    st.success("✅ Buen nivel de información en el mercado.")

st.divider()

# Sección 3: Recomendación automática simple
st.header("🤖 Recomendación automática")
fake_titles = [
    "Mercado en alza tras anuncio de la FED",
    "Crisis política golpea las bolsas",
    "Nueva tecnología impulsa acciones tecnológicas"
]

selected_title = random.choice(fake_titles)
st.write(f"**Última noticia analizada:** {selected_title}")

if "crisis" in selected_title.lower():
    st.error("🚨 Recomendación: Precaución, alta volatilidad detectada.")
elif "alza" in selected_title.lower() or "impulsa" in selected_title.lower():
    st.success("📈 Recomendación: Posible oportunidad detectada.")
else:
    st.info("🔎 Recomendación: Sigue monitoreando el mercado.")

st.divider()

# Sección 4: Sala colaborativa (simulada)
st.header("💬 Sala colaborativa (demo)")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📹 Videollamada (simulada)")
    components.iframe("https://meet.jit.si/InfoLinkAI-demo", height=300)

with col2:
    st.subheader("🗨️ Chat en vivo (simulado)")
    chat_text = """User1: ¿Qué opinan del movimiento del mercado hoy?
User2: Creo que se debe a la noticia sobre la FED."""
    st.text_area("Chat", chat_text, height=300)

st.divider()

# Sección 5: Gráficos de simulación
st.header("📊 Simulación del impacto de InfoLink AI")

st.subheader("📈 Evolución del indicador PIN")
img1 = Image.open("grafico_evolucion_pin.png")
st.image(img1, caption="Evolución del PIN: sin vs con InfoLink AI",use_container_width=True)

st.subheader("📊 Comparación de desempeño entre grupos")
img2 = Image.open("comparacion_grupoA_grupoB.png")
st.image(img2, caption="Usuarios sin InfoLink AI vs con InfoLink AI", use_container_width=True)

st.caption("Datos simulados para demostrar el impacto de la herramienta en la toma de decisiones.")
