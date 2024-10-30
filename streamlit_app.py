# tutorial 1 : st.text,st.write, st.code, st.write(st.write), st.write(st.error), st.header, st.subheader

# import streamlit as st
# import numpy as np
# import pandas as pd
# import json

# #TUTORIAL 2:

# st.title("tutorial 2")
# # DATAFRAME
# df = pd.DataFrame(
#   np.random.randn(50,20),
#   columns=["cols" + str(i) for i in range(20)])
#st.write(df)

#st.DataFrame(df,height=1000, width= 200)

#st.DataFrame(np.random.randn(50,20))

# TABLE:
# there is not any customization or thing it work on only printing data in the form of table:
#st.table(df)

# st.metric:
# TCS stock example: inverse/off
#st.metric("TCS Stock", value ="3220.70", delta="19.10", delta_color="off")

#st.json:
# dt = [
#     {
#         "human": "Hello",
#         "bot": "Hi there! How can I assist you today?"
#     },
#     {
#         "human": "What is your name?",
#         "bot": "I'm your friendly chatbot here to help you out!"
#     },
#     {
#         "human": "How do I reset my password?",
#         "bot": "To reset your password, go to the settings page and click on 'Forgot Password.' Follow the instructions from there."
#     },
#     {
#         "human": "Can you tell me a joke?",
#         "bot": "Sure! Why did the scarecrow win an award? Because he was outstanding in his field!"
#     },
#     {
#         "human": "What is the weather like today?",
#         "bot": "I'm not able to check the weather at the moment, but you can look it up on a weather app or website!"
#     },
#     {
#         "human": "Thank you!",
#         "bot": "You're very welcome! Let me know if there's anything else I can help with."
#     }
# ]

# # Display the data as JSON in Streamlit
# st.json(dt,expanded = False)
#########################################################################
# TUTORIAL 3: streamlit st.line_chart , st.bar_chart , st.pyplot , st.map
# import streamlit as st
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt


# df = pd.DataFrame(np.random.randn(10,2), columns = ["prices","diff"])
####Line Chart:

# st.line_chart(df,y=["diff"])

# #### Area Chart:
# st.area_chart(df,y=["diff"])

# #### Bar Chart:
# st.bar_chart(df)

#### MatplotLib:

#fig, ax = plt.subplots()
#ax.scatter(np.arange(10),np.arange(10)**2)
#ax.hist(np.random.randn(100), bins =10)
#st.pyplot(fig)

###### Map plot:
# st.map()
# place_a = pd.DataFrame({
#   "Latitude" : [19.8762],
#   "Longitude": [75.3433]
# })

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

import streamlit as st
from datetime import time
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
s_color, e_color = st.select_slider(
   label="choose color range:",
   options = ("red","yellow","green"),
  value = ("red","yellow")
 )
 st.write("from ", s_color," to ", e_color )





