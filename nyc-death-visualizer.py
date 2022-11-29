import streamlit as st
import pandas as pd

st.title('NYC deaths causes')

st.sidebar.header('User Input Features')
selected_year = st.sidebar.selectbox('Year', list(reversed(range(1950,2020))))


print(selected_year)