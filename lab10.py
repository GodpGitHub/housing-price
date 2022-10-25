import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

st.title('California Housing Data by Yuhao Guan')

df = pd.read_csv('housing.csv')
# add a slider

price_slider = st.slider('Median housing price', 0.0, 500001.0, 200000.0)

# add a multi selector
capital_filter = st.sidebar.multiselect(
     'choose the location type',
     df.ocean_proximity.unique(),  # options
     df.ocean_proximity.unique())  # defaults

# Filter by housing price
df = df[df.median_house_value >= price_slider]

# Filter by location
df = df[df.ocean_proximity.isin(capital_filter)]


# choose income level

level = st.sidebar.radio(
    "choose income level",
    ('Low', 'Median', 'High'))

if level == 'Low':
    df = df[df.median_income < 2.5]  
elif level == 'High':
    df = df[df.median_income > 4.5]  
else:
    df = df[(df.median_income <= 4.5) & (df.median_income >= 2.5)]
    
    
# show map
st.map(df)


# show hitogram
st.subheader('Histogram of the median house value')
fig, ax = plt.subplots()
histogram = df.median_house_value
histogram.plot.hist(ax=ax, bins=30)

st.pyplot(fig)


