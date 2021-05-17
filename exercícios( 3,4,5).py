#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


x = np.array([[1,1,2,3,4,5,3],[0,1,1,2,3,4,5],[0,1,1,2,3,4,5],[0,7,2,2,3,4,5],[0,1,1,2,3,8,7]])


# In[3]:


x.T
#transposta


# In[4]:


x.sum() #soma de todos os elementos 


# In[5]:


x.sum(axis=0) #soma de colunas


# In[6]:


x.sum(axis=1) #soma de linhas


# In[7]:


x.max() #retorna maior valor


# In[8]:


x.min() #menor valor


# In[9]:


j = np.array([[1,1,2,3,4],[4,5,2,3,4],[1,1,2,3,4],[3,5,2,3,4],[1,1,2,3,4]])


# In[10]:


teste_soma = j*x #soma de matrizes de ordem diferentes


# In[11]:


z = np.arange (0,1001)


# In[ ]:




