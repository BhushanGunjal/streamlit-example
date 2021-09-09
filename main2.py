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
        
    image = cv2.imread('image.jpg',0)
    
    x = st.slider('Change Threshold value',min_value = 50,max_value = 255)  

    ret,thresh1 = cv2.threshold(image,x,255,cv2.THRESH_BINARY)
    thresh1 = thresh1.astype(np.float64)
    st.image(thresh1, use_column_width=True,clamp = True)
    
    st.text("Bar Chart of the image")
    histr = cv2.calcHist([image],[0],None,[256],[0,256])
    st.bar_chart(histr)
    
    st.text("Press the button below to view Canny Edge Detection Technique")
    if st.button('Canny Edge Detector'):
        image = load_image("jerry.jpg")
        edges = cv2.Canny(image,50,300)
        cv2.imwrite('edges.jpg',edges)
        st.image(edges,use_column_width=True,clamp=True)
      
    y = st.slider('Change Value to increase or decrease contours',min_value = 50,max_value = 255)     
    
    if st.button('Contours'):
        im = load_image("jerry1.jpg")
          
        imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        ret,thresh = cv2.threshold(imgray,y,255,0)
        image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        
        img = cv2.drawContours(im, contours, -1, (0,255,0), 3)
 
        
        st.image(thresh, use_column_width=True, clamp = True)
        st.image(img, use_column_width=True, clamp = True)
         




