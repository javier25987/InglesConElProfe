import streamlit as st
from pathlib import Path

directorio_actual = Path(".")
st.set_page_config(layout="wide")

archivos_en_raiz: list[str] = ["no class"] + list(
    map(
        lambda x: x[:-3],
        [
            f.name
            for f in directorio_actual.iterdir()
            if f.is_file() and f.name.endswith(".md")
        ]
    )
)

st.session_state.archivo = "no class"

st.title("Clases de ingles con el profe")

with st.sidebar:
    archivo_seleccionado: str = st.selectbox(
        "Seleccione la clase que desea abrir",
        archivos_en_raiz
    )

    if st.button("Abrir"):
        if archivos_en_raiz != "no class":
            st.session_state.archivo = archivo_seleccionado + ".md"

if st.session_state.archivo == "no class":
    st.header("seleccione una clase.")
else:
    with open(st.session_state.archivo, "r") as f:
        archivo = "".join(f.readlines())

    st.markdown(archivo, unsafe_allow_html=True)