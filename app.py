import streamlit as st

st.title("Muay Thai 🥊")
st.write("Bem-vinda ao app de Muay Thai - A Arte das 8 Armas!")
st.markdown("---")

st.header("📸 Galeria de Fotos")
st.image("https://ceu.sme.prefeitura.sp.gov.br/wp-content/uploads/2025/05/progression-of-muay-thai-waq3npw5y5b60sxx-2.jpg")
st.image("https://media-cdn.tripadvisor.com/media/attractions-splice-spp-674x446/15/6e/c2/c0.jpg")
st.image("https://www.ironworksprime.com.br/wp-content/uploads/2016/12/Academia-Ironworks-Prime-Gramado-e-S%C3%A3o-Borja-RS-Modalidade-Muay-Thai.jpg")
st.image("https://efemeridesdoefemello.com/wp-content/uploads/2016/06/30jun16.jpg?w=768&h=767")
st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSIsLD1dsnnQRuC8QhYsWU1kJnqd21WEiRfqQ&s")

st.markdown("---")
st.header("🎥 Vídeo de Muay Thai")
st.video("https://www.youtube.com/watch?v=bI12xJW3GUM")

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
st.write("Teste seus conhecimentos!")

r1 = st.radio("1. Quantas armas tem o Muay Thai?", ["4 armas", "6 armas", "8 armas", "10 armas"])
r2 = st.radio("2. De qual país é originário o Muay Thai?", ["China", "Japão", "Tailândia", "Coreia"])
r3 = st.radio("3. O Muay Thai virou esporte olímpico em qual ano?", ["2020", "2022", "2024", "2026"])

pontos = 0
pontos = pontos + (1 if r1 == "8 armas" else 0)
pontos = pontos + (1 if r2 == "Tailândia" else 0)
pontos = pontos + (1 if r3 == "2024" else 0)

st.write(f"Sua pontuação atual: {pontos} de 3 ✅")

st.markdown("---")
st.caption("App criado com Streamlit | Muay Thai 🥊")





