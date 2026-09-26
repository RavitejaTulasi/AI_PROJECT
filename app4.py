from dotenv import load_dotenv
import os
from google import genai
import streamlit as st

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
st.set_page_config(page_title="AI Translator🤖",layout="wide")
st.title("AI Translator")
st.caption("Powered by Teja")
languages = ["English",
             "Telugu",
             "Hindi",
             "Kannada",
             "Tamil",
             "Bengali",
             "Odia",
             "Urdu",
             "Spanish",
             "Chineese"
             "Sanskrit",
             "French",
             "Arabi",    
             ]

if "source_language" not in st.session_state:
    st.session_state.source_language = "English"
if "destination_language" not in st.session_state:
    st.session_state.destination_language = "Telugu"

col1,col2 = st.columns(2)
with col1:
    source_language = st.selectbox(
        "source_language",
        languages,
        index= languages.index(
            st.session_state.source_language
        )
    )
with col2:
    destination_language = st.selectbox(
        "destination_destination",
        languages,
        index= languages.index(
            st.session_state.destination_language
        )
    )

st.session_state.source_language = source_language
st.session_state.destination_language = destination_language

if st.button("swap"):
    temp = st.session_state.source_destination
    st.session_state.source_language = (st.session_state.destination_language)
    st.session_state.destination_language = temp
text = st.text_area("enter text to translate")

if st.button("translate"):
    prompt = f"""
    act as professional translator
translate {text} from {source_language} to {destination_language}

strict rules:
1. don't add extra information
2. don't remove existing information
3. don't summarise the {text}
4. act as a proffesional native {destination_language}
"""


    response = client.models.generate_content(
            model = "gemini-3.6-flash",
            contents = prompt
        )
    st.subheader("Translate")
    st.text_area("translated text  is: ",
                response.text
            )
with st.slider:
    st.subheader("model info")
    st.code("gemin-3.6-flash")
    