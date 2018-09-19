
# coding: utf-8

# In[29]:


def fib2(x):
    n1 = 0
    n2 = 1
    count = 0
    if x <= 0:
        print("Please enter a positive integer")
    elif x == 1:
        print("Fibonacci sequence upto",x,":")
        print(n1)
    else:
        print("Fibonacci sequence upto",x,":")
        while count < x:
            print(n1,end=' , ')
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1

