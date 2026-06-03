import pandas as pd
import streamlit as st

df = pd.DataFrame({
    "Name": ["Bob", "Sarah", "Steve"],
    "Age:": [24,23,27],
    "City": ["New York", "Los Angeles", "Philadelphia"]

})

st.write(df)

