#############Lecture 9:  st.stop , st.form , st.set_page_config , st.echo , st.help

import streamlit as st
#import time
########### st.stop:

email = st.text_input("Enter Email")
if not email:
 st.warning("Enter your email")
 st.stop()
st.success("Go ahead!")

 
