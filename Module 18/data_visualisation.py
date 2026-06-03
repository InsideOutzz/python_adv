import pandas as pd
import streamlit as st
import plotly.express as px

books_df.df = pd.read_csv("file1.csv")

st.title("some analysis")
st.write("this app analyses books or smth")

st.subheader("books")
total_books = books_df.shape(0)
unique_titles = books_df["Name"].nunique()