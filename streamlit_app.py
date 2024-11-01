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
# form = st.form("Add Info")
# name = form.text_input("Enter Name")
# age = form.slider("enter Age",min_value = 18,max_value = 100, step =1)
# date = form.date_input("enter DOB",value = datetime.date(2004,1,25))
# submitted = form.form_submit_button("Submit")
# if submitted:
#  st.write(name,age,date)

##########st.set_page_config:

# st.set_page_config(
#  page_title = "OG APP",
#  layout = "wide"
# )
# st.write("OmG")


##########st.echo:

# def summ(a,b):
#  return a+b

# with st.echo():
#  def mul(a,b):
#   return a*b
#  a=10
#  b=20
#  su = summ(a,b)
#  mu = mul(a,b)
#  st.write(su,mu)

# st.write("outside of Fucking Echo")
# print like geek for geeks

#########st.help:

st.hele(datetime)
st.help(datetime.time)
  
 


