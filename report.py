import time,threading,sys
from algorithm import *

sys.setrecursionlimit(10**8)
threading.stack_size(10**8)

def generateReport():
    iteration = 1
    ns = [10, 100, 1000]
    orders = [['Ascending', 1], ['Descending', 2], ['Random', 3]]
    plotData= {}
    for o in orders:
        for n in ns:
            #Merge Sort
            totalTime = 0
            for i in range(iteration):
                arr = getArray(n, o[1])
                start=time.time()
                mergeSort(arr,0,n-1)
                end=time.time()
                totalTime+=end-start
            print('Merge Sort, Order : '+o[0]+", n="+str(n)," Average time = "+str(totalTime/iteration)+"seconds")
            key='Merge Sort,'+o[0]+' Order'
            if not(key in plotData):
                plotData[key]=[]
            plotData[key].append(totalTime)
            # Quick Sort
            totalTime = 0
            for i in range(iteration):
                arr = getArray(n, o[1])
                start = time.time()
                quickSort(arr, 0, n - 1)
                end = time.time()
                totalTime += end - start
            print('Quick Sort, Order : ' + o[0] + ", n=" + str(n),
                  " Average time = " + str(totalTime / iteration) + "seconds")
            key = 'Quick Sort,' + o[0] + ' Order'
            if not (key in plotData):
                plotData[key] = []
            plotData[key].append(totalTime)
    print(plotData[list(plotData.keys())[0]])



t = threading.Thread(target=generateReport)
t.start()
t.join()