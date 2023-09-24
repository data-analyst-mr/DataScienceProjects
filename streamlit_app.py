#!/usr/bin/env python
# coding: utf-8

# In[11]:


import streamlit as st
import pandas as pd


# In[12]:


st.title("A Simple Streamlit Web App")


# In[13]:


name = st.text_input("Enter your name", "")


# In[14]:


st.write(f"Hello {name}!")


# In[15]:


x = st.slider("Select an integer x", 0, 10, 1)
y = st.slider("Select an integer y", 0, 10, 1)


# In[16]:


df = pd.DataFrame({"x": [x], "y": [y] , "x + y": [x + y]}, index = ["addition row"])
st.write(df)


# In[ ]:




