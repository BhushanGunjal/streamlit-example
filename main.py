  
import keras
import numpy as np
import streamlit as st
from keras import layers, models, optimizers  # modeling
from PIL import Image


image = Image.open(img).convert("RGB")
p_img = image.resize((224, 224))
st.image(p_image)
