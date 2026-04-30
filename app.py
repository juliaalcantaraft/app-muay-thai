import streamlit as st

st.title("Muay Thai 🥊")

st.write("Bem-vinda ao app de Muay Thai - A Arte das 8 Armas!")

st.markdown("---")

st.header("📸 Galeria de Fotos")

st.image("https://ceu.sme.prefeitura.sp.gov.br/wp-content/uploads/2025/05/progression-of-muay-thai-waq3npw5y5b60sxx-2.jpg")

st.image("https://media-cdn.tripadvisor.com/media/attractions-splice-spp-674x446/15/6e/c2/c0.jpg")

st.image("https://www.ironworksprime.com.br/wp-content/uploads/2016/12/Academia-Ironworks-Prime-Gramado-e-S%C3%A3o-Borja-RS-Modalidade-Muay-Thai.jpg")

st.markdown("---")

st.header("🔥 Calculadora de Calorias")

st.write("Descubra quantas calorias você queimou no treino!")

peso = st.number_input("Seu peso em kg:", min_value=30, max_value=150, value=60)

tempo = st.number_input("Tempo de treino em minutos:", min_value=10, max_value=180, value=60)

calorias = peso * 0.10 * tempo

st.write("Você queimou aproximadamente:")

st.metric("Calorias", f"{calorias:.0f} kcal 🔥")

st.markdown("---")

st.header("🧠 Quiz de Muay Thai")

st.write("Quantas armas tem o Muay Thai?")
st.radio("Escolha:", ["4 armas", "6 armas", "8 armas", "10 armas"])

st.write("De qual país é originário o Muay Thai?")
st.radio("Escolha:", ["China", "Japão", "Tailândia", "Coreia"])

st.write("O Muay Thai virou esporte olímpico em qual ano?")
st.radio("Escolha:", ["2020", "2022", "2024", "2026"])

st.markdown("---")

st.caption("App criado com Streamlit | Muay Thai 🥊")





