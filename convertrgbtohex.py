import streamlit as st

# Streamlit app title
st.title("RGB to Hex Color Converter")

# User input for R, G, and B color levels using sliders
st.subheader("Color Levels")
red = st.slider("Red (R)", 0, 255, 128)
green = st.slider("Green (G)", 0, 255, 128)
blue = st.slider("Blue (B)", 0, 255, 128)

# Convert RGB to Hex
hex_color = "#{:02X}{:02X}{:02X}".format(red, green, blue)

# Display RGB and Hex color codes
st.subheader("Color Codes")
st.write(f"RGB: ({red}, {green}, {blue})")
st.write(f"Hex: {hex_color}")

# Display color preview
st.subheader("Color Preview")
st.write(f"Color Preview:")
st.markdown(f'<div style="width: 100px; height: 100px; background-color: {hex_color};"></div>', unsafe_allow_html=True)
