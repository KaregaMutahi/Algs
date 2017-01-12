# selection sort
def selectionSort(myList):
    for i in range(len(myList)):  # outer loop
        min_idx = i  # first element is considered the minimum in the list
        for j in range(i + 1, len(myList)):  # the inner loop begins at the second item, i+1,
            if myList[min_idx] > myList[j]:  # compare...is the first item larger than the second item, then t
                min_idx = j  # if the first item is larger than the second item, then the second item becomes the minimum item...
        myList[i], myList[min_idx] = myList[min_idx], myList[i]  # swapping occurs here..
        print(myList)
    return myList


theList = [21, 130, 1005, 3, 17, 64, 30015, 2, 1467, 1]
print(selectionSort(theList))
