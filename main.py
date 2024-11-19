import streamlit as st
from langchain_model import generate_restaurant_idea

st.title("Restaurant Idea Generator")

cuisine = st.sidebar.selectbox("Pick a Cuisine", ("Indian", "South Indian", "Indo-Chinese", "Indo-Pak", "Nepalese", "Mediterranean", "Mexican", "Italian", ))

if cuisine:
    response = generate_restaurant_idea(cuisine)

    print(response)
    st.header(response.get('name'))

    menu = response.get('menu').strip().split('\n')
    for item in menu:
        st.write(item)
