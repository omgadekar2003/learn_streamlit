#### Tutorial 4 input widget part 1:

# import streamlit as st
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import time
# import requests

#### --- BUTTON
# pr = st.button("Click me")
#st.write(pr)
#if pr == True:
  #st.write(time.time())

# def fn():
#   st.write(time.time())

# st.button("Click me", on_click = fn)
  
###-- Download Button
## for CSV file Download:
# df = pd.DataFrame(np.random.randn(10,2), columns=["col1","col2"])
# #st.write(df)
# data = df.to_csv().encode("utf-8")
           
# st.download_button(
#    label="Download Code",
#    data = data,
#   file_name = "Gesture_Based_Game_Control",
#   mime = "text"
# )


### For Text file Download

# txt = "My name os Om Gadekar"
# st.download_button(
#    label="Download Code",
#    data = txt,
#    file_name="code",
#    mime = "text"
# )

# ### open jpg file:
# # https://github.com/omgadekar2003/MusicBot/blob/main/20220503_112329.jpg
# # 20220503_112329.jpg
# file = open("https://signature.freefire-name.com/img.php?f=3&t=Om%20Gadekar")
# btn = st.download_button(
#   label = "Download Image",
#   data = file,
#   file_name = "om_the_guitarist.jpg",
#   mime = "image/jpg"
# )




# ### Download Image from URL with headers
# url = "https://signature.freefire-name.com/img.php?f=3&t=Om%20Gadekar"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
# }
# response = requests.get(url, headers=headers)
# if response.status_code == 200:
#     image_data = response.content
#     st.download_button(
#         label="Download Image",
#         data=image_data,
#         file_name="om_the_guitarist.jpg",
#         mime="image/jpg"
#     )
# else:
#     st.error("Error: Could not retrieve the image.")


##### Checkbox:
# ck= st.checkbox("I agree to buy google", value =False)
# if ck == True:
#   st.write("Aggrement is Done")
# else:
#   st.write("Aggrement is Not Done")


##### Radio Buttons:

# option = st.radio(
#   label = "Order your food",
#   options = ("Vadapav","Kachori","Dabeli"),
#   index=1
#   ) 
# if option == "Vadapav":
#   st.write("Vadapav kha")
# elif option == "Kachori":
#   st.write("Kachori kha")
# elif option == "Dabeli":
#   st.write("dabeli kha")

##### Select Button:
# option = st.selectbox(
#   label = "Order your food",
#   options = ("Vadapav","Kachori","Dabeli")
#   ) 
# if option == "Vadapav":
#   st.write("Vadapav kha")
# elif option == "Kachori":
#   st.write("Kachori kha")
# elif option == "Dabeli":
#   st.write("dabeli kha")

############################ tutorial 5:
#   Input widgets part 2 

# import streamlit as st
# from datetime import time
# this import for all below code

# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt


### MultiSelect: ###
# option = st.multiselect(
#   label ="my name is: ",
#   options = ("om","sachin","og"),
#   default = ("om")
# )

# st.write(option)

###### Slider #####
#1. used as for checking in between min max
#2. Range

# num = st.slider(
#   label= "Your age",
#   min_value = 18,
#   max_value = 120,
#   value = 20,
#   step = 1
# )

# st.write(num)

# 2. Range Slider:
# num = st.slider(
#   label= "Ladki Bahin Yojana Age ",
#   min_value = 18,
#   max_value = 120,
#   value = (40,60),
#   step = 1
# )

#3. Time Range Slider: Ex. Appointment:

#appointment = st.slider(
#   label= "Your Appointment:",
#   value = (time(10,15),time(17,30))
# )
#st.write(appointment)

###### Select Slider ########

# option = st.select_slider(
#   label="choose color",
#   options = ("red","yellow","green")
# )
# st.write(option)

####### slect slider for between two colors:
# s_color, e_color = st.select_slider(
#     label="Choose color range:",
#     options=("red", "yellow", "green"),
#     value=("red", "yellow")
# )
# st.write("From", s_color, "to", e_color)

#######Text input:  # enter Email
# txt = st.text_input(
#   label = "enter your email",
#   max_chars = 50, 
#   placeholder = "Email here" 
# )
# st.write(txt)

#######enter email and pass:

# txt = st.text_input(
#   label = "enter your email",
#   max_chars = 50, 
#   placeholder = "Email here" 
# )
# st.write(txt)

# passw = st.text_input(
#   label = "enter your password",
#   max_chars = 20,
#   placeholder  = "type pass here",
#   type ="password"
# )
# st.write(passw)

######## Number Input:

# weight = st.number_input(
#   label = "enter your Weight",
#   min_value = 40,
#   max_value = 80,
#   value = 65,
#   step = 1,
#    # placeholder = "write Weight here" 
# )
# st.write(weight)

################ Lecture 6 : Input Widgert part 3:
# text_area, date_input, time_input, file_uploader, camera_input , color_pick

txt = st.text_area(
  label = "Write Something Interesting",
  height = 200,
  max_chars =100,
  placeholder = "Write here"
)
st.write(txt)

















