import random
import time
L = []
for i in range(1000):
    L.append(random.randint(0,1001))
start=time.clock()
for i in range(len(L)):
    min=i
    for j in range(i+1,len(L)):
        if L[j] < L[min]:
            min=j
    L[i],L[min]=L[min],L[i]
end=time.clock()
print L
print ("The program ran for:")
print (end-start)
print ("seconds")
