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




    
st.title('Covid Detection using Streamlit')
    
st.header(' Dhanaashree Chavan, Bhushan Gunjal, Durvesh Talekar\n\n\n\n')
    




    
file=st.file_uploader("Upload x-ray image")
if file is not None:
    st.write(type(file))
    image = file.read()
    st.subheader('Original')
    st.image('image.png')
        
    
    x = st.slider('Change Threshold value',min_value = 0,max_value = 10)     
    img = cv2.imread('image.png',0)
    #image_bw = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit = x)
    final_img = clahe.apply(img) 
        #_, ordinary_img = cv2.threshold(image_bw, 155, 201, cv2.THRESH_BINARY)
        
        
        #res = np.vstack((final_img, ordinary_img))
        #cv2.imshow('image', image)
        #cv2.imshow('image', final_img)
        #cv2.imshow('image', ordinary_img)
        
     
     
        #cv2.imshow('ImageWindow', final_img)
    st.image(final_img)
        #cv2.waitKey()
        #st.pyplot()





