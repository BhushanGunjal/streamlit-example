  
import keras
import numpy as np
import streamlit as st
from keras import layers, models, optimizers  # modeling
from PIL import Image

img = st.file_uploader(label="Load X-Ray Chest image", type=['jpeg', 'jpg', 'png'], key="xray")

if img is not None:
    # Preprocessing Image
        st.image(img)
