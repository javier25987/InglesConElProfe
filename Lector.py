import streamlit as st
from pathlib import Path

directorio_actual = Path(".")
st.set_page_config(layout="wide", theme="light")

archivos_en_raiz: list[str] = [
    f.name[:-3]
    for f in directorio_actual.iterdir()
    if f.is_file() and f.name.endswith(".md")
]

st.session_state.archivo = "inicio.md"

with st.sidebar:
    archivo_seleccionado: str = st.selectbox(
        "Que clase desea abrir?",
        archivos_en_raiz
    )

    if st.button("Abrir"):
        st.session_state.archivo = archivo_seleccionado + ".md"

with open(st.session_state.archivo, "r") as f:
    archivo = "".join(f.readlines())

st.markdown(archivo, unsafe_allow_html=True)