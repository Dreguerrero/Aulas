#!/usr/bin/env python
# coding: utf-8

# In[3]:


def calculadora (valor_1, valor_2, conta):
  x=int()
  y=int()

x = int (input('valor_1:'))
y = int (input('valor_2:'))
operação = input('conta:')

if (operação=="+"):
  print( x + y)

elif (operação=="*"):
  print( x * y)

elif (operação=="-"):
  print( x - y)

elif (operação=="**"):
  print( x ** y)

elif operação=="/" and (y !=0):
  print(x / y)

else:
  print('erro')


# In[ ]:




