#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# # Exercise 1: Create a 4X2 integer array and Prints its attributes

# In[10]:


a=np.array([[64392,31655],[32579,0],[49248,462],[0,0]])
print("Printing Array")
print(a)
print("Printing NumPy array Attributes")
print("Array Shape is:  ",a.shape,"\nArray dimensions are  ",a.ndim,"\nLength of each element of array in bytes is ", a.itemsize)


# # Exercise 2: Create a 5X2 integer array from a range between 100 to 200 such that the difference between each element is 10

# In[17]:


b=np.zeros((5,2))
b
for i in range(100,200+1,10):
    for b in


# In[19]:


#the ans
num=np.arange(100,200,10)
print(num)
num=num.reshape(5,2)
print(num)


# # Exercise 3: Following is the provided numPy array. Return array of items by taking the third column from all rows

# In[22]:


Array = np.array([[11 ,22, 33], [44, 55, 66], [77, 88, 99]])
print("Printing array of items in the third column from all rows\n",Array[:,2])


# # Exercise 4: Return array of odd rows and even columns from below numpy array

# In[24]:


ay = np.array([[3 ,6, 9, 12], [15 ,18, 21, 24],[27 ,30, 33, 36], [39 ,42, 45, 48], [51 ,54, 57, 60]])
y=ay[::2,1::2]
print(y)


# # Exercise 5: Create a result array by adding the following two NumPy arrays. Next, modify the result array by calculating the square of each element

# In[27]:


arrayOne = np.array([[5, 6, 9], [21 ,18, 27]])
arrayTwo = np.array([[15 ,33, 24], [4 ,7, 1]])
re=arrayOne+arrayTwo
re**2


# # Exercise 6: Split the array into four equal-sized sub-arrays

# In[ ]:





# # Exercise 7: Sort following NumPy array

# In[ ]:





# # Exercise 8: Print max from axis 0 and min from axis 1 from the following 2-D array.

# In[ ]:





# # Exercise 9: Delete the second column from a given array and insert the following new column in its place.

# In[ ]:





# # Exercise 10: Create two 2-D arrays and Plot them using matplotlib

# In[ ]:





# # 

# # 

# # 

# # 

# # 
