import sys
import os
import numpy as np
from PIL import Image  # Import the Image class from PIL

# Calculate the correct path to the modules directory
current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
modules_dir = os.path.join(parent_dir, 'modules')

# Add the modules directory to sys.path
if modules_dir not in sys.path:
    sys.path.append(modules_dir)

# Now you can import your modules
from image_processing import detect_faces_landmarks_and_colors
from jewelry_recommendations import generate_jewelry_recommendations
from utils import recommendation_results

# Your Streamlit code below
import streamlit as st

st.title('Jewelry Recommendation System')

uploaded_file = st.file_uploader("Upload your photo", type=['jpg', 'png', 'jpeg'])
if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Process the image
    if st.button('Generate Recommendations'):
        st.write("Analyzing the image...")
        try:
            # Assuming the function expects a path, you might need to save the image locally first
            # For demonstration, assuming direct use of image array
            image_array = np.array(image)  # Convert PIL image to numpy array
            recommendations = generate_jewelry_recommendations(image_array, num_colors=5)

            # Display results
            recommendation_results(recommendations)
        except Exception as e:
            st.error(f"Error in processing the image: {str(e)}")
