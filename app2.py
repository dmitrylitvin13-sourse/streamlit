import streamlit as st
import pandas as pd
import numpy as np
# import ipympl
import matplotlib
# matplotlib.use('Agg') # default not interactive
matplotlib.use('TkAgg') # Or 'TkAgg', 'Qt5Agg', 'GTK3Agg'
        # pip install PyQt6  in Terminal for use 'Qt5Agg'  не работает?
        # pip install tk        in Terminal for use 'TkAgg' 
import matplotlib.pyplot as plt

print(matplotlib.get_backend())  # matplotlib.use('Agg') # default not interactive
print(f'{plt.isinteractive() = }')  # TkAgg тоже пишет не интерактивный, но выводит figure?
# %matplotlib inline

df = pd.read_csv('BikeData2020.csv')

print(df.head(2))

# %matplotlib inline
plt.scatter(df['Temperature'], df['Humidity'])
plt.show()

# plt.show(block=True)


#********************************************************************

# type in terminal to lounch app.py
# python -m streamlit run app.py
# or
# streamlit run app.py
# %%
