import streamlit as st 
from PIL import Image
import numpy as np
from decrypt import decryptPage
from encrypt import encryptPage

st.set_page_config(page_title="LSB Stego App", page_icon=":eyes:", layout="wide")

# Set up the Streamlit app
st.title('Tugas Akhir')
st.header('Steganografi LSB pada kover buku')

st.write("---")

PAGES = {
    "Encrypt" : encryptPage,
    "Decrypt": decryptPage,
}

st.sidebar.title("Menu")
selection = st.sidebar.radio("silahkan pilih", list(PAGES.keys()))

page = PAGES[selection]
page()