import streamlit as st

tab1, tab2, tab3, = st.tabs(["Tab1", "Tab2", "Tab3"]) #Built-in function for tabs.#

with tab1:
    st.header("Content")
    st.write("Yuji has a black flash chain, which you can hit on an actual player by sidedashing whilst using 3.")

with tab2:
    st.header("Content")
    st.write("Nanami's third move is chainable with every move he has.")

with tab3:
    st.header("Content")
    st.write("Yuta now has a built-in black flash.")