#!/usr/bin/env python
# coding: utf-8

# In[1]:


list1 = [1,2,3,4,5,6,7,8]
list2 = ["a","b","c","d","e"]
minlen = min(len(list1), len(list2))

#dict1[list1[i]] = list2[i] for i in range(minlen)

dict1 = { list1[i] : list2[i] for i in range(minlen) }

print(dict1)


# In[ ]:




