import streamlit as st
from PIL import Image
import cv2 
import numpy as np



def main():

    selected_box = st.sidebar.selectbox(
    'Choose one of the following',
    ('Welcome','Detection')
    )
    
    if selected_box == 'Welcome':
        welcome() 
    if selected_box == 'Detection':
        photo()
 

def welcome():
    _, col2, _ = st.columns([1, 10, 1])

    with col2:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.title('Covid 19 Detection using X-ray')
    with col2:
        st.write("")
        st.write("")
        st.write("")
        st.subheader('Dhanashree Chavan')
        st.write("")
        st.subheader('Bhushan Gunjal')
        st.write("")
        st.subheader('Durvesh Talekar')
    


def photo():
                     
    _, col2, _ = st.columns([1, 6, 1])

    with col2:

        st.header("Image Pre-processing using CLAHE")
        st.write("")
        st.write("")
        st.write("")
    
    ##if st.button('See Original Image'):
        
        #original = cv2.imread('image.png')
        #original = cv2.resize(original, (400, 400))
        #st.image(original)
     
   # image = cv2.imread('image.png')
   # image = cv2.resize(image, (400, 400))
  #  image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  #  
  #  x = st.slider('Change Threshold value',min_value = 0,max_value = 10)     
  #  img = cv2.imread('image.png',0)
 #   clahe = cv2.createCLAHE(clipLimit = x)
  #  final_img = clahe.apply(image) 
  #  st.image(final_img)//
    
        def load_image(img):
            im = Image.open(img)
            image = np.array(im)
            return image

        uploadFile = st.file_uploader(label="Upload image", type=['jpg', 'png', 'jpeg'])

        if uploadFile is not None:
            st.write("Original X-ray Image:")
            st.write("")
            img = load_image(uploadFile)
            final_img = cv2.resize(img, (400, 400))
            st.image(final_img)
            
            #im = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
            #notworking
            clahe = cv2.createCLAHE(clipLimit = 4) 
            final_img = clahe.apply(img) 
            #assertionerror comes here
            final_img = cv2.resize(final_img, (400, 400))
            st.write("")
            st.write("")
            st.write("After applying CLAHE:")
            st.write("")
      
            st.image(final_img)
        else:
            st.write("Make sure you image is in JPG/PNG Format.")
    
def photo1():
        
        
        def load_image(img):
            im = Image.open(img)
            image = np.array(im)
            return image

        uploadFile = st.file_uploader(label="Upload image", type=['jpg', 'png', 'jpeg'])

        if uploadFile is not None:
            st.write("Original X-ray Image:")
            st.write("")
            img = load_image(uploadFile)
            img = cv2.resize(img, (400, 400))
            #durvesh work on this
            x = st.slider('Change Threshold value',min_value = 69,max_value = 169)
            image = cv2.imread('image.png')
            image = cv2.resize(img, (300, 300))
            ret,thresh1 = cv2.threshold(image,x,255,cv2.THRESH_BINARY)
            thresh1 = thresh1.astype(np.float64)
            st.image(thresh1, use_column_width=True,clamp = True)
            #dhanashreesoln
            st.text("Bar Chart of the image")
            histr = cv2.calcHist([image],[0],None,[256],[0,256])
            st.bar_chart(histr)
            #final_imag is the name
            st.image(final_img)
        else:
            st.write("Make sure you image is in JPG/PNG Format.")
            
            

    
if __name__ == "__main__":
    main()
