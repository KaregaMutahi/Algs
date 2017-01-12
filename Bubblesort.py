#Bubble sort implementation
def bubbleSort(myList):
    for i in range (0, len(myList)-1): #Number of passes
        for j in range (0, len(myList)-1-i): #For each pass, execute the following
            if myList[j]> myList[j+1]: #Comparing the two numbers
                myList[j], myList[j+1] = myList[j+1], myList[j] #swapping the two numbers, from left no. to right no.
                print(myList)

    return myList
theList = [21,130,1005,3,17,64,30015,2,1467,1]
print(bubbleSort(theList))


