#  File: sorting.py
#  Description:
#  Student's Name: Julio Gonzalez
#  Student's UT EID: jcg3245
#  Course Name: CS 313E 
#  Unique Number: 51325
#
#  Date Created: 11/15/16
#  Date Last Modified: 11/15/16

import random
import time
import sys
sys.setrecursionlimit(10000)

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

def selectionSort(alist):
    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax = 0
        for location in range(1,fillslot+1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location
        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp


def insertionSort(alist):
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index

        while position>0 and alist[position-1]>currentvalue:
            alist[position] = alist[position-1]
            position = position-1

        alist[position] = currentvalue

def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist,startposition,sublistcount)
        sublistcount = sublistcount // 2

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):
        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position] = alist[position-gap]
            position = position - gap

        alist[position] = currentvalue

def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0

        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1

def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
    if first < last:
        splitpoint = partition(alist,first,last)
        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
    pivotvalue = alist[first]
    leftmark = first + 1
    rightmark = last
    done = False

    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark += 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark -= 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark

def main():

    listLength = 10
    print("Input type = Random")
    print("                   avg time    avg time    avgtime")
    print("  Sort function     (n=10)     (n=100)     (n=1000)")
    print("-------------------------------------------------------")
    print("     bubbleSort", end='')
    for i in range(3):
        myList = [i for i in range(listLength)]
        totaltime = 0
        random.shuffle(myList)
        for i in range(5):
            startTime = time.perf_counter()
            bubbleSort(myList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            totaltime += elapsedTime
        
        averagetime = round(totaltime/5, 6)
        
        print ("   ", '%-7s' % averagetime, end = ' ')
        listLength = listLength*10
        
    listLength = 10
    print()
    print("  selectionSort", end='')
    for i in range(3):
        myList = [i for i in range(listLength)]
        totaltime = 0
        random.shuffle(myList)
        for i in range(5):
            startTime = time.perf_counter()
            selectionSort(myList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            totaltime += elapsedTime
        
        averagetime = round(totaltime/5, 6)
        
        print ("   ", '%-7s' % averagetime, end = ' ')
        listLength = listLength*10

    listLength = 10
    print()
    print("  insertionSort", end='')
    for i in range(3):
        myList = [i for i in range(listLength)]
        totaltime = 0
        random.shuffle(myList)
        for i in range(5):
            startTime = time.perf_counter()
            insertionSort(myList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            totaltime += elapsedTime
        
        averagetime = round(totaltime/5, 6)
        
        print ("   ", '%-7s' % averagetime, end = ' ')
        listLength = listLength*10

    listLength = 10
    print()
    print("      shellSort", end='')
    for i in range(3):
        myList = [i for i in range(listLength)]
        totaltime = 0
        random.shuffle(myList)
        for i in range(5):
            startTime = time.perf_counter()
            shellSort(myList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            totaltime += elapsedTime
        
        averagetime = round(totaltime/5, 6)
        
        print ("   ", '%-7s' % averagetime, end = ' ')
        listLength = listLength*10
        
    listLength = 10
    print()
    print("      mergeSort", end='')
    for i in range(3):
        myList = [i for i in range(listLength)]
        totaltime = 0
        random.shuffle(myList)
        for i in range(5):
            startTime = time.perf_counter()
            mergeSort(myList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            totaltime += elapsedTime
        
        averagetime = round(totaltime/5, 6)
        
        print ("   ", '%-7s' % averagetime, end = ' ')
        listLength = listLength*10
        
    listLength = 10
    print()
    print("      quickSort", end='')
    for i in range(3):
        myList = [i for i in range(listLength)]
        totaltime = 0
        random.shuffle(myList)
        for i in range(5):
            startTime = time.perf_counter()
            quickSort(myList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            totaltime += elapsedTime
        
        averagetime = round(totaltime/5, 6)
        
        print ("   ", '%-7s' % averagetime, end = ' ')
        listLength = listLength*10
        
#####################################################################################
    print()
    print()
    listLength = 10
    print("Input type = Sorted")
    print("                   avg time    avg time    avgtime")
    print("  Sort function     (n=10)     (n=100)     (n=1000)")
    print("-------------------------------------------------------")
    print("     bubbleSort", end='')
    for i in range(3):
        myList = [i for i in range(listLength)]
        totaltime = 0
        for i in range(5):
            startTime = time.perf_counter()
            bubbleSort(myList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            totaltime += elapsedTime
        
        averagetime = round(totaltime/5, 6)
        
        print ("   ", '%-7s' % averagetime, end = ' ')
        listLength = listLength*10
        
    listLength = 10
    print()
    print("  selectionSort", end='')
    for i in range(3):
        myList = [i for i in range(listLength)]
        totaltime = 0
        for i in range(5):
            startTime = time.perf_counter()
            selectionSort(myList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            totaltime += elapsedTime
        
        averagetime = round(totaltime/5, 6)
        
        print ("   ", '%-7s' % averagetime, end = ' ')
        listLength = listLength*10

    listLength = 10
    print()
    print("  insertionSort", end='')
    for i in range(3):
        myList = [i for i in range(listLength)]
        totaltime = 0
        for i in range(5):
            startTime = time.perf_counter()
            insertionSort(myList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            totaltime += elapsedTime
        
        averagetime = round(totaltime/5, 6)
        
        print ("   ", '%-7s' % averagetime, end = ' ')
        listLength = listLength*10

    listLength = 10
    print()
    print("      shellSort", end='')
    for i in range(3):
        myList = [i for i in range(listLength)]
        totaltime = 0
        for i in range(5):
            startTime = time.perf_counter()
            shellSort(myList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            totaltime += elapsedTime
        
        averagetime = round(totaltime/5, 6)
        
        print ("   ", '%-7s' % averagetime, end = ' ')
        listLength = listLength*10
        
    listLength = 10
    print()
    print("      mergeSort", end='')
    for i in range(3):
        myList = [i for i in range(listLength)]
        totaltime = 0
        for i in range(5):
            startTime = time.perf_counter()
            mergeSort(myList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            totaltime += elapsedTime
        
        averagetime = round(totaltime/5, 6)
        
        print ("   ", '%-7s' % averagetime, end = ' ')
        listLength = listLength*10
        
    listLength = 10
    print()
    print("      quickSort", end='')
    for i in range(3):
        myList = [i for i in range(listLength)]
        totaltime = 0
        for i in range(5):
            startTime = time.perf_counter()
            quickSort(myList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            totaltime += elapsedTime
        
        averagetime = round(totaltime/5, 6)
        
        print ("   ", '%-7s' % averagetime, end = ' ')
        listLength = listLength*10
#####################################################################################
    print()
    print()
    listLength = 10
    print("Input type = Reverse")
    print("                   avg time    avg time    avgtime")
    print("  Sort function     (n=10)     (n=100)     (n=1000)")
    print("-------------------------------------------------------")
    print("     bubbleSort", end='')
    for i in range(3):
        myList = [i for i in range(listLength)]
        myList.reverse()
        totaltime = 0
        for i in range(5):
            startTime = time.perf_counter()
            bubbleSort(myList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            totaltime += elapsedTime
        
        averagetime = round(totaltime/5, 6)
        
        print ("   ", '%-7s' % averagetime, end = ' ')
        listLength = listLength*10
        
    listLength = 10
    print()
    print("  selectionSort", end='')
    for i in range(3):
        myList = [i for i in range(listLength)]
        myList.reverse()
        totaltime = 0
        for i in range(5):
            startTime = time.perf_counter()
            selectionSort(myList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            totaltime += elapsedTime
        
        averagetime = round(totaltime/5, 6)
        
        print ("   ", '%-7s' % averagetime, end = ' ')
        listLength = listLength*10

    listLength = 10
    print()
    print("  insertionSort", end='')
    for i in range(3):
        myList = [i for i in range(listLength)]
        myList.reverse()
        totaltime = 0
        for i in range(5):
            startTime = time.perf_counter()
            insertionSort(myList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            totaltime += elapsedTime
        
        averagetime = round(totaltime/5, 6)
        
        print ("   ", '%-7s' % averagetime, end = ' ')
        listLength = listLength*10

    listLength = 10
    print()
    print("      shellSort", end='')
    for i in range(3):
        myList = [i for i in range(listLength)]
        myList.reverse()
        totaltime = 0
        for i in range(5):
            startTime = time.perf_counter()
            shellSort(myList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            totaltime += elapsedTime
        
        averagetime = round(totaltime/5, 6)
        
        print ("   ", '%-7s' % averagetime, end = ' ')
        listLength = listLength*10
        
    listLength = 10
    print()
    print("      mergeSort", end='')
    for i in range(3):
        myList = [i for i in range(listLength)]
        myList.reverse()
        totaltime = 0
        for i in range(5):
            startTime = time.perf_counter()
            mergeSort(myList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            totaltime += elapsedTime
        
        averagetime = round(totaltime/5, 6)
        
        print ("   ", '%-7s' % averagetime, end = ' ')
        listLength = listLength*10
        
    listLength = 10
    print()
    print("      quickSort", end='')
    for i in range(3):
        myList = [i for i in range(listLength)]
        myList.reverse()
        totaltime = 0
        for i in range(5):
            startTime = time.perf_counter()
            quickSort(myList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            totaltime += elapsedTime
        
        averagetime = round(totaltime/5, 6)
        
        print ("   ", '%-7s' % averagetime, end = ' ')
        listLength = listLength*10

####################################################################################
    print()
    print()
    listLength = 10
    print("Input type = Almost sorted")
    print("                   avg time    avg time    avgtime")
    print("  Sort function     (n=10)     (n=100)     (n=1000)")
    print("-------------------------------------------------------")
    print("     bubbleSort", end='')
    for i in range(3):
        myList = [i for i in range(listLength)]
        totaltime = 0
        for i in range(10):
            randomIndex = random.randint(0,len(myList))
            randomIndex2 = random.randint(0,len(myList))
            myList[randomIndex-2], myList[randomIndex2-3] = myList[randomIndex2-3], myList[randomIndex-2]
        for i in range(5):
            startTime = time.perf_counter()
            bubbleSort(myList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            totaltime += elapsedTime
        
        averagetime = round(totaltime/5, 6)
        
        print ("   ", '%-7s' % averagetime, end = ' ')
        listLength = listLength*10
        
    listLength = 10
    print()
    print("  selectionSort", end='')
    for i in range(3):
        myList = [i for i in range(listLength)]
        totaltime = 0
        randomIndex = random.randint(0,len(myList))
        for i in range(5):
            startTime = time.perf_counter()
            selectionSort(myList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            totaltime += elapsedTime
        
        averagetime = round(totaltime/5, 6)
        
        print ("   ", '%-7s' % averagetime, end = ' ')
        listLength = listLength*10

    listLength = 10
    print()
    print("  insertionSort", end='')
    for i in range(3):
        myList = [i for i in range(listLength)]
        totaltime = 0
        randomIndex = random.randint(0,len(myList))
        for i in range(5):
            startTime = time.perf_counter()
            insertionSort(myList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            totaltime += elapsedTime
        
        averagetime = round(totaltime/5, 6)
        
        print ("   ", '%-7s' % averagetime, end = ' ')
        listLength = listLength*10

    listLength = 10
    print()
    print("      shellSort", end='')
    for i in range(3):
        myList = [i for i in range(listLength)]
        totaltime = 0
        randomIndex = random.randint(0,len(myList))
        for i in range(5):
            startTime = time.perf_counter()
            shellSort(myList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            totaltime += elapsedTime
        
        averagetime = round(totaltime/5, 6)
        
        print ("   ", '%-7s' % averagetime, end = ' ')
        listLength = listLength*10
        
    listLength = 10
    print()
    print("      mergeSort", end='')
    for i in range(3):
        myList = [i for i in range(listLength)]
        totaltime = 0
        randomIndex = random.randint(0,len(myList))
        for i in range(5):
            startTime = time.perf_counter()
            mergeSort(myList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            totaltime += elapsedTime
        
        averagetime = round(totaltime/5, 6)
        
        print ("   ", '%-7s' % averagetime, end = ' ')
        listLength = listLength*10
        
    listLength = 10
    print()
    print("      quickSort", end='')
    for i in range(3):
        myList = [i for i in range(listLength)]
        totaltime = 0
        randomIndex = random.randint(0,len(myList))
        for i in range(5):
            startTime = time.perf_counter()
            quickSort(myList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            totaltime += elapsedTime
        
        averagetime = round(totaltime/5, 6)
        
        print ("   ", '%-7s' % averagetime, end = ' ')
        listLength = listLength*10
main()

    
