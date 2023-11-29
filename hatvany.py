import streamlit as st
import pandas as pd
import numpy as np

hatvanykitevo = st.slider(label'hatvany (2 ^ )', min_value=0, max_value = 16)

st.write(2**hatvanykitevo)

data = {
    'x': [i**2 for i in range(hatvanykitevo)] }

dataframe =pd.DataFrame(data)
st.write("szex")
st.line_chart(dataframe)
