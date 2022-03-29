import streamlit as st

import pandas as pd
import numpy as np

import altair as alt

st.title('Display Information')

st.markdown('There are a variety of ways to display information inside of streamlit')

st.subheader('Display Text')


st.markdown('You can use:')

st.code('st.markdown(s)')
st.markdown('This is in markdown')


st.markdown('st.write()')

st.write('Allows you to display all types of data and information. Streamlit just knows...')