import random
from sorting import QuickSortAscending, BubbleSortAscending, BucketSortAscending, QuickSortDescending, BubbleSortDescending, BucketSortDescending
from strategy import T_shirt, colors, sizes, fabrics

################################################
################################################
# present the three sort algorithms

# 1. quick sort 
def quicksort(arr, left, right):
    if left < right :
        partision_pos = partision(arr, left, right)
        quicksortAscending(arr, left, partision_pos - 1)
        quicksortAscending(arr, partision_pos + 1, right)

def partision(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]

    while i < j:

        while i < right and arr[i] < pivot:
            i += 1

        while j > left and arr[j] >= pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]

    return i

# 2. bubble sort 
def bubble_sort(arr):
    
    n = len(arr)

    for i in range(n-1):

        for j in range(0, n-i-1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr 

# 3. bucket sort
def bucketSort(arr, noOfBuckets):
    max_ele = max(arr)
    min_ele = min(arr)
 
    rnge = (max_ele - min_ele) / noOfBuckets
    print('range', rnge)
 
    temp = []
 
    for i in range(noOfBuckets):
        temp.append([])
 
    for i in range(len(arr)):
        diff = (arr[i] - min_ele) / rnge - int((arr[i] - min_ele) / rnge)
 
        if(diff == 0 and arr[i] != min_ele):
            temp[int((arr[i] - min_ele) / rnge) - 1].append(arr[i])
 
        else:
            temp[int((arr[i] - min_ele) / rnge)].append(arr[i])
 
    for i in range(len(temp)):
        if len(temp[i]) != 0:
            temp[i].sort()
 
    k = 0
    for lst in temp:
        if lst:
            for i in lst:
                arr[k] = i
                k = k+1

########################################################
########################################################
# create forty(40) random T-shirts

def tShirt_generator():
    t_shirts = []

    for i in range(40):

        color = random.randint(1, len(colors))
        size = random.randint(1, len(sizes))
        fabric = random.randint(1, len(fabrics))

        t_shirt = T_shirt(color, size, fabric)
        t_shirts.append(t_shirt)
    
    return t_shirts

####################################################
####################################################
# all the sortings algorithms for each of t-shirt attributes and the combination of them, 
# both ascending and descending

# ask the user for the continuation of the main program
def Continue():
    print()
    choice = input("Continue?\n\t1: Yes\n\t2: No\n\t ->")
    while choice not in ["1", "2"]:
        print("Sorry, i don't understand")
        print("Please chose again, 1 for Yes, 2 for No")
        choice = input("Continue?\n\t1: Yes\n\t2: No\n\t ->")
    return choice

# user choose the criteria of sorting
def Sort_by():
    choiceDic = {"1":"size", "2":'color', "3":'fabric', "4":"sizeColorFabric"} 
    print()
    print("\t\t~ Sort By ~")
    choice = input("\n\t1: Size\n\t2: Color\n\t3: Fabric\n\t4: Size, Color and Febric\n\t ->")
    while choice not in ["1", "2", "3", "4"]:
        print("Sorry, i don't understand")
        print("Please chose again a number between 1-4")
        choice = input("\n\t1: Size\n\t2: Color\n\t3: Fabric\n\t4: Size, Color and Febric\n\t ->")
    return choiceDic[choice]

# user choose the algorithm of sorting
def Sorting_Algorithm():
    print()
    print("\t\t~ Sort Algorithm ~")
    choice = input("\n\t1: Qiuck sort in Ascending\n\t2: Quick sort in Descending\n\t3: Bubble sort in Ascending\n\t4: Bubble sort in Descending\n\t"
                       "5: Bucket sort in Ascending\n\t6: Bucket sort in Descending\n\t ->")
                       
    while choice not in ["1", "2", "3", "4", "5", "6"]:
        print("Sorry, i don't understand")
        print("Please chose again a number between 1-7")
        choice = input("\n\t1: Qiuck sort in Ascending\n\t2: Quick sort in Descending\n\t3: Bubble sort in Ascending\n\t4: Bubble sort in Descending\n\t"
                       "5: Bucket sort in Ascending\n\t6: Bucket sort in Descending\n\t ->")

    return choice

#main

if __name__ == '__main__':

    cont = None

    # create forty random t-shirts
    t_shirts = tShirt_generator()

    while cont != '2':

        # choose the criteria of sorting
        sortBy = Sort_by()
        # choose the algorithm
        sortingAlgorithm = Sorting_Algorithm()

        if sortingAlgorithm == "1":
            print("~ Quick sort ascending")
            QuickSortAscending(t_shirts, 0, len(t_shirts) - 1, sortBy)
        
        elif sortingAlgorithm == "2":
            print("~ Quick sort descending")
            QuickSortDescending(t_shirts, 0, len(t_shirts) - 1, sortBy)
        
        elif sortingAlgorithm == "3":
            print("~ Bubble sort ascending")
            BubbleSortAscending(t_shirts, sortBy)
        
        elif sortingAlgorithm == "4":
            print("~ Bubble sort descending")
            BubbleSortDescending(t_shirts, sortBy)
        
        elif sortingAlgorithm == '5':
            print("~ Bucket sort ascending")
            BucketSortAscending(t_shirts, sortBy)
        
        else:
            print("~ Bucket sort descending")
            BucketSortDescending(t_shirts, sortBy)

        # print the t-shirts
        for count, tshirt in enumerate(t_shirts):
            print("{}.".format(count + 1))
            print(tshirt, "\n\t")
            
        
        cont = Continue()

        