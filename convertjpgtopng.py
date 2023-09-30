import streamlit as st
from PIL import Image
import io
import base64

# Streamlit app title
st.title("JPG to PNG Converter")

# User input for uploading a JPG image file
uploaded_jpg_image = st.file_uploader("Upload a JPG image:", type=["jpg", "jpeg"])

# Function to convert JPG to PNG
def convert_jpg_to_png(jpg_image):
    try:
        img = Image.open(jpg_image)
        if img.mode != "RGBA":
            img = img.convert("RGBA")
        return img
    except Exception as e:
        st.error(f"Error: {e}")
        return None

# Display the converted PNG image
if uploaded_jpg_image:
    st.subheader("Original JPG Image:")
    st.image(uploaded_jpg_image, use_column_width=True)
    
    if st.button("Convert to PNG"):
        png_image = convert_jpg_to_png(uploaded_jpg_image)
        if png_image:
            st.subheader("Converted PNG Image:")
            st.image(png_image, use_column_width=True)

            # Option to download the converted PNG image
            st.markdown(get_binary_file_downloader_html(png_image, "converted"), unsafe_allow_html=True)

# Function to create a download link for the image
def get_binary_file_downloader_html(image, file_label):
    img_byte_array = io.BytesIO()
    image.save(img_byte_array, format="PNG")
    b64 = base64.b64encode(img_byte_array.getvalue()).decode()
    href = f'<a href="data:image/png;base64,{b64}" download="{file_label}.png">Download {file_label}</a>'
    return href
