import os
from dotenv import load_dotenv
import streamlit as st
from openai import OpenAI

load_dotenv()

#CRIAR O MODELO DE IA
modelo_ia = OpenAI(
    api_key=os.getenv("API_KEY"),
    base_url=os.getenv("BASE_URL")
    )

#CRIA A SESSÃO
if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []

#TITULO DA PAGINA
st.write("## Chatbot com IA")

#EXIBE AS MENSAGENS DO HISTÓRICO
for mensagem in st.session_state["lista_mensagens"]:
    st.chat_message(mensagem["role"]).write(mensagem["content"])

#RECEBE A PERGUNTA
pergunta = st.chat_input("Insira sua pergunta aqui")

if pergunta:
    #EXIBE A PERGUNTA
    st.chat_message("user").write(pergunta)

    #ADICIONA A PERGUNTA DO USUARIO AO HISTORICO
    mensagem_usuario = {
        "role": "user", 
        "content":pergunta
    }
    
    st.session_state["lista_mensagens"].append(
        mensagem_usuario
    )

    #PEDE A RESPOSTA PARA O MODELO
    with st.chat_message("assistant"):
        resposta_modelo = modelo_ia.chat.completions.create(
            messages=st.session_state["lista_mensagens"],
            model="gemini-flash-lite-latest",
            stream = True
        )

        #ESCREVE O CONTEUDO CONFORME A IA GERA
        resposta_ia = st.write_stream(resposta_modelo)

    #ADICIONA A MENSAGEM DA IA AO HISTORICO
    st.session_state["lista_mensagens"].append(
        {
            "role": "assistant", 
            "content": resposta_ia
        }
    )



