import streamlit as st

import pandas as pd
import numpy as np

import altair as alt

st.set_page_config(layout='wide')
st.title('Unicorn Companies')
st.markdown('A unicorn is a privately held company with a valuation over $1 Billion.')

DATE_COLUMN = 'date/time'
#DATA_URL = ('/Users/blakekrupa/Desktop/School/Python/Streamlit_practice/Unicorn_Companies.csv')
DATA_URL = ('Unicorn_Companies.csv')
         
@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    #data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

 # Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.

data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text("Done! (using st.cache)")

st.subheader('Raw data')
st.write(data)


st.subheader('Number of Unicorns by Year')

#df = pd.read_csv('/Users/blakekrupa/Desktop/School/Python/Unicorn_Companies.csv')
df = pd.read_csv('Unicorn_Companies.csv')
df = df[['Company','Founded Year', 'Industry' ]]
df = df.replace(to_replace ="None",
                 value =np.nan)
df = df.replace(to_replace ="Other",
                 value =np.nan)
df = df.dropna()



df['Industry'] = df['Industry'].astype(str)
df[['Founded Year']] = df[['Founded Year']].apply(pd.to_numeric) 


df = df[(df['Founded Year'] > 1999 ) &
          (df['Founded Year'] <2022  )]

df = df.groupby(["Founded Year",'Industry']).count().reset_index()
df = df[(df['Company'] >3 )]



st.markdown('From the Chart below we notice an increase in Unicorn Companies around the mid 2010s with a steep decline following 2015')

col5, col6 = st.columns((1,1))





chart = alt.Chart(df).mark_bar().encode(
    alt.X('Founded Year:O', title = 'Year Founded'),
    alt.Y('Company', title = 'Total Count'),
    color='Industry').properties(
    width=800  # controls width of bar.
)
with col5:
    st.altair_chart(chart, use_container_width=True)
with col6:
    st.dataframe(df.style.highlight_max(axis=0))
    