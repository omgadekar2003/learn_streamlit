#############Lecture 8:Layout elements. st.sidebar, st.columns, st.tabs, st.expander, st.container

########### Sidebar:
import streamlit as st

choice = st.sidebar.radio(
  label = "GBGC",
  options =("home","Code Run Manual/Download","Feedback","Aboout Us") 
)
