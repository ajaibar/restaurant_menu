#!/usr/bin/env python
# coding: utf-8

# In[14]:


def my_func(st):
    for index in range(len(st)):
        if index % 2 == 0:
            return st.upper()
        else:
            return st.lower()


# In[15]:


capitalize('jaibar')


# In[ ]:





# In[50]:


def alternate_capitalization(st):
    result=[]
    list1=''
    list2=''
    for char in range(len(st)):
        if char % 2 == 0:
            list1=list1 + (st[char].upper())
            list2= list2+ (st[char].lower())
        else:
            list2= list2 + (st[char].upper())
            list1= list1 + (st[char].lower())
    result.append (list1)
    result.append (list2)
    return result        


# In[51]:


alternate_capitalization('montecarlos')


# In[ ]:




