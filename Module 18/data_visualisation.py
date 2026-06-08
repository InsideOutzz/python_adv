import pandas as pd
import streamlit as st
import plotly.express as px

books_df = pd.read_csv("bestsellers_with_categories_2022_03_27.csv")

st.title("some analysis")
st.write("this app analyses books or smth")

st.subheader("books")
total_books = books_df.shape[0]
unique_titles = books_df["Name"].nunique()
average_rating = books_df["User Rating"].mean()
average_price = books_df["Price"].mean()

col1,col2,col3,col4 = st.columns(4)
col1.metric("Total Books", total_books) # Metric shows boxes of column information(?) #
col2.metric("Average Rating", average_rating)
col3.metric("Average Price", average_price)
col4.metric("Unique Tiles", unique_titles)

st.subheader("Dataset Preview or smth")
st.write(books_df.head())

col1,col2 = st.columns(2)

with col1:
    st.subheader("Top 10 Books")
    top_titles = books_df["Name"].value_counts().head(10)
    st.bar_chart(top_titles)

with col2:
    st.subheader("Top 10 Authors")
    top_authors = books_df["Author"].value_counts().head(10)
    st.bar_chart(top_authors)

st.subheader("Genre Distribution i guess")
fig = px.pie(books_df, values="Genre", title="Most Liked Genre (2009-2022)", color="Genre",color_discrete_sequence=px.colors.sequential.Plasma )
st.plotly_chart(fig)


st.subheader("Number if Fiction vs Non-Fiction (2009-2022)")
size = books_df.groupby(['Year', 'Genre']).size().reset_index(name='Count')
fig = px.bar(size,x="Year", y='Counts', color="Genre", title="Number if Fiction vs Non-Fiction (2009-2022)",color_discrete_sequence=px.colors.sequential.Plasma
             , barmode='group')
st.plotly_chart(fig)

st.subheader("Top 15 Authors by Counts of Books Published (2009-2022)")
top_authors = books_df["Author"].value_counts().head(15).reset_index()
top_authors.columns = ["Author", "Count"]
fig = px.bar(x="Count", y='Author', orientation="h", title="Top 15 Authors by Count of Books Published (2009-2022)",
             labels={"Count": "Books Published", "Author": "Author"}, color="Count", color_discrete_sequence=px.colors.sequential.Plasma)
st.plotly_chart(fig)

st.subheader("Filter Data by Genre")
genre_filter = st.selectbox('Select Genre', books_df['Genre'].unique())
filtered_df = books_df[books_df['Genre'] == genre_filter]
st.write(filtered_df)