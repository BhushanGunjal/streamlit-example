from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st



image = cv2.imread("image.png")

image = cv2.resize(image, (300, 300))


image_bw = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


clahe = cv2.createCLAHE(clipLimit = 4)
final_img = clahe.apply(image_bw) 


#_, ordinary_img = cv2.threshold(image_bw, 155, 201, cv2.THRESH_BINARY)


#res = np.vstack((final_img, ordinary_img))
#cv2.imshow('image', image)
cv2.imshow('image', final_img)
#cv2.imshow('image', ordinary_img)


cv2.waitKey(0)
cv2.destroyAllWindows()
