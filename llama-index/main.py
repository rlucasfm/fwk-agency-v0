import streamlit as st
# from dotenv import load_dotenv
from motor import run_agency
import time

# load_dotenv()

st.title("FWK Marketing Agency")

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {
            "role": "assistant", 
            "content": """Bem-vindo! Eu somos uma agencia de marketing IA desenvolvida para a FWK. Me diga que tipo de campanha você quer fazer. \nSou uma criação da FWK Labs. Caso queira saber mais, acesse: https://fwk.global."""
        }, 
        {
            "role": "assistant", 
            "content": "Me fala sobre que tipo de campanha e conteúdo você quer publicar..."
        }
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if "data" not in st.session_state:
    st.session_state['data'] = {
        "campaign_briefing": "",
        "aditional_info": ""
    }

if prompt := st.chat_input():
    if st.session_state.data['campaign_briefing'] == '':
        st.session_state.data['campaign_briefing'] = prompt
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        time.sleep(0.2)
        st.session_state.messages.append({"role": "assistant", "content": "Me fala um pouco mais sobre o seu perfil/empresa.."})
        st.chat_message("assistant").write("Me fala um pouco mais sobre o seu perfil/empresa..")

    elif st.session_state.data['aditional_info'] == '':
        st.session_state.data['aditional_info'] = prompt
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.session_state.messages.append({"role": "assistant", "content": "Estou pensando numa campanha..."})
        st.chat_message("user").write(prompt)
        st.chat_message("assistant").write("Estou pensando numa campanha...")

        crew_response = run_agency(st.session_state.data['campaign_briefing'], st.session_state.data['aditional_info'])

        msg = f"Estes são os posts:\n {crew_response['post_content']}.\n\n Estão são as imagens (Use como prompt para o DALL-E ou Midjourney):\n {crew_response['images']}"

        st.session_state.messages.append({"role": "assistant", "content": msg})
        st.chat_message("assistant").write(msg)

        st.session_state.messages.append({"role": "assistant", "content": 'Gostaria de criar mais uma campanha? Descreva sua ideia'})
        st.chat_message("assistant").write('Gostaria de criar mais uma campanha? Descreva sua ideia')

        st.session_state['data'] = {
            "campaign_briefing": "",
            "aditional_info": ""
        }