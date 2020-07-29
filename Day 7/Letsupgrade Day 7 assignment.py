#!/usr/bin/env python
# coding: utf-8

# In[1]:


port1 = {21: "FTP", 22:"SSH", 23: "telnet", 80: "http"}
print(port1)

port1 = {value:key for key, value in port1.items()}
print(port1)


# In[3]:


ls1 = [(1,2), (3,4), (5,6),(4,5)]
ls2 = []
for n in ls1:
    ls2.append(n[0] + n[1])
    
print(ls2)


# In[4]:


list1=[(1,2,3),[1,2],['a','hit','less']]

list2=[i for each in list1 for i in each]
print (list2)


# In[ ]:




