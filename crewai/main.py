import streamlit as st
from dotenv import load_dotenv
from motor import RunCrew

load_dotenv()

st.title("FWK Marketing Agency")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": """Bem-vindo! Eu somos uma agencia de marketing IA desenvolvida para a FWK. Me diga que tipo de campanha você quer fazer.
                                     \nSou uma criação da FWK Labs. Caso queira saber mais, acesse: https://fwk.global."""}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.session_state.messages.append({"role": "assistant", "content": "Estou pensando numa campanha..."})

    st.chat_message("user").write(prompt)
    st.chat_message("assistant").write("Estou pensando numa campanha...")

    crew_response = RunCrew(prompt)

    msg = f"Estes são os posts: {crew_response['campaign']}.\n\n Estão são as imagens: {crew_response['images']}"

    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)