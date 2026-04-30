import streamlit as st

st.title("Muay Thai 🥊")
st.write("Bem-vinda ao app de Muay Thai - A Arte das 8 Armas!")

st.markdown("---")
st.header("📸 Galeria de Fotos")

st.write("Evolução do Muay Thai:")
st.image("https://ceu.sme.prefeitura.sp.gov.br/wp-content/uploads/2025/05/progression-of-muay-thai-waq3npw5y5b60sxx-2.jpg")

st.write("Treino de Muay Thai:")
st.image("https://media-cdn.tripadvisor.com/media/attractions-splice-spp-674x446/15/6e/c2/c0.jpg")

st.write("Academia de Muay Thai:")
st.image("https://www.ironworksprime.com.br/wp-content/uploads/2016/12/Academia-Ironworks-Prime-Gramado-e-S%C3%A3o-Borja-RS-Modalidade-Muay-Thai.jpg")

st.markdown("---")
st.header("🔥 Calculadora de Calorias do Treino")

st.write("Descubra quantas calorias você queimou no treino!")

peso = st.number_input("Seu peso (kg):", min_value=30, max_value=150, value=60)
tempo = st.number_input("Tempo de treino (minutos):", min_value=10, max_value=180, value=60)
nivel = st.selectbox("Intensidade do treino:", ["Leve", "Moderado", "Intenso"])

if nivel == "Leve":
calorias = peso * 0.08 * tempo
elif nivel == "Moderado":
calorias = peso * 0.10 * tempo
else:
calorias = peso * 0.13 * tempo

if st.button("Calcular Calorias 🔥"):
st.success(f"Você queimou aproximadamente {calorias:.0f} calorias!")
if calorias < 300:
st.write("Bom começo! Continue treinando! 💪")
elif calorias < 600:
st.write("Ótimo treino! Você está arrasando! 🥊")
else:
st.write("Treino incrível! Você é uma guerreira! 🏆")

st.markdown("---")
st.header("🧠 Quiz de Muay Thai")

st.write("Teste seus conhecimentos sobre o Muay Thai!")

q1 = st.radio("1. Quantas armas tem o Muay Thai?", ["4", "6", "8", "10"])
q2 = st.radio("2. De qual país é originário o Muay Thai?", ["China", "Japão", "Tailândia", "Coreia"])
q3 = st.radio("3. O Muay Thai virou esporte olímpico em qual ano?", ["2020", "2022", "2024", "2026"])
q4 = st.radio("4. Qual golpe usa o antebraço para bloquear?", ["Jab", "Teep", "Clinch", "Defesa com braço"])

if st.button("Ver meu resultado 🏆"):
pontos = 0
if q1 == "8":
pontos += 1
if q2 == "Tailândia":
pontos += 1
if q3 == "2024":
pontos += 1
if q4 == "Defesa com braço":
pontos += 1

st.write(f"Você acertou **{pontos} de 4** perguntas!")

if pontos == 4:
st.success("Parabéns! Você é uma especialista em Muay Thai! 🏆🥊")
elif pontos >= 2:
st.info("Muito bem! Continue estudando! 💪")
else:
st.warning("Continue treinando e estudando! Você chega lá! 🥊")

st.markdown("---")
st.caption("App criado com ❤️ e Streamlit | Muay Thai 🥊")





