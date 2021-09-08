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




    
st.title('Image Processing using Streamlit')
    
st.subheader('A simple app that shows different image processing algorithms. You can choose the options'
             + ' from the left. I have implemented only a few to show how it works on Streamlit. ' + 
             'You are free to add stuff to this app.')
    




    
file=st.file_uploader("Upload x-ray image")
if file is not None:
    image = file.read()
    st.image(image,use_column_width=True)
        
        
    img = cv2.imread('C:\\Users\\gunja\\Desktop\\image.png')
    image_bw = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
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





