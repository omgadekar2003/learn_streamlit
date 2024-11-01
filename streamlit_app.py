#############Lecture 9:  st.stop , st.form , st.set_page_config , st.echo , st.help

import streamlit as st
import datetime
########### st.stop:

# email = st.text_input("Enter Email")
# if not email:
#  st.warning("Enter your email")
#  st.stop()
# st.success("Go ahead!")


########### st.form:
form = st.form("Add Info")
name = form.text_input("Enter Name")
age = form.slider("enter Age",min_value = 18,max_value = 100, step =1)
date = form.date_input("enter DOB",value = datetime.date(2004,1,25))
submitted = form.form_submit_button("Submit")
if submitted:
 st.write(name,age,date)
 
