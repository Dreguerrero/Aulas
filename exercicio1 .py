#!/usr/bin/env python
# coding: utf-8

# In[1]:


lista = [6,7,4,7,8,4,2,5,7,'um','dois']


# In[2]:


len (lista)


# In[3]:


sublist = [x for x in lista if isinstance(x, int)]


# In[4]:


print(sublist)


# In[7]:


x= sum (sublist)


# In[8]:


print(x)


# In[9]:


med = x/len(lista)


# In[10]:


print(med)


# In[ ]:




