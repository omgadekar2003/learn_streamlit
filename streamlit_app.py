#############Lecture 11 | Mutate charts, add_rows.

import streamlit as st
import pandas as pd
import numpy as np
df1 = pd.DataFrame(np.random.randn(10,2), columns =["col1","col2"])
my_table = st.table(df1)
# addin data:
df2 = pd.DataFrame(np.random.randn(5,2), columns =["col1","col2"])
my_table = st.table.add_rows(df2)

