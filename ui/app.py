import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from agent.agent import ask_agent

st.title("Weather Agent UI")

question = st.text_input("Ask your weather question (e.g.: weather in Paris tomorrow)")

if st.button("Envoyer") and question:
    with st.spinner("Réfléchit..."):
        result = ask_agent(question)
    st.write("**Réponse:**", result)
