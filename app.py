import  streamlit as st
import pandas as pd
from PIL import Image
import docx2txt
from PyPDF2 import PdfReader



@st.cache_data
def cargar_imagen(image_file):
    img = Image.open(image_file)
    return img

def leer_pdf(file):
    PdfReader = PdfReader(file)
    count = len(PdfReader.pages)
    todo_el_texto = ""
    for i in range(count):
        pagina = PdfReader.pages(i)
        todo_el_texto += pagina.extract_text()
    return(todo_el_texto)

def main():
    st.title("Tutorial de carga de archivos")
    menu = ["Imagenes", "Conjunto de Datos", "Archivos de Documentos"]
    eleccion = st.sidebar.selectbox("Menú", menu)

    if eleccion == "Imagenes":
        st.subheader("Imagen")
        archivo_imagen = st.file_uploader("Subir Imagenes", type=["png", "jpg", "jpeg"])
        if archivo_imagen is not None:
            detalles_archivo = {"nombre_archivo" : archivo_imagen.name,
                            "tipo_archivo" : archivo_imagen.type,
                            "tamaño_archivo" : archivo_imagen.size}
            st.write(detalles_archivo)
            st.image(cargar_imagen(archivo_imagen), width=250)
        
    elif eleccion == "Conjunto de Datos":
        st.subheader("Conjunto de datos")
        archivo_datos = st.file_uploader("Subir CSV o Excel", type=["csv", "xlsx"])
        if archivo_datos is not None:
            detalles_archivo = {"nombre_archivo" : archivo_datos.name,
                            "tipo_archivo" : archivo_datos.type,
                             "tamaño_archivo" : archivo_datos.size }        
            st.write(detalles_archivo)
            if detalles_archivo["tipo_archivo"] == "text/csv":
                df = pd.read_csv(archivo_datos)
            elif detalles_archivo["tipo_archivo"] == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
                df = pd.read_excel(archivo_datos)
            st.dataframe(df)




if __name__ == '__main__':
    main()



