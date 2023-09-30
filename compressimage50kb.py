import streamlit as st
from PIL import Image
import io
import base64

# Streamlit app title
st.title("Image Compressor (50KB)")

# User input for uploading an image file
uploaded_image = st.file_uploader("Upload an image file:", type=["jpg", "jpeg", "png", "gif"])

# Function to compress the image to 50KB
def compress_image(image, target_size_kb):
    try:
        img = Image.open(image)
        img.save("temp.jpg", optimize=True, quality=85)  # Compress the image to 85% quality
        img = Image.open("temp.jpg")

        # Ensure the image is within the target size range
        while len(img.tobytes()) / 1024 > target_size_kb:
            img.save("temp.jpg", optimize=True, quality=85)
            img = Image.open("temp.jpg")

        return img
    except Exception as e:
        st.error(f"Error: {e}")
        return None

# Display the compressed image
if uploaded_image:
    st.subheader("Original Image:")
    st.image(uploaded_image, use_column_width=True)
    
    if st.button("Compress to 50KB"):
        compressed_img = compress_image(uploaded_image, target_size_kb=50)
        if compressed_img:
            st.subheader("Compressed Image (50KB):")
            st.image(compressed_img, use_column_width=True)

            # Option to download the compressed image
            st.markdown(get_binary_file_downloader_html(compressed_img, "compressed"), unsafe_allow_html=True)

# Function to create a download link for the image
def get_binary_file_downloader_html(image, file_label):
    img_byte_array = io.BytesIO()
    image.save(img_byte_array, format="JPEG")
    b64 = base64.b64encode(img_byte_array.getvalue()).decode()
    href = f'<a href="data:image/jpeg;base64,{b64}" download="{file_label}.jpg">Download {file_label}</a>'
    return href
