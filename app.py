import streamlit as st

st.set_page_config(page_title="Muay Thai 🥊", page_icon="🥊", layout="wide")

st.title("🥊 Muay Thai - A Arte das 8 Armas")
st.markdown("---")

st.markdown("## O que é o Muay Thai?")
st.markdown("O **Muay Thai** é uma arte marcial tailandesa conhecida como a *Arte das 8 Armas*, pois utiliza punhos, cotovelos, joelhos e canelas como armas de combate. É um dos esportes mais completos e eficientes do mundo! 🌍")


st.markdown("---")
st.header("📸 Galeria de Fotos")

col1, col2, col3 = st.columns(3)

with col1:
st.image("https://ceu.sme.prefeitura.sp.gov.br/wp-content/uploads/2025/05/progression-of-muay-thai-waq3npw5y5b60sxx-2.jpg", caption="Evolução do Muay Thai", use_container_width=True)

with col2:
st.image("https://media-cdn.tripadvisor.com/media/attractions-splice-spp-674x446/15/6e/c2/c0.jpg", caption="Treino de Muay Thai", use_container_width=True)

with col3:
st.image("https://www.ironworksprime.com.br/wp-content/uploads/2016/12/Academia-Ironworks-Prime-Gramado-e-S%C3%A3o-Borja-RS-Modalidade-Muay-Thai.jpg", caption="Academia de Muay Thai", use_container_width=True)

st.markdown("---")
st.header("🎥 Vídeo - Nocautes Épicos")
st.video("https://www.youtube.com/watch?v=ZF85JcLaoTk")

st.markdown("---")
st.header("⚔️ As 8 Armas do Muay Thai")

col4, col5 = st.columns(2)

with col4:
st.markdown("👊 **Punhos** - Jab, Cross, Hook, Uppercut")
st.markdown("💪 **Cotovelos** - O golpe mais temido")
st.markdown("🦵 **Joelhos** - Potência e precisão")
st.markdown("🦶 **Canelas** - Chutes devastadores")

with col5:
st.info("O Muay Thai é praticado há mais de 2.000 anos na Tailândia 🇹🇭")
st.success("É esporte olímpico desde Paris 2024! 🏅")

st.markdown("---")
st.header("🎯 Conheça os Golpes")

golpe = st.selectbox("Escolha um golpe para saber mais:", ["Jab", "Teep (chute frontal)", "Roundhouse Kick", "Clinch com joelho"])

if golpe == "Jab":
st.write("👊 O **Jab** é o golpe mais básico e importante. Serve para manter distância.")
elif golpe == "Teep (chute frontal)":
st.write("🦵 O **Teep** empurra o adversário e controla a distância de combate.")
elif golpe == "Roundhouse Kick":
st.write("🦶 O **Roundhouse Kick** é o chute mais poderoso do Muay Thai!")
elif golpe == "Clinch com joelho":
st.write("💪 O **Clinch** é único do Muay Thai — agarra e desfere joelhadas!")

st.markdown("---")
st.header("📊 Benefícios do Muay Thai")

col6, col7, col8 = st.columns(3)

with col6:
st.metric("Calorias por hora", "800 kcal", "🔥")

with col7:
st.metric("Grupos musculares", "12+", "💪")

with col8:
st.metric("Praticantes no mundo", "130 milhões", "🌍")

st.markdown("---")
st.caption("App criado com ❤️ e Streamlit | Muay Thai 🥊")




