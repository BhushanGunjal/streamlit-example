
import streamlit as st
from PIL import Image
import cv2 
import numpy as np



def main():

    selected_box = st.sidebar.selectbox(
    'Choose one of the following',
    ('Welcome','Image Processing 1', 'Image Processing 2', 'Image Preprocessing', 'Detection')
    )
    
    if selected_box == 'Welcome':
        welcome() 
    if selected_box == 'Image Processing 1':
        photo()
    if selected_box == 'Image Processing 2':
        photo1()
    if selected_box == 'Image Preprocessing':
        photo3()
    if selected_box == 'Detection':
        feature_detection()
 

def welcome():
    
    st.title('Image Processing using Streamlit')
    
    st.subheader('A simple app that shows different image processing algorithms. You can choose the options'
             + ' from the left. I have implemented only a few to show how it works on Streamlit. ' + 
             'You are free to add stuff to this app.')
    


def load_image(filename):
    image = cv2.imread(filename)
    return image
 
def photo():

    st.header("Thresholding, Edge Detection and Contours")
    
    if st.button('See Original Image'):
        
        original = Image.open('image.png')
        st.image(original, use_column_width=True)
        
    image = cv2.imread('image.png')
    image = cv2.resize(image, (300, 300))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    x = st.slider('Change Threshold value',min_value = 0,max_value = 10)     
    img = cv2.imread('image.png',0)
    clahe = cv2.createCLAHE(clipLimit = x)
    final_img = clahe.apply(image) 
    st.image(final_img)
    
def photo1():
        x = st.slider('Change Threshold value',min_value = 69,max_value = 169)
        image = cv2.imread('image.png')
        image = cv2.resize(image, (300, 300))
        ret,thresh1 = cv2.threshold(image,x,255,cv2.THRESH_BINARY)
        thresh1 = thresh1.astype(np.float64)
        st.image(thresh1, use_column_width=True,clamp = True)
    
        st.text("Bar Chart of the image")
        histr = cv2.calcHist([image],[0],None,[256],[0,256])
        st.bar_chart(histr)

    
if __name__ == "__main__":
    main()
