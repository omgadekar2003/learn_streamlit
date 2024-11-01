#############Lecture 8:Layout elements. st.sidebar, st.columns, st.tabs, st.expander, st.container
###########
# choice = st.sidebar.radio(
#   label = "GBGC",
#   options =("home","Code Run Manual/Download","Feedback","Aboout Us") 
# )
########### Sidebar:
import streamlit as st

# choice = st.sidebar.radio(
#   label = "GBGC",
#   options =("audio","video") 
# )
# if choice =="audio":
#   st.audio("fein.mp3")
#   st.write("playing audio")

# elif choice == "video":
#   st.video("VID-20220808-WA0001.mp4")
#   st.write("playing video")


######### st.columns:

# col1, col2 =st.columns(2,gap="small")
# col1.audio("fein.mp3")
# col1.write("I'm feining for more")
# col2.video("VID-20220808-WA0001.mp4")
# col2.write("walk")

########## st.tabs:::
# tab1 , tab2  = st.tabs(["audio" , "video"])
# tab1.audio = ("fein.mp3")
# tab1.write("I'm feining for more")
# tab2.video = ("VID-20220808-WA0001.mp4")
# tab2.write("walk")

######

# # Creating tabs for audio and video
# tab1, tab2 = st.tabs(["Audio", "Video"])

# # Displaying audio in the first tab
# with tab1:
#     st.write("Playing audio file:")
#     st.audio("fein.mp3", format="audio/mp3")
#     st.write("I'm feining for more")

# # Displaying video in the second tab
# with tab2:
#     st.write("Playing video file:")
#     st.video("VID-20220808-WA0001.mp4")
#     st.write("Walk")

####### st.expander:

exp = st.expander("see pic")
exp.write("see image")
exp.image("deogiri.png",width = 400)








