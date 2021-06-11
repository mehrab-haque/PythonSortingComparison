import time,sys,threading
from tabulate import tabulate
from algorithm import *

sys.setrecursionlimit(10**8)
threading.stack_size(10**8)

def evaluate(n,order):
    arr=getArray(n,order)
    duplicateArr=arr.copy()
    start=time.time()
    mergeSort(arr,0,n-1)
    end=time.time()
    print("Time taken by merge sort : "+str(end-start)+"seconds...")
    start = time.time()
    quickSort(duplicateArr, 0, n-1)
    end = time.time()
    print("Time taken by quick sort : " + str(end - start) + "seconds...")
    tableData=[['Merge Sort','Quick Sort']]
    for i in range(n):
        tableData.append([arr[i],duplicateArr[i]])
    print(tabulate(tableData, headers='firstrow', tablefmt='fancy_grid'))

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

