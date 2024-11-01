#############Lecture 8:Layout elements. st.sidebar, st.columns, st.tabs, st.expander, st.container
###########
# choice = st.sidebar.radio(
#   label = "GBGC",
#   options =("home","Code Run Manual/Download","Feedback","Aboout Us") 
# )
########### Sidebar:
import streamlit as st

choice = st.sidebar.radio(
  label = "GBGC",
  options =("audio","video") 
)
if choice =="audio":
  st.audio("fein.mp3")
  st.write("playing audio")

elif choice == "video":
  st.video("VID-20220808-WA0001.mp4")
  st.write("playing video")
