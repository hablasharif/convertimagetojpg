import streamlit as st
from PIL import Image
import io
import base64

# Streamlit app title
st.title("PNG to JPG Converter")

# User input for uploading a PNG image file
uploaded_png_image = st.file_uploader("Upload a PNG image:", type=["png"])

# Function to convert PNG to JPG
def convert_png_to_jpg(png_image):
    try:
        img = Image.open(png_image)
        if img.mode != "RGB":
            img = img.convert("RGB")
        return img
    except Exception as e:
        st.error(f"Error: {e}")
        return None

# Display the converted JPG image
if uploaded_png_image:
    st.subheader("Original PNG Image:")
    st.image(uploaded_png_image, use_column_width=True)
    
    if st.button("Convert to JPG"):
        jpg_image = convert_png_to_jpg(uploaded_png_image)
        if jpg_image:
            st.subheader("Converted JPG Image:")
            st.image(jpg_image, use_column_width=True)

            # Option to download the converted JPG image
            st.markdown(get_binary_file_downloader_html(jpg_image, "converted"), unsafe_allow_html=True)

# Function to create a download link for the image
def get_binary_file_downloader_html(image, file_label):
    img_byte_array = io.BytesIO()
    image.save(img_byte_array, format="JPEG")
    b64 = base64.b64encode(img_byte_array.getvalue()).decode()
    href = f'<a href="data:image/jpeg;base64,{b64}" download="{file_label}.jpg">Download {file_label}</a>'
    return href
