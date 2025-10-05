# https://blog.skillfactory.ru/kak-napisat-veb-prilozhenie-dlya-demonstratsii-data-science-proekta-na-python/


import streamlit as st
import pandas as pd
import numpy as np
# !!! указать путь к .../VSC/.venv ч/з верхнюю панель VSC Ctrl+Shift+P

# import ipympl
# import matplotlib
# matplotlib.use('Agg') # default not interactive
# matplotlib.use('TkAgg') # interactive  backend matplotlib

import matplotlib.pyplot as plt

# print(matplotlib.get_backend())  # matplotlib.use('Agg') # default not interactive
# print(f'{plt.isinteractive() = }')  # TkAgg тоже пишет не интерактивный, но выводит figure?
# %matplotlib inline

# df = pd.read_csv('BikeData2020.csv')   # без cashe
df = st.cache_data(pd.read_csv)("BikeData2020.csv")

st.title('`st.title` My first streamlit-app')

st.subheader('`st.subheader` It is our pd.DataFrame')
st.write(df.head(2))

st.markdown('''`st.markdown`
...     :red[Select] :orange[params] :green[write] :blue[text] :violet[in]
...     :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.''' )
# Наименования только числовых колонок
col_num = df.select_dtypes(include='number').columns
# col_num   # equal  st.write(col_num)

col_x = st.selectbox('`st.selectbox` по оси Х for st.scatter_chart()', col_num, index=1 )  # preselect
# 'You selected: ', col_x

col_y = st.selectbox('`st.selectbox` по оси Y for st.scatter_chart()', col_num, index=6) 
# 'You selected: ', col_y
# print(col_x, type(col_x))   # for debugging

# fig, ax = plt.subplots(figsize=(5,3))
# fig = ax.scatter(df[col_x], df[col_y])
# plt.show(fig)

st.header('Use `st.scatter_chart()` ')
# st.line_chart(fig)
st.scatter_chart(df, x=col_x, y=col_y)

# ******************************************************************
st.header('Use `plotly_express` `px.scatter()`')
import plotly_express as px
# df = st.cache(pd.read_csv)("BikeData2020.csv")
x_y = st.sidebar.multiselect('Select X and Y for px.scatter()', col_num, 
                             default=['Temperature', 'Partner 1'],
                             max_selections=2)
# print(x_y, type(x_y))   # for debugging

fig = px.scatter(df, x=x_y[0], y=x_y[1], color='Temperature')
# Plot!
st.plotly_chart(fig)



#********************************************************************

# type in terminal to lounch app.py
# python -m streamlit run app.py
# or
# streamlit run app.py

