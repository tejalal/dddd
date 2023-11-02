import streamlit as st

st.write("TEJALAL CHOUDHARY")

a = st.sidebar.radio('Choose', ["Experience", "Education", "Research"])

tab1, tab2, tab3, tab4 = st.tabs(["Experience", "Research", "Publications", "Education"])
tab1.write("Experience")
tab2.write("Research")
tab3.write("Publications")
tab4.write("Education")


