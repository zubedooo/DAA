import random
import time
def merge(a,b):
        m,c = [],0
        if a[0] <= b[0]:
                m.append(a.pop(0))
        else:
                c += len(a)
                m.append(b.pop(0))
        m += a
        m += b
        return m,c
def sort(arr):
        if len(arr) <= 1:
                return arr,0
        mid = len(arr)//2
        b,r1 = sort(arr[:mid])
        c,r2 = sort(arr[mid:])
        d,c = merge(b,c)
        return d,(r1+r2+c)
x = []
n=int(input("Enter size: "))
for i in range(n):
        x.insert(i,int(input("Enter Values: ")))
start = time.clock()
s,c = sort(x)
end = time.clock()
print "Initial list: ",x
print "Sortred list: ",s
print "Number of Invertions: ",c
print "Time :",end-start,"seconds"
