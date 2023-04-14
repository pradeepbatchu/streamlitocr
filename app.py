import easyocr as ocr  # OCR
import streamlit as st  # Web App
import os
from easyoc import easyocr
from pathlib import Path

UPLOAD_FOLDER = './upload/'

# title
st.title("OCR - Extract Text from PDF")

st.markdown("")

# uploader
uploaded_file = st.file_uploader('Choose your .pdf file', type="pdf")


@st.cache
def load_model():
    reader = ocr.Reader(['en'], model_storage_directory='.')
    return reader


reader = load_model()  # load model

if uploaded_file is not None:
    save_folder = UPLOAD_FOLDER
    save_path = Path(save_folder, uploaded_file.name)
    with open(save_path, mode='wb') as w:
        w.write(uploaded_file.getvalue())
    pdf_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
    print(pdf_path)
    text = easyocr(pdf_path)
    st.write(text)
    st.success("Here you go!")
    st.balloons()
    st.caption("Hurray your document get OCRrred!")
else:
    st.write("Upload an PDF")



