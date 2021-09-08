from collections import namedtuple
from PIL import Image
import altair as alt
import math
import pandas as pd
import streamlit as st
import cv2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import shutil




def main():

    selected_box = st.sidebar.selectbox(
    'Choose one of the following',
    ('Welcome','Image Processing', 'Video', 'Face Detection', 'Feature Detection', 'Object Detection')
    )
    
    if selected_box == 'Welcome':
        welcome() 
        
    if selected_box == 'Image Processing':
        photo()

 

def welcome():
    
    st.title('Image Processing using Streamlit')
    
    st.subheader('A simple app that shows different image processing algorithms. You can choose the options'
             + ' from the left. I have implemented only a few to show how it works on Streamlit. ' + 
             'You are free to add stuff to this app.')
    




def photo():
    
    file=st.file_uploader("Upload x-ray image")
    if file is not None:
        image = file.read()
        
        
        
        image_bw = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        clahe = cv2.createCLAHE(clipLimit = 4)
        final_img = clahe.apply(image_bw) 
        #_, ordinary_img = cv2.threshold(image_bw, 155, 201, cv2.THRESH_BINARY)
        
        
        #res = np.vstack((final_img, ordinary_img))
        #cv2.imshow('image', image)
        #cv2.imshow('image', final_img)
        #cv2.imshow('image', ordinary_img)
        
     
     
        #cv2.imshow('ImageWindow', final_img)
        st.image(final_img)
        st.image(final_img)
        #cv2.waitKey()
        #st.pyplot()

if __name__ == "__main__":
    main()




