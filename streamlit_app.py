import streamlit as st
import EDA
import prediction

st.set_page_config(
    layout='wide',
    initial_sidebar_state='expanded',
    page_title='FIFA 2022'
)

page = st.sidebar.selectbox('Pilih Halaman', ('EDA', 'Prediction'))

if page == 'EDA':
    EDA.run()
else: 
    prediction.run()