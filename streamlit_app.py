# tutorial 1 : st.text,st.write, st.code, st.write(st.write), st.write(st.error), st.header, st.subheader

# import streamlit as st
# import numpy as np
# import pandas as pd
# import json

# #TUTORIAL 2:

# st.title("tutorial 2")
# # DATAFRAME
# df = pd.DataFrame(
#   np.random.randn(50,20),
#   columns=["cols" + str(i) for i in range(20)])
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
# dt = [
#     {
#         "human": "Hello",
#         "bot": "Hi there! How can I assist you today?"
#     },
#     {
#         "human": "What is your name?",
#         "bot": "I'm your friendly chatbot here to help you out!"
#     },
#     {
#         "human": "How do I reset my password?",
#         "bot": "To reset your password, go to the settings page and click on 'Forgot Password.' Follow the instructions from there."
#     },
#     {
#         "human": "Can you tell me a joke?",
#         "bot": "Sure! Why did the scarecrow win an award? Because he was outstanding in his field!"
#     },
#     {
#         "human": "What is the weather like today?",
#         "bot": "I'm not able to check the weather at the moment, but you can look it up on a weather app or website!"
#     },
#     {
#         "human": "Thank you!",
#         "bot": "You're very welcome! Let me know if there's anything else I can help with."
#     }
# ]

# # Display the data as JSON in Streamlit
# st.json(dt,expanded = False)
#########################################################################
# TUTORIAL 3: streamlit st.line_chart , st.bar_chart , st.pyplot , st.map
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json

df = pd.dataframe(np.random.randn(10,2), columns = ]"prices","differences"])
####Line Chart:

st.line_chart(df)







