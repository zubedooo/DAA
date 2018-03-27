import random
import time
def partition(arr,low,high):
    i = ( low-1 )
    pivot = arr[high]
    for j in range(low , high):
        if   arr[j] <= pivot:
                     i = i+1;arr[i],arr[j] = arr[j],arr[i]

    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 ) #pivot - single pivot
def quickSort(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
arr =[]
def repeat(n):
        for i in range(n):
                arr.append(random.randint(0,51))
        start=time.clock()
        quickSort(arr,0,n-1)
        end=time.clock()
        print "Time taken to sort array of size ",n,": ", end-start,"seconds"
for i in range(1,6):
        repeat(500*i)
