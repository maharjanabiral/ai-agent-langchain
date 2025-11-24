import streamlit as st
import requests
import os

API_URL=os.environ.get("API_URL")
st.set_page_config(page_title="AI Agent", page_icon=":robot_face:", layout="centered")
st.title("AI Agent")
st.write("This is an AI agent that can answer your questions")

MODEL_NAMES_GROQ = ["llama-3.3-70b-versatile", "llama-3.1-8b-instant"]
MODEL_NAMES_GEMINI = ["gemini-2.5-flash"]

provider = st.radio("Select a provider", ["Groq", "Google"])
if provider == "Groq":
    model_name = st.selectbox("Select a model", MODEL_NAMES_GROQ)
else:
    model_name = st.selectbox("Select a model", MODEL_NAMES_GEMINI)

user_query = st.text_area("Enter your query", height=150, placeholder="Ask me anything")
allow_search = st.checkbox("Allow search")

if(st.button("Generate Response")):
    if user_query.strip():
        payload = {
            "model_provider": provider,
            "model_name": model_name,
            "messages": [user_query],
            "allow_search": allow_search
        }
        response = requests.post(API_URL, json=payload)
        if(response.status_code==200):
            response_data = response.json()
            if "error" in response_data:
                st.error(response_data["error"])
            st.subheader("Agent Response")
            st.markdown(f"Final Response: {response_data}")