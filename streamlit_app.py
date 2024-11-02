#############Lecture 11 | Mutate charts, add_rows.

# import streamlit as st
# import pandas as pd
# import numpy as np
# import time
# df1 = pd.DataFrame(np.random.randn(10,2), columns =["col1","col2"])

#my_table = st.table(df1)
##adding data:
#df2 = pd.DataFrame(np.random.randn(5,2), columns =["col1","col2"])
#my_table.add_rows(df2)
#st.line_chart(df1)
## on start inp[ut data
#my_chart =st.line_chart(df1)
## on new added data 
#my_chart.add_rows(df2)


#### visual on continuous data like share market:
##adding 5 Rows after every 5 seconds:
# my_chart =st.line_chart(df1)
# for i in range(10):
#     time.sleep(5)
#     df2 = pd.DataFrame(np.random.randn(5,2), columns =["col1","col2"])
#     my_chart.add_rows(df2)

######### Lecture 12 | Session states in Streamlit:
import streamlit as st

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
st.session_state
st.text_input("Name", key ="name")
st.session_state
