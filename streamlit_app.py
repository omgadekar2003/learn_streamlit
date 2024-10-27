# tutorial 1 : st.text,st.write, st.code, st.write(st.write), st.write(st.error), st.header, st.subheader

import streamlit as st
import numpy as np
import pandas as pd
import json
st.title("tutorial 2")
# DATAFRAME
df = pd.DataFrame(
  np.random.randn(50,20),
  columns=["cols" + str(i) for i in range(20)])
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
f = open(r"D:\datum\aa_chatbot\simple_chatbot\prac\all_intents_js.json")
dt = json.load(f)
st.json(dt)





