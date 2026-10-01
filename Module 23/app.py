import streamlit as st
import requests
import pandas as pd

st.title("An Amazing Project Managment App!!")

st.header("Add an Amazing Developer:")
dev_name= st.text_input("Their amazing name:")
dev_experience= st.number_input("Their awesome experience:", min_value=0,max_value=50,value=0)

if st.button("Create sigma developer"):
    dev_data={"name":dev_name,"experience":dev_experience}
    response = requests.post("http://localhost:8000/developers",json=dev_data)
    st.json = (response.json())

st.header("Add an Amazing Projects:")
proj_title = st.text_input("Input amazing name here")
proj_desc = st.text_input("Input very cool description here")
proj_langs = st.text_input("Languages Used(Comma-separated)")
lead_dev_name = st.text_input("Their amazing name:")
lead_dev_exp = st.number_input("Their awesome experience:", min_value=0,max_value=50,value=0)


if st.button("Create sigma project"):
    lead_dev_data={"name":lead_dev_name,"experience":lead_dev_exp}
    proj_data={
        "title":proj_title,
        "description":proj_desc,
        "languages":proj_langs.split(","),
        "lead_developer":lead_dev_data,
    }
    response = requests.post("http://localhost:8000/developers",json=proj_data)
    st.json = (response.json())



