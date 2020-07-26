#!/usr/bin/env python
# coding: utf-8

# In[1]:


ls=[0,1,2,10,4,1,0,56,2,0,1,3,0,56,0,4]
ls.sort()
ls1=[]
ls2=[]
ls2=[]
for i in ls:
    if i==0:
        ls1.append(i)
    if i>0:
        ls2.append(i)
ls3=ls2+ls1
print(ls3)


# In[2]:


list1=[10,20,40,60,70,80] 
list2=[5,15,25,35,45,60] 
list3=list1+list2
print(sorted(list3))


# In[3]:


# Python3 code to demonstrate 
# to combine two sorted list 
# using naive method 

# initializing lists 
test_list1 = [10,20,40,60,70,80] 
test_list2 = [5,15,25,35,45,60] 

# printing original lists 
print ("The original list 1 is : " + str(test_list1)) 
print ("The original list 2 is : " + str(test_list2)) 

# using naive method 
# to combine two sorted lists 
size_1 = len(test_list1) 
size_2 = len(test_list2) 

res = [] 
i, j = 0, 0

while i < size_1 and j < size_2:
    if test_list1[i] < test_list2[j]:
        res.append(test_list1[i])
        i += 1
    else:
        res.append(test_list2[j])
        j += 1

res = res + test_list1[i:] + test_list2[j:] 

# printing result 
print ("The combined sorted list is : " + str(res)) 


# In[ ]:




