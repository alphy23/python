#!/usr/bin/env python
# coding: utf-8

# In[9]:


print("Binary to Decimal Conversion")
a=int(intput("Enter the binary number"))
n=len(a)
x=int(a)
def con(x,n):
    temp=0
    for i in range(0,n):
        dec = x % 10
        temp = dec + 2**1
        x//=10
        return temp
    z = con(x,n)
    print("Decimal no. is:",z)
    


# In[35]:


def con(n):
    s=0
    i=0
    while(n>0):
        r = n%10
        s = s+r*(2**1)
        i = i+1
        n = n//10
        print(s)
        a = int(input("Enter the binary value :"))
    print("Decimal number is:")
    count(a)


# In[ ]:





# In[34]:


print("hello")


# In[36]:


def con(n):
    s=0
    i=0
    while(n>0):
        r = n%10
        s = s+r*(2**1)
        i = i+1
        n = n//10
        print(s)
        a = int(input("Enter the binary value :"))
    print("Decimal number is:")
    count(a)


# In[50]:


def con(n):
    s=0
    i=0
    while(n>0):
        r = n%10
        s = s+r*(2**i)
        i = i+1
        n = n//10
    print(s)
a = int(input("Enter the binary value :"))
print("Decimal number is:")
con(a)


# In[61]:


def sum(num):
    sum = 0
    for i in range(1,num+1):
        sum = sum+i
    return sum
num=int(input("Enter the limit:"))
z = sum(num)
print("The sum till",z)


# In[ ]:




