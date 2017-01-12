def merge_sort (myList): #user interface
    merge_sort2(myList, 0, len(myList)-1) #recursive function with the passed list, a starting index and ending index

def merge_sort2(myList, first, last): #description of the recursive function merge_sort2
    if first < last: #if there's more than one item in the list
        middle = (first+last)//2 #division
        merge_sort2(myList, first, middle) #division
        merge_sort2(myList, middle+1, last) #division
        merge(myList, first, middle, last) #combination
        #print ("the divided list is:", myList)

def merge (myList, first, middle, last):
    L = myList[first:middle] #copy the first half of the list, to the left sublist
    R = myList[middle:last+1] #copy the second half of the list to the right sublist
    L.append (9999999999999)
    R.append (9999999999999)
    i=j=0 #indices for the left and right hand sides of the lists
    #print ("L list is:", L)
    #print ("R list is:", R)
    for k in range (first, last+1):
        if L[i]<R[j]:
            myList[k] = L[i]
            i +=1
        else:
            myList[k] = R[j]
            j +=1
    print (myList)

theList = [21, 130, 1005, 3, 17, 64, 30015, 2, 1467, 1]
print(merge_sort(theList))


def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid] # divide: 1st portion of the list
        righthalf = alist[mid:] # 2nd portion of the list

        mergeSort(lefthalf) # recursive calling itself
        mergeSort(righthalf) # recursive: calls itself again

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf): #
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1
        print (alist)
        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1

    print (alist)

alist = [21, 130, 1005, 3, 17, 64, 30015, 2, 1467, 1]
mergeSort(alist)
print(alist)
