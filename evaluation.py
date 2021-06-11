import random,time,sys,threading
from algorithm import *

sys.setrecursionlimit(10**6)
threading.stack_size(10**8)

def evaluate(n,order):
    arr=[]
    offset=random.randint(-512,512)
    if order==1:
        for i in range(n):
            arr.append(random.randint(i*4,(i+1)*4)+offset)
    elif order==2:
        for i in range(n):
            arr.append(random.randint((n-i-2)*4,(n-i-1)*4)+offset)
    elif order==3:
        arr=random.sample(range(1+offset,n*4+offset), n)
    duplicateArr=arr.copy()
    start=time.time()
    mergeSort(arr,0,n-1)
    end=time.time()
    print("Time taken by merge sort : "+str(end-start)+"seconds...")
    start = time.time()
    quickSort(duplicateArr, 0, n-1)
    end = time.time()
    print("Time taken by quick sort : " + str(end - start) + "seconds...")

def takeInput():
    print("Enter the length of array")
    n = int(input())
    if n<0:
        print("invalid input")
        takeInput()
        return
    print("Enter array ordering:")
    print("1.Ascending")
    print("2.Descending")
    print("3.Random")
    order = int(input())
    if order==1 or order==2 or order==3:
        evaluate(n,order)
        takeInput()
    else:
        print("invalid input")
        takeInput()

t = threading.Thread(target=takeInput)
t.start()
t.join()
