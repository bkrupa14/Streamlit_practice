#%%
import pandas as pd
import numpy as np

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
# %%
df
# %%

# %%
df.columns
# %%
chart_data = pd.DataFrame(
     np.random.randn(50, 3),
     columns=["a", "b", "c"])
chart_data
# %%
df.dtypes
# %%

import altair as alt
chart = alt.Chart(df).mark_bar().encode(
    alt.X('Founded Year:O', title = 'Year Founded'),
    alt.Y('Company', title = 'Total Count'),
    color='Industry')

chart
# %%
df
# %%
