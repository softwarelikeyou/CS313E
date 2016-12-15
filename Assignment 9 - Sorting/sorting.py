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

## Bulko's code above, my code below

# return a list based on the sort strategy
def listFactory(inputType, listLength):
    myList = [i for i in range(listLength)]
    myList.sort()
    if inputType == 'Random':
        random.shuffle(myList)
    elif inputType == 'Sorted':
        pass
    elif inputType == 'Reverse':
        myList.reverse()
    elif inputType == 'Almost sorted':
        n = int(len(myList) * .1)
        for i in range(n):
            ## TODO: why is it throwing an IndexError exception?
            try:
                randomIndex = random.randint(0,len(myList))
                temp = myList[i]
                myList[i] = myList[randomIndex]
                myList[randomIndex] = temp
            except IndexError:
                pass
    else:
        print('Invalid Input Type: ' + inputType)
        sys.exit()

    return myList

# return the average time for a sortFuction
def sortFunctionFactory(sortFunction, myList):
    count = 0
    while count < 5:
        startTime = time.perf_counter()
        if sortFunction == 'bubbleSort':
            bubbleSort(myList)
        elif sortFunction == 'selectionSort':
            selectionSort(myList)
        elif sortFunction == 'insertionSort':
            insertionSort(myList)
        elif sortFunction == 'shellSort':
            shellSort(myList)
        elif sortFunction == 'mergeSort':
            mergeSort(myList)
        elif sortFunction == 'quickSort':
            quickSort(myList)
        else:
            print('Invalid Sort Function: ' + sortFunction)
            sys.exit()
        endTime = time.perf_counter()
        elapsedTime = 0
        elapsedTime += endTime - startTime
        count += 1
    return format(float(elapsedTime/count), '.6f')

class Result:
    def __init__(self, inputType, listLength, sortFunction, average):
        self.inputType = inputType
        self.listLength = listLength
        self.sortFunction = sortFunction
        self.average = average

    def __str__(self):
        return self.inputType + ':' + str(self.listLength) + ':' + self.sortFunction + ':' + str(self.average)

class Average:
    def __init__(self, ten, hundred, thousand):
        self.ten = ten
        self.hundred = hundred
        self.thousand = thousand

    def __str__(self):
        return '{:>4}'.format(' ') + str(self.ten) + '{:>3}'.format(' ') + str(self.hundred) + '{:>3}'.format(' ') + str(self.thousand)
    
def main():

    inputTypes = ['Random', 'Sorted', 'Reverse', 'Almost sorted']
    listLengths = [10, 100, 1000]
    sortFunctions = ['bubbleSort', 'selectionSort', 'insertionSort', 'shellSort', 'mergeSort', 'quickSort']

    results = []
    
    for inputType in inputTypes:
        for listLength in listLengths:
            myList = listFactory(inputType, listLength)
            for sortFunction in sortFunctions:
                average = str(sortFunctionFactory(sortFunction, myList))
                result = Result(inputType, listLength, sortFunction, average)
                results.append(result)

    inputTypesDict = {}
    sortsDict = {'bubbleSort': Average(0.0,0.0,0.0), 'selectionSort': Average(.0,0.0,0.0), 'insertionSort': Average(.0,0.0,0.0), 'shellSort': Average(.0,0.0,0.0), 'mergeSort': Average(.0,0.0,0.0), 'quickSort': Average(.0,0.0,0.0)}
     
    for inputType in inputTypes:
        printInputTypeHeaders = True
        if printInputTypeHeaders:
            print('Input type = ' + inputType)
            print('                    avg time   avg time   avg time')
            printInputTypeHeaders = False
        for result in results:
            if inputType == result.inputType:
                average = sortsDict.get(result.sortFunction)
                if result.listLength == 10:
                    average.ten = result.average
                if result.listLength == 100:
                    average.hundred = result.average
                if result.listLength == 1000:
                    average.thousand = result.average
        printSortFunctionHeaders = True
        if printSortFunctionHeaders:
            print('   Sort function     (n=10)    (n=100)    (n=1000)')
            print('-----------------------------------------------------')
            printSortFunctionHeaders = False
        for sortFunction in sortFunctions:
            average = sortsDict.get(sortFunction)
            print('{:>16}'.format(sortFunction) + str(average))
        print()
        print()
       
main()
