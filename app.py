import streamlit as st
from utils import generate_image, classify_image

# Título de la aplicación
st.title("Generador y Clasificador de Imágenes")

# Crear dos columnas
col1, col2 = st.columns(2)

# Sección de Generación de Imágenes (col1)
with col1:
    st.header("Generación de Imágenes")
    prompt = st.text_input("Ingrese un texto para generar una imagen")
    if st.button("Generar Imagen"):
        if prompt:
            image = generate_image(prompt)
            st.image(image, caption="Imagen Generada", use_column_width=True)
        else:
            st.error("Por favor, ingrese un texto")

# Sección de Clasificación de Imágenes (col2)
with col2:
    st.header("Clasificación de Imágenes")
    uploaded_file = st.file_uploader("Cargue una imagen para clasificar", type=["png", "jpg", "jpeg"])
    if st.button("Clasificar Imagen"):
        if uploaded_file:
            classification = classify_image(uploaded_file)
            st.image(uploaded_file, caption="Imagen Cargada", use_column_width=True)
            st.write(f"Clasificación: {classification}")
        else:
            st.error("Por favor, cargue una imagen")

