import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 
from PIL import Image
import plotly.express as px

def run():
    
    # Membuat title
    st.title('Aplikasi Prediksi Rating Pemain FIFA 2022')
    
    # Membuat sub-header
    st.subheader('Page ini Berisi Explorary Data Analysis')
    
    # Menulis baris
    st.write('By Tatia Mahendra')
    st.write('# Hello')
    st.write('## Hello')
    
    # Memasukkan dataset
    dataset = pd.read_csv("https://raw.githubusercontent.com/FTDS-learning-materials/phase-1/refs/heads/v2.4/w1/P1W1D1PM%20-%20Machine%20Learning%20Problem%20Framing.csv")
    st.dataframe(dataset)
    
    # Memasukkan gambar
    img = Image.open('images.jpg')
    st.image(img, caption='EDA for FIFA 2O22')
    
    # Menampilkan histogram dari rating
    st.write('### Histogram dari Rating')
    fig = plt.figure(figsize=(15,8))
    sns.histplot(dataset['Overall'], bins=30, kde=True)
    st.pyplot(fig)
    
    # Membuat Histogram Berdasarkan Input User
    st.write("### Histogram Berdasarkan Input User")
    fig=plt.figure(figsize=(15,8))
    opsi = st.selectbox('Pilih Kolom', ('Weight', 'Height', 'ShootingTotal'))
    sns.histplot(dataset[opsi], bins=30, kde=True)
    st.pyplot(fig)
    
    # Membuat Plotly Plot
    st.write('### Plotty Plot = Rating vs Price')
    fig = px.scatter(dataset, x='Overall', y='ValueEUR', hover_data=['Name', 'Age'])
    st.plotly_chart(fig)
    
    
    
if __name__ == '__main__': 
    run()