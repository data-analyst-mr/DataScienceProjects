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
                     options=tuple(sorted(df['make'].unique())),
                     index=None,
                     placeholder="Выберите производителя"
                    )

df = df.loc[df['make'] == maker]

model_name = st.selectbox(label="Модель: ",
                     options=tuple(sorted(df['model'].unique())),
                     index=None,
                     placeholder="Выберите модель",
                    )

df_filtered = df.loc[df['model'] == model_name]
try:
    year_start = int(df_filtered['year'].min())
    year = st.number_input(label="Год выпуска: ",
                           min_value=year_start-5,
                           max_value=datetime.now().year,
                           placeholder="Укажите год выпуска"
                          )

    car_age = datetime.now().year - year


    today = datetime.today()
    week = today.isocalendar()[1]

    trim_name = st.selectbox(label="Модификация: ",
                    options=tuple(sorted(df['trim'].unique())),
                    index=None,
                    placeholder="Выберите модификацию",
                   )

    df_filtered = df_filtered.loc[df_filtered['trim'] == trim_name]
    body_name = st.selectbox(label="Тип кузова: ",
                    options=tuple(sorted(df['body'].unique())),
                    index=None,
                    placeholder="Выберите тип кузова",
                   )

    df_filtered = df_filtered.loc[df_filtered['body'] == body_name]
    transmission_name = st.selectbox(label="Тип КПП: ",
                            options=tuple(sorted(df['transmission'].unique())),
                            index=None,
                            placeholder="Выберите тип КПП",
                           )
    
    color_name = st.selectbox(label="Цвет кузова: ",
                     options=tuple(sorted(df['color'].unique())),
                     index=None,
                     placeholder="Выберите цвет кузова",
                    )
    

    odometer_name = st.number_input(label="Пробег (мили): ",
                           min_value=0,
                           max_value=1500000,
                           placeholder="Укажите пробег"
                          )


    condition_name = st.radio(label="Состояние автомобиля: ",
                     options=(1, 2, 3, 4, 5))

    interior_name = st.selectbox(label="Цвет интерьера: ",
                            options=tuple(sorted(df['interior'].unique())),
                            index=None,
                            placeholder="Выберите цвет интерьера"
                           )

    state_name = st.selectbox(label="Регион: ",
                     options=tuple(sorted(df['state'].unique())),
                     index=None,
                     placeholder="Выберите регион",
                    )
except:
    pass

# In[15]:

import pickle

filename = 'catboost_model.pkl'
model = pickle.load(open(filename, 'rb'))

data = [{'maker': maker_name, 'model': model_name, 'year': year_name, 'car_age': car_age, 'year': year_name, 'week': week_name,
         'body': body_name, 'transmission': transmission_name, 'color': color_name, 'odometer': odometer_name,
         'condition': condition_name, 'interior': interior_name, 'state': state_name, 'trim': trim_name}] 
df_pred = pd.DataFrame(data)

y_pred = model.predict(df_pred)

st.write(y_pred)


x = st.slider("Select an integer x", 0, 10, 1)
y = st.slider("Select an integer y", 0, 10, 1)


# In[16]:


df = pd.DataFrame({"x": [x], "y": [y] , "x + y": [x + y]}, index = ["addition row"])
st.write(df)


# In[ ]:




