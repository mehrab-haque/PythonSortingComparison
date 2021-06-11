import time,threading,sys
import matplotlib.pyplot as plt
import numpy as np
from algorithm import *

sys.setrecursionlimit(10**8)
threading.stack_size(10**8)

iteration = 2
ns = list(range(400))
orders = [['Ascending', 1], ['Descending', 2], ['Random', 3]]

def plot(plotData):
    colors=['red','green','black','orange','blue','pink']
    fig, ax = plt.subplots()
    for key in list(plotData.keys()):
        ax.plot(ns, plotData[key], color=colors[list(plotData.keys()).index(key)], label=key)
    ax.set(xlabel='n', ylabel='Average Time (seconds)',
           title='Merge Sort vs Quick Sort ('+str(iteration)+' iterations averaged for each case)')
    ax.grid()
    plt.legend()
    plt.show()

def generateReport():
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
    plot(plotData)



t = threading.Thread(target=generateReport)
t.start()
t.join()