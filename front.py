import streamlit as st
import requests

st.title("VentureForce MVP")
st.write("Welcome to the Streamlit frontend!")

# Input fields for Company Name and User Idea
company_name = st.text_input("Company Name")
user_idea = st.text_input("User Idea")

# Button to start the venture process
if st.button("Start Your Venture"):
  pass  # Add your functionality here
