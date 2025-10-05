### Приложение-демонстратор возможностей `streamlit`
Основа взята из [blog.skillfactory.ru](https://blog.skillfactory.ru/kak-napisat-veb-prilozhenie-dlya-demonstratsii-data-science-proekta-na-python/)

Используются:  <br>
- `df = st.cache_data(pd.read_csv)("BikeData2020.csv")`  чтение данных
- `st.title(),   st.header(),   st.subheader()`
- `st.write(), st.markdown()`
- `st.selectbox(),  st.multiselect(),  st.sidebar`
- `st.scatter_chart(df, x=col_x, y=col_y)`  
- `st.plotly_chart(fig)`   with plotly_express
