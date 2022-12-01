import streamlit as st
import pandas as pd
import numpy as np


def load_data():
    # finish writing data processing.
    return

df = pd.read_csv('modified_nyc_deaths_final.csv')

st.title('NYC Leading Causes of Death')
st.markdown("""
This is and interactive app between leading causes of death and race/sex in NYC.
""")


st.sidebar.header('User Input Features')
# selected_years = st.sidebar.selectbox('Year', sorted(list(df['Year'].unique())))

sorted_year_unique = sorted(df['Year'].unique()) 
selected_years = st.sidebar.multiselect('Year',sorted_year_unique) 

sorted_leading_cause_unique = sorted(df['Leading Cause'].unique())
selected_leading_cause= st.sidebar.multiselect('Leading Causes of Death', sorted_leading_cause_unique)

sorted_race_and_sex_unique = sorted(df['Race Ethnicity Sex'].unique())
selected_race_and_sex = st.sidebar.multiselect('Race and Sex', sorted_race_and_sex_unique)

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"])

st.bar_chart(chart_data)