# https://blog.streamlit.io/streamlit-101-python-data-app/   
# The fundamentals of a Python data app
# By Chanin Nantasenamat
import streamlit as st
import pandas as pd

@st.cache_data

def load_data():
    return pd.read_csv("https://github.com/dataprofessor/population-dashboard/raw/master/data/us-population-2010-2019-reshaped.csv", index_col=0)

df = load_data()  # or easier:
# df = pd.read_csv("https://github.com/dataprofessor/population-dashboard/raw/master/data/us-population-2010-2019-reshaped.csv", index_col=0)

st.write("My first Streamlit app 🎈")

url = 'https://blog.streamlit.io/streamlit-101-python-data-app/'
st.write("The fundamentals of a Python data app [By Chanin Nantasenamat](%s)" % url )
st.divider()   

st.header("1. Inspect the data 🔍")

# Example 1: Inspect your data 
st.write("`st.data_editor` allows us to display :red[AND edit] data")
# st.markdown("`st.data_editor` allows us to display :red[AND edit] data")    # equal
st.data_editor(df)  # displays data in an editable table.

# Example 2: A simple bar chart
st.header("2. Get started with a simple bar chart 📊")
st.write("`st.bar_chat()` Let's chart the US state population data from the year 2019")
st.bar_chart(df[['year', 'states', 'population']],
             x='states',
             y='population')

# Example 3: Add interactivity to a bar chart  
# The following code contains three different types of interactivity. 
# Comment and uncomment the code to see which one suits your needs the best.
st.header("3. Now make it interactive 🪄")

st.write("It's your turn to select a year")

# Using st.selectbox
selected_year = st.selectbox("Select a year",
                             list(df.year.unique())[::-1])

# Using st.slider
selected_year1 = st.slider("Select a year", 2010, 2019)  # Rename  to selected_year without 1

# Using st.number_input                                   # Rename  to selected_year without 1
selected_year1 = st.number_input("Enter a year",
                               placeholder="Enter a year from 2010-2019",
                               value=2019)

if selected_year:
    df_selected_year = df[df.year == selected_year]

    # Display chart
    st.bar_chart(df_selected_year,
                 x='states',
                 y='population')

# Example 4: Integrate another Python library to create a line chart
import altair as alt 

st.header("4. How about a line chart? 📈")

st.write("Track changes over time")
'`st.altair_chart` uses the `Vega-Altair` library'

df_line_chart = df.copy()
df_line_chart['year'] = df_line_chart['year'].astype(str)

c = (
    alt.Chart(df_line_chart)
        .mark_line()
        .encode(x=alt.X('year'),
            y=alt.Y('population'),
            color='states')
)

st.altair_chart(c, use_container_width=True)

# Example 5: Add interactivity to an Altair line chart
st.header("5. Sprinkle in more interactivity 🪄")

st.write("Use `st.multiselect` and `st.slider` for data filter before chart creation")

states = st.multiselect("Pick your states (alow anything)",
                        list(df.states.unique())[::-1],
                        "California")
date_range = st.slider("Pick your date range",
                       2010, 2019,
                       (2010, 2019))          # с двух сторон меняется!

if states:
    chart_data = df[df['states'].isin(states)]   # arg is column with True and False
    chart_data = chart_data[chart_data['year'].between(date_range[0], date_range[1])]
    chart_data['year'] = chart_data['year'].astype(str)

    c = (
        alt.Chart(chart_data)
            .mark_line()
            .encode(x=alt.X('year'),
                y=alt.Y('population'),
                color='states')
    )

    st.altair_chart(c, use_container_width=True)


# streamlit run st_app101.py  