############## Lecture 7:streamlit media elements - st.image , st.audio , st.video
import streamlit as st
from PIL import Image
# import cv2

### streamlit media elements - st.image
img = Image.open("deogiri.png")
# show image:
st.image(
  img,
  caption = "OG",
  width =100,
  channels = "RGB"
)


####### audio file:

st.audio("fein.mp3", start_time = 27)
###### video file###:
st.video("VID-20220808-WA0001.mp4")

