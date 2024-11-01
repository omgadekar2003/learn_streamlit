#############Lecture 9: Status elements - st.progress, spinner, balloons, error, warning, exception
########### Status element:::

import streamlit as st
import time

#### st.progress:

# txt = "%completed"
# my_bar = st.progress(0, text = txt)
# for pr in range(100):
#   time.sleep(0.1)
#   my_bar.progress(pr + 1 ,text = txt)

####### Spinner / Buffer used when we are downloading something:

# with st.spinner("wait for it....."):
#   time.sleep(5)

# st.write("wait over")


######### Balloons:
# st.balloons()
# st.snow()

#####status:

# with st.status("Downloading data..."):
#     st.write("Searching for data...")
#     time.sleep(2)
#     st.write("Found URL.")
#     time.sleep(1)
#     st.write("Downloading data...")
#     time.sleep(1)

# st.button("Rerun")


######## ERROR Message:
# st.balloons()
# st.snow()
# st.error("I'm Feining for more")


######## ERROR Message:
# st.balloons()
# st.snow()
# st.warning("Warning: I'm Feining for more")

####### Exception:
# st.balloons()
# st.snow()
# st.exception("exception: I'm Feining for more")


####### Info:
st.balloons()
st.snow()
st.info("Information: Today diwali in my house ")
