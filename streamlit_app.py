#############Lecture 9: Status elements - st.progress, spinner, balloons, error, warning, exception
########### Status element:::

import streamlit as st
import time

#### st.progress:

txt = "%completed"
my_bar = st.pregress(0, text = txt)
for pr in range(100):
  my_bar.progress(pr + 1 ,text = txt)










