#%%
import pandas as pd
import numpy as np

df = pd.read_csv('/Users/blakekrupa/Desktop/School/Python/Unicorn_Companies.csv')
df = df[['Company','Founded Year' ]]
df = df.replace(to_replace ="None",
                 value =np.nan)
df = df.dropna()



df['Company'] = df['Company'].astype(str)
df[['Founded Year']] = df[['Founded Year']].apply(pd.to_numeric) 



df = df[(df['Founded Year'] > 1999 ) &
          (df['Founded Year'] <2022  ) ]

df = df.groupby(["Founded Year"]).count().reset_index()

# %%
df.dtypes
# %%
import matplotlib.pyplot as plt
df.plot.bar(x="Founded Year", y="Company", title="Number of Unicorn Companies founded by Year");

plt.show()
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

df['Founded Year'] = df['Founded Year'].dt.year
df
# %%
df['Founded Year'] = pd.to_datetime(df['Founded Year'])