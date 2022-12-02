import streamlit as st
import pandas as pd
import numpy as np

import plotly.express as px


# function to pre-process the data
def load_data():
    df = pd.read_csv('New_York_City_Leading_Causes_of_Death.csv')

    # drop unused columns
    df = df.drop(labels=['Death Rate', 'Age Adjusted Death Rate'], axis = 1)

    # Change sex to full names
    df['Sex'] = df['Sex'].replace({'M':'Male', 'F':'Female'})

    # race before skin color
    df['Race Ethnicity'] = df['Race Ethnicity'].replace({'Non-Hispanic White':'White Non-Hispanic', 'Non-Hispanic Black':'Black Non-Hispanic'})

    # change data type of death column and clean data
    df['Deaths'] = df['Deaths'].astype("string") # object data type to string data type
    df['Deaths'] = df['Deaths'].replace({'.':'0'}) # replace 0 with .
    df['Deaths'] = df['Deaths'].astype(int) # string data type to integer data type

    # Clean up Race Ethnicity column
    df['Race Ethnicity'] = df['Race Ethnicity'].astype('string')
    df['Race Ethnicity'] = df['Race Ethnicity'].replace({'Other Race/ Ethnicity':'Other Race/Ethnicity'})

    # combine race and sex
    df["Race Ethnicity Sex"] = df["Race Ethnicity"] + "_" + df["Sex"]

    # drop the sex and race ethnicity columns
    df = df.drop(columns = ['Sex', 'Race Ethnicity'])
    return df

# df = pd.read_csv('modified_nyc_deaths_final.csv')
df = load_data()

st.title('NYC Leading Causes of Death')
st.markdown("""
This is an interactive app between leading causes of death and race/sex in NYC.
""")

# upleaded_file = st.file_uploader('Upload your file here')



st.sidebar.header('User Input Features')
# selected_years = st.sidebar.selectbox('Year', sorted(list(df['Year'].unique())))

sorted_year_unique = sorted(df['Year'].unique()) 
selected_years = st.sidebar.multiselect('Year',sorted_year_unique, sorted_year_unique) 

sorted_leading_cause_unique = sorted(df['Leading Cause'].unique())
selected_leading_cause= st.sidebar.multiselect('Leading Causes of Death', sorted_leading_cause_unique, sorted_leading_cause_unique)

sorted_race_and_sex_unique = sorted(df['Race Ethnicity Sex'].unique())
selected_race_and_sex = st.sidebar.multiselect('Race and Sex', sorted_race_and_sex_unique, sorted_race_and_sex_unique)

# filtering data
df_selected_data = df[(df['Year'].isin(selected_years)) & (df['Leading Cause'].isin(selected_leading_cause)) & (df['Race Ethnicity Sex'].isin(selected_race_and_sex))]
# display the selected data frame
st.header('Display selected data')
st.write('Data Dimension: ' + str(df_selected_data.shape[0]) + ' rows and ' + str(df_selected_data.shape[1]) + ' columns.')
st.dataframe(df_selected_data)


# chart_data = pd.DataFrame(
#     np.random.randn(20, 3),
#     columns=["a", "b", "c"])
# st.bar_chart(chart_data)

# def interactive_plot_example():
#     x_axis_val = st.selectbox('Select the X-axis', options=df.columns)
#     y_axis_val = st.selectbox('Select the Y-axis', options=df.columns)

#     plot = px.scatter(df, x=x_axis_val, y=y_axis_val)
#     st.plotly_chart(plot, use_container_width=True)

# interactive_plot_example()

# st.write(selected_years)
# st.write(type(selected_years))

# def interactive_plot(years, causes, race_and_sex):
#     fig = px.bar(df, )
#     return


def interactive_plot(df):
    # fig = px.bar(df, x="Deaths", y="Leading Cause", color="Race Ethnicity Sex", orientation='h')
    # fig.show()
    plot = px.bar(df, x="Deaths", y="Leading Cause", color="Race Ethnicity Sex", orientation='h')
    st.plotly_chart(plot)


# st.bar_chart(df, x = selected_race_and_sex, y = selected_leading_cause)

interactive_plot(df_selected_data)


# data frame extractor function from user input features
# draw horizontal bar graph using user chosen data frame