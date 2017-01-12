def insertionSort(myList):
    for i in range (1, len(myList)):
        for j in range (i-1, -1, -1): #begin the inner loop on the left-hand side of the outer-loop, and continually move to the left hand side....
            if myList[j]>myList[j+1]:
                myList[j],myList[j+1] = myList[j+1], myList[j]
            else:
                break #if the list is already sorted, the loop breaks and begins at the next position
            print(myList)

theList = [21, 130, 1005, 3, 17, 64, 30015, 2, 1467, 1]
print(insertionSort(theList))

def insertionSort2(secondList):
    for i in range (1, len(secondList)):
        j = i-1
        while secondList[j]>secondList[j+1] and j>=0:
            secondList[j], secondList[j+1] = secondList[j+1], secondList[j]
            j=j-1
        print(secondList)

print(insertionSort2(theList))

def insertionSort3(thirdList):
    for i in range (1, len(thirdList)):
        curNum = thirdList[i]
        for j in range (i-1, -1, -1):
            if thirdList[j]>curNum:
                thirdList[j+1] = thirdList [j]
            else:
                thirdList[j+1] = curNum
                break
    print(thirdList)

print(insertionSort3(theList))


