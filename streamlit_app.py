import streamlit as st
import numpy as np
import pandas as pd
import json
st.title("tutorial 2")

df = pd.DataFrame(
  np.random.randn(50,20),
  columns=["cols" + str(i) for i in range(20)])
st.write(df)


