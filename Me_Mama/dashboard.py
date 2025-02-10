import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Instagram MKT')
st.text('Como funciona o marketing digital no Instagram')

uploaded_file = st.file_uploader('Upload your file here:')

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.write(df.describe())

    st.header('Dados Iniciais:')
    st.write(df.head())

    fig, ax = plt.subplots(1,1)
    ax.scatter(x=df['Reach'], y=df['Likes'])
    ax.set_xlabel('Alcance')
    ax.set_ylabel('Curtidas')

    st.pyplot(fig)