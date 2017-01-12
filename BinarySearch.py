def binarySearch(thelist, item):
    first = 0
    last = len(thelist) - 1
    found = False

    while first<=last and not found:
        midpoint = (first + last)//2
        if thelist[midpoint] == item:
            found = True
        else:
            if item < thelist [midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found
print(binarySearch([0, 1, 2, 8, 13, 17, 19, 32, 42,], 8))

def binarySearch2(alist, item2):
    if len(alist) == 0:
        return False
    else:
        midpoint2 = len(alist)//2
        if alist[midpoint2] == item2:
            return True
        else:
            if item2<alist[midpoint2]:
                return binarySearch2(alist[:midpoint2], item2)
            else:
                return binarySearch2(alist[midpoint2+1:], item2)

print(binarySearch2([0, 1, 2, 8, 13, 17, 19, 32, 42,], 7))


