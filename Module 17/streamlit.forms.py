import streamlit as st

with st.form('my_form', clear_on_submit=True):
    name = st.text_input('Name')
    age = st.slider('Age', 0, 100)
    biography = st.text_area('Biography')
    email = st.text_input('Email')
    terms = st.checkbox('I agree to the terms (even tho i didnt read them)')

    submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        st.write(f"Name: {name}")
        st.write(f"Age: {age}")
        st.write(f"Email: {email}")
        st.write(f"Short bio: {biography}")

        if terms:
            st.write("You agreed to the terms and conditions.")
        else:
            st.write("You didn't agree to the terms and conditions.")