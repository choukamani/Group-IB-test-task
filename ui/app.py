import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from agent.agent import ask_agent

st.title("Weather Agent UI")

question = st.text_input("Pose ta question météo (ex: météo à Paris demain)")

if st.button("Envoyer") and question:
    with st.spinner("Réfléchit..."):
        result = ask_agent(question)
    st.write("**Réponse:**", result)
