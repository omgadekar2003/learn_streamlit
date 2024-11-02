
######### Lecture 12 | Session states in Streamlit:
#import streamlit as st

#Initialize session state:
#st.write(st.session_state)
# st.session_state
# if "key" not in st.session_state:
#  st.session_state["key"] = 1
# st.session_state

###Change session state value:

# st.session_state
# if "key" in st.session_state:
#  st.session_state["key"]=2
#  st.session_state

### Delete Session state:
# st.session_state
# if "key" in st.session_state:
#  del st.session_state["key"]
# st.session_state 

#### Bul Delete:
# st.session_state["k1"]=10
# st.session_state["k2"]=20

# st.session_state
# for k in st.session_state.keys():
#  del st.session_state[k]
# st.session_state 

#### input widget as session_state:
# st.session_state
# st.text_input("Name", key ="name")
# st.session_state

####### Callback on session_state :
# def form_callback():
#   st.write(st.session_state["my_slider"])
#   st.write(st.session_state["my_checkbox"])

# with st.form(key = "Feedback Form"):
#   slider_input = st.slider("Rate Us", 1, 5, 1, key = "my_slider")
#   checkbox_input = st.checkbox("Like it or Not", key = "my_checkbox")
#   submit_button = st.form_submit_button("submit",on_click = form_callback)
