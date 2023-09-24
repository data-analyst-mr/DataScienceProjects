#!/usr/bin/env python
# coding: utf-8

# In[11]:


import streamlit as st
import pandas as pd
from datetime import datetime


# In[12]:


st.title("Стоимость автомобиля")


# In[13]:


year = st.number_input("Год выпуска", min_value=1900, max_value=datetime.now().year)

maker = st.selectbox("Производитель", options=["jjjjjj", "gggg"], placeholder="Select contact method...")


# In[15]:


x = st.slider("Select an integer x", 0, 10, 1)
y = st.slider("Select an integer y", 0, 10, 1)


# In[16]:


df = pd.DataFrame({"x": [x], "y": [y] , "x + y": [x + y]}, index = ["addition row"])
st.write(df)


# In[ ]:




