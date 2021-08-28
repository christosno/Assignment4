import math
from operator import attrgetter

##########################################################
# ascending
##########################################################

# quick sort

def QuickSortAscending(arr, left, right, attr):
    if left < right :
        partision_pos = partisionAsceding(arr, left, right, attr)
        QuickSortAscending(arr, left, partision_pos - 1, attr)
        QuickSortAscending(arr, partision_pos + 1, right, attr)


def partisionAsceding(arr, left, right, attr):
    i = left
    j = right - 1
    pivot = getattr(arr[right], attr)

    while i < j:

        while i < right and getattr(arr[i], attr) < pivot:
            i += 1

        while j > left and getattr(arr[j], attr) >= pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    if getattr(arr[i], attr) > pivot:
        arr[i], arr[right] = arr[right], arr[i]

    return i

# bubble sort

def BubbleSortAscending(arr, attr):
    
    n = len(arr)

    for i in range(n-1):

        for j in range(0, n-i-1):

            if getattr(arr[j], attr) > getattr(arr[j + 1], attr):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr 

# bucket sort

def BucketSortAscending(arr, attr):

    max_ele = max(arr, key=attrgetter(attr))
    min_ele = min(arr, key=attrgetter(attr))
    max_ele = getattr(max_ele, attr)
    min_ele = getattr(min_ele, attr)
    noOfBuckets = int(math.sqrt(max_ele - min_ele))
 
    rnge = (max_ele - min_ele) / noOfBuckets
    temp = []
 
    for i in range(noOfBuckets):
        temp.append([])
 
    for i in range(len(arr)):
        diff = (getattr(arr[i], attr) - min_ele) / rnge - int((getattr(arr[i], attr) - min_ele) / rnge)
 
        if(diff == 0 and (getattr(arr[i], attr) != min_ele)):
            temp[int(((getattr(arr[i], attr) - min_ele) / rnge)) - 1].append(arr[i])
 
        else:
            temp[int(((getattr(arr[i], attr) - min_ele) / rnge))].append(arr[i])

    for i in range(len(temp)):
        if len(temp[i]) != 0:

            def tshirtAttr(tshirt):
                return (getattr(tshirt, attr))

            temp[i].sort(key=tshirtAttr)
 
    k = 0
    for lst in temp:
        if lst:
            for i in lst:
                arr[k] = i
                k = k+1


##########################################################
#  descending
##########################################################

# quick sort 
def QuickSortDescending(arr, left, right, attr):
    if left < right :
        partision_pos = partisionDesceding(arr, left, right, attr)
        QuickSortDescending(arr, left, partision_pos - 1, attr)
        QuickSortDescending(arr, partision_pos + 1, right, attr)


def partisionDesceding(arr, left, right, attr):
    i = left
    j = right - 1
    pivot = getattr(arr[right], attr)

    while i < j:

        while i < right and getattr(arr[i], attr) > pivot:
            i += 1

        while j > left and getattr(arr[j], attr) <= pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    if getattr(arr[i], attr) < pivot:
        arr[i], arr[right] = arr[right], arr[i]

    return i

# bubble sort
def BubbleSortDescending(arr, attr):
    
    n = len(arr)

    for i in range(n-1):

        for j in range(0, n-i-1):

            if getattr(arr[j], attr) < getattr(arr[j + 1], attr):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr 

# bucket sort
def BucketSortDescending(arr, attr):

    max_ele = max(arr, key=attrgetter(attr))
    min_ele = min(arr, key=attrgetter(attr))
    max_ele = getattr(max_ele, attr)
    min_ele = getattr(min_ele, attr)
    noOfBuckets = int(math.sqrt(max_ele - min_ele))
 
    rnge = (max_ele - min_ele) / noOfBuckets
    temp = []
 
    for i in range(noOfBuckets):
        temp.append([])
 
    for i in range(len(arr)):
        diff = (getattr(arr[i], attr) - min_ele) / rnge - int((getattr(arr[i], attr) - min_ele) / rnge)
 
        if(diff == 0 and (getattr(arr[i], attr) != min_ele)):
            temp[int(((getattr(arr[i], attr) - min_ele) / rnge)) - 1].append(arr[i])
 
        else:
            temp[int(((getattr(arr[i], attr) - min_ele) / rnge))].append(arr[i])
 
    for i in range(len(temp)):
        if len(temp[i]) != 0:

            def tshirtAttr(tshirt):
                return (getattr(tshirt, attr))

            temp[i].sort(reverse= True, key=tshirtAttr)
 
    k = 0
    for i in range(len(temp) - 1, -1, -1):
        if temp[i]:
            for j in temp[i]:
                arr[k] = j
                k = k+1


