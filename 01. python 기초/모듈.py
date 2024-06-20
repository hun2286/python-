#!/usr/bin/env python
# coding: utf-8

# In[1]:


A = 1
B = 2

def add(*args) :
    return sum(args)


# In[ ]:


get_ipython().system('jupyter nbconvert --to script 04.모듈.ipynb')

# ! -> python 언어가 아닌 프롬프트 명렁어(스크립트문)

