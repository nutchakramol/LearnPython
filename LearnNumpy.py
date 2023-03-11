#!/usr/bin/env python
# coding: utf-8

# array need to store 1 type of data it can has 3 dimention
# 

# In[2]:


import numpy as np
import sys


# In[4]:


arrayy=np.array(1)
arrayy
arrayy.ndim


# In[89]:


num=np.array([1,3,5],dtype='int16')
num


# In[90]:


num+2


# In[5]:


num.dtype


# In[13]:


num.itemsize


# In[12]:


num.size


# Accessingh changing specific elements rows columns

# In[43]:


a=np.array([[1,3,5,7,9,11,13,15],[0,2,4,6,8,10,12,14]])
print(a)


# get specific elements [row,column]
# **index start with 0 **

# In[46]:


a[1,2]


# In[45]:


a[0,-4]


# In[44]:


a[:,1]


# In[53]:


# [start:end:step size]
a[0,0:5:2]


# In[54]:


a[1,4]=88
print(a)


# In[55]:


a[:,3]=[14,15]
print(a)


# In[57]:


#size of column in each row should be equal

b1=np.array([[[1,3],[2,4]],[[10,20,30],[5,15,25]]])


# In[59]:


b2=np.array([[[1,3],[2,4]],[[10,20],[5,15]]])
print(b2)


# all o. matrix

# In[61]:


np.zeros((2,4))


# In[66]:


np.zeros((2,4,1,3))


# In[65]:


np.full((2,2),18)


# In[67]:


np.identity(6)


# In[68]:


aray=np.array([[1,3,5]])
ab=np.repeat(aray,3,axis=0)
print(ab)


# In[88]:


#ur ans
all=np.ones((5,5))
all[1:4,1:4]=0

all[2,2]=9
all


# In[ ]:


#t ans


# In[83]:


al=np.ones((5,5))
zero=np.zeros((3,3))
zero[1,1]=9

al[1:4,1:4] = zero

al


# In[ ]:




