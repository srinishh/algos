import pandas as pd
from timeit import timeit




df = pd.read_excel("attendence.xlsx")
ali=df["marks"].tolist()
print("The unsorted array:")
print(ali)


def bubbleSort( theSeq ):
    
    n = len( theSeq )

    for i in range( n - 1 ) :
        flag = 0

        for j in range(n - 1) :
            
            if theSeq[j] > theSeq[j + 1] : 
                tmp = theSeq[j]
                theSeq[j] = theSeq[j + 1]
                theSeq[j + 1] = tmp
                flag = 1

        if flag == 0:
            break

    return theSeq


print('\nBubbleSorted Array in Ascending Order:')
print(bubbleSort(ali))
bubtime = timeit(lambda:bubbleSort(ali),number=10000)
print("execution_time_of_bubble_sort-",bubtime)

def selectionSort( itemsList ):
    n = len( itemsList )
    for i in range( n - 1 ): 
        minValueIndex = i

        for j in range( i + 1, n ):
            if itemsList[j] < itemsList[minValueIndex] :
                minValueIndex = j

        if minValueIndex != i :
            temp = itemsList[i]
            itemsList[i] = itemsList[minValueIndex]
            itemsList[minValueIndex] = temp

    return itemsList




print('\nSelectionSorted Array in Ascending Order:')
print(selectionSort(ali))
seltime = timeit(lambda:selectionSort(ali),number=10000)
print("execution_time_of_selectionSort-",seltime)



def insertion_sort(arr):
  
    for i in range(1, len(arr)): 
  
        val = arr[i]
  
        j = i-1
        while j >=0 and val < arr[j] : 
            arr[j+1] = arr[j] 
            j -= 1
        arr[j+1] = val
    
    return arr


print('\ninsertion_sort Array in Ascending Order:')
print(insertion_sort(ali))
instime = timeit(lambda:insertion_sort(ali),number=10000)
print("execution_time_of_insertion_sort-",instime)


def QuickSort(arr):

    elements = len(arr)
    
    #Base case
    if elements < 2:
        return arr
    
    current_position = 0 #Position of the partitioning element

    for i in range(1, elements): #Partitioning loop
         if arr[i] <= arr[0]:
              current_position += 1
              temp = arr[i]
              arr[i] = arr[current_position]
              arr[current_position] = temp

    temp = arr[0]
    arr[0] = arr[current_position] 
    arr[current_position] = temp #Brings pivot to it's appropriate position
    
    left = QuickSort(arr[0:current_position]) #Sorts the elements to the left of pivot
    right = QuickSort(arr[current_position+1:elements]) #sorts the elements to the right of pivot

    arr = left + [arr[current_position]] + right #Merging everything together
    
    return arr


print('\nQuickSort Array in Ascending Order:')
print(QuickSort(ali))
quitime = timeit(lambda:QuickSort(ali),number=10000)
print("execution_time_of_insertion_sort-",quitime)


def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0
        
        # Iterator for the main list
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              # The value from the left half has been used
              myList[k] = left[i]
              # Move the iterator forward
              i += 1
            else:
                myList[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1

myList = ali
mergeSort(myList)
print('\nmergeSort Array in Ascending Order:')
print(myList)
mertime = timeit(lambda:mergeSort(ali),number=10000)
print("execution_time_of_mergeSort-",mertime)

