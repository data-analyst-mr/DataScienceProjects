#!/usr/bin/env python
# coding: utf-8

# In[11]:


import streamlit as st
import pandas as pd
from datetime import datetime

df = pd.read_csv('preprocessed_dataset.csv')

# In[12]:


st.title("Стоимость автомобиля")


# In[13]: 

maker = st.selectbox(label="Производитель: ",
                     options=tuple(df['make'].unique()),
                     index=None,
                     placeholder="Выберите производителя"
                    )

df = df.loc[df['make'] == maker]

model_name = st.selectbox(label="Модель: ",
                     options=tuple(df['model'].unique()),
                     index=None,
                     placeholder="Выберите модель",
                    )

df = df.loc[df['model'] == model_name]
try:
    year_start = int(df['year'].min())
    year = st.number_input(label="Год выпуска: ",
                           min_value=year_start,
                           max_value=datetime.now().year,
                           placeholder="Укажите год выпуска"
                          )

    car_age = datetime.now().year - year


    today = datetime.today()
    week = today.isocalendar()[1]

    trim = st.selectbox(label="Модификация: ",
                    options=("jjjjjj", "gggg"),
                    index=None,
                    placeholder="Выберите модификацию",
                   )

    body = st.selectbox(label="Тип кузова: ",
                    options=("jjjjjj", "gggg"),
                    index=None,
                    placeholder="Выберите тип кузова",
                   )

    transmission = st.selectbox(label="Тип КПП: ",
                            options=("jjjjjj", "gggg"),
                            index=None,
                            placeholder="Выберите тип КПП",
                           )

    color = st.selectbox(label="Цвет кузова: ",
                     options=("jjjjjj", "gggg"),
                     index=None,
                     placeholder="Выберите цвет кузова",
                    )

    odometer = st.number_input(label="Пробег (мили): ",
                           min_value=0,
                           max_value=500000,
                           placeholder="Укажите пробег"
                          )


    condition = st.radio(label="Состояние автомобиля: ",
                     options=(1, 2, 3, 4, 5))

    if condition == 1:
        interior = st.selectbox(label="Цвет интерьера: ",
                        options=("jjjjjj", "gggg"),
                        index=None,
                        placeholder="Выберите цвет интерьера"
                       )

    state = st.selectbox(label="Регион: ",
                     options=("jjjjjj", "gggg"),
                     index=None,
                     placeholder="Выберите регион",
                    )
except:
    pass

# In[15]:


x = st.slider("Select an integer x", 0, 10, 1)
y = st.slider("Select an integer y", 0, 10, 1)


# In[16]:


df = pd.DataFrame({"x": [x], "y": [y] , "x + y": [x + y]}, index = ["addition row"])
st.write(df)


# In[ ]:




