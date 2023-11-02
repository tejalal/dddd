import streamlit as st

st.write("TEJALAL CHOUDHARY")

a = st.sidebar.radio('Choose', ["Experience", "Education", "Research"])

tab1, tab2 = st.tabs(["Experience", "Research", "Publications", "Education"])
tab1.write("Experience")
tab2.write("Research")
tab2.write("Publications")
tab2.write("Education")


