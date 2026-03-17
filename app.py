import streamlit as st
import easyocr
import cv2
import numpy as np
from PIL import Image
import re

st.title("📄 Invoice Data Extraction using EasyOCR")

uploaded_file = st.file_uploader("Upload Invoice Image", type=["png","jpg","jpeg"])

if uploaded_file is not None:

    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Invoice", width=500)

    img = np.array(image)

    reader = easyocr.Reader(['en'])

    results = reader.readtext(img)

    extracted_text = ""
    for detection in results:
        extracted_text += detection[1] + "\n"

    st.subheader("Extracted Text")
    st.text(extracted_text)

    # Extract invoice fields
    invoice_no = re.findall(r'INV\d+', extracted_text)
    date = re.findall(r'\d{2}/\d{2}/\d{4}', extracted_text)
    amount = re.findall(r'\d+\.\d{2}', extracted_text)

    st.subheader("Extracted Invoice Data")

    st.write("Invoice Number:", invoice_no[0] if invoice_no else "Not Found")
    st.write("Date:", date[0] if date else "Not Found")
    st.write("Total Amount:", amount[-1] if amount else "Not Found")