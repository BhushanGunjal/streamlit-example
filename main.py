import streamlit as st
from PIL import Image
import cv2 
import numpy as np

img = st.file_uploader(label="Load X-Ray Chest image", type=['jpeg', 'jpg', 'png'], key="xray")

if img is not None:
            st.write("Original X-ray Image:")
            st.write("")
            final_img = cv2.resize(img, (400, 400))
            st.image(img)
            
            #im = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
            #notworking
            clahe = cv2.createCLAHE(clipLimit = 4) 
            final_img = clahe.apply(final_img) 
            #assertionerror comes here
            final_img = cv2.resize(final_img, (400, 400))
            st.write("")
            st.write("")
            st.write("After applying CLAHE:")
            st.write("")
      
            st.image(final_img)
else:
            st.write("Make sure you image is in JPG/PNG Format.")
