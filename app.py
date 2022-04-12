import streamlit as st

cons = st.sidebar.selectbox('Choose', ('A', 'B'))
if cons == 'A':
    st.write('Hi')
if cons == 'B':
    st.write('Hello')