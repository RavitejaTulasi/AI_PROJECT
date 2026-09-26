from dotenv import load_dotenv
import os
from mistralai.client import Mistral
import streamlit as st

load_dotenv()
client = Mistral(api_key=os.getenv("MISTRAL_API_KEY"))

st.set_page_config(page_title="Mr.Teja")
st.set_page_config(page_icon="😎")
st.title("Mr.Teja😎")

#clear button 
if st.button("clear"):
    st.session_state.messages = []
    st.rerun()

#memory
if "messages" not in st.session_state:
    st.session_state.messages = []

#display all messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

prompt = st.chat_input("Ask me anything:")
if prompt:
    st.session_state.messages.append({"role":"user","content":prompt})
    with st.chat_message("user"):
        st.write(prompt)

    response = client.chat.complete(
            model="ministral-3b-latest",
            messages=st.session_state.messages
    )

    answer = response.choices[0].message.content
    st.session_state.messages.append({"role":"user","content":answer})
    with st.chat_message("assistant"):
        st.write(answer)