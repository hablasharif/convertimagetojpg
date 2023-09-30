import streamlit as st
from PIL import Image
import io
import base64

# Streamlit app title
st.title("Image to JPG Converter")

# User input for uploading an image file
uploaded_image = st.file_uploader("Upload an image file:", type=["jpg", "jpeg", "png", "gif"])

# Function to convert the image to JPG format
def convert_to_jpg(image):
    try:
        img = Image.open(image)
        img_jpg = img.convert("RGB")
        return img_jpg
    except Exception as e:
        st.error(f"Error: {e}")
        return None

# Display the converted image in JPG format
if uploaded_image:
    st.subheader("Original Image:")
    st.image(uploaded_image, use_column_width=True)
    
    if st.button("Convert to JPG"):
        jpg_image = convert_to_jpg(uploaded_image)
        if jpg_image:
            st.subheader("Converted Image (JPG):")
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
