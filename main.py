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
    uploadFile = st.file_uploader(label="Upload image", type=['jpg', 'png', 'jpeg'])
    def load_image(img):
            im = Image.open(img)
            image_array = np.array(im)
            return image_array

    if uploadFile is not None:
            st.write("Original X-ray Image:")
            st.write("")
            img = load_image(uploadFile)
            
            st.image(img)
            
            image = cv2.imread(img) #Reading Image from path(/Image_Name.jpg) eg. here - /content/pneumonia bacterial.jpg
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            image_tensor = test_transforms(image=image)["image"]
            input_tensor = image_tensor.unsqueeze(0) 
            input_tensor = input_tensor.to(device)

            loaded_model.eval()
            prediction = np.argmax(loaded_model(input_tensor).detach().cpu().numpy())
            Predicted_Class = idx_to_class[prediction]
            st.write(Predicted_Class)
    else:
            st.write("Make sure you image is in JPG/PNG Format.")

            

    
if __name__ == "__main__":
    main()
