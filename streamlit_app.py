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
st.table(df)
