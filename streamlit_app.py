################ Lecture 6 : Input Widgert part 3:
# text_area, date_input, time_input, file_uploader, camera_input , color_pick
# import streamlit as st
# import datetime

### text_area:
# txt = st.text_area(
#   label = "Write Something Interesting",
#   height = 200,
#   max_chars =100,
#   placeholder = "Write here"
# )
# st.write(txt)

### date_input:

# dte = st.date_input(
#   label = "Enter DOB",
#   value = datetime.date(2024,10,31)
# )
# st.write(dte)

###Time_Input:

# tme = st.time_input(
#   label = "Enter time",
#   value = datetime.time(10,15)
# )
# st.write(tme)

###### File Uploader:
##IMPORT
# from PIL import Image
# import numpy as np
# from io import StringIO 
# fle = st.file_uploader(
# label = "Upload File"  
# )
# if fle:
#   st.write(fle.type)
#   if "image" in fle.type:
#     # if image show image size
#     img = Image.open(fle)
#     st.write(np.array(img).shape)
#   elif fle.type == "text/plain":
#     stringio = StringIO(fle.getvalue().decode("utf-8"))
#     string_data = stringio.read()
#     st.write(string_data)

####### Camera Input:

# pict = st.camera_input(
#   "take a Pic"
# )
# if pict:
#   img = image.open(pict)
#   st.write(np.array(img).shape)

###### Color Picker:
# clr = st.color_picker(
#   "select  color you want"
# )
# st.write("You picked color",clr)

############## Lecture 7:streamlit media elements - st.image , st.audio , st.video
import streamlit as st
from PIL import Image
# import cv2

# ### streamlit media elements - st.image
# img = Image.open("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTkESVsBno9V8sbKGdJU6EpS_TzIJKWZxR4JQ&s")
# # show image:
# st.image(
#   img,
#   caption = "OG",
#   width =100,
#   channels = "RGB"
# )


####### audio file:

st.audio("learn_streamlit//fein.mp3")


