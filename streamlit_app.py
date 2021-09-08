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

image = cv2.imread("image.png")



image_bw = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

clahe = cv2.createCLAHE(clipLimit = 4)
final_img = clahe.apply(image_bw) 


#_, ordinary_img = cv2.threshold(image_bw, 155, 201, cv2.THRESH_BINARY)


#res = np.vstack((final_img, ordinary_img))
#cv2.imshow('image', image)
#cv2.imshow('image', final_img)
#cv2.imshow('image', ordinary_img)


cv2.imshow('ImageWindow', final_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
st.pyplot()
