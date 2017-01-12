def sequentialSearch (alist, item):
    pos = 0
    found = False


    while pos < len(alist) and not found:
        if alist[pos] == item:
             found = True
        else:
            pos = pos + 1

    return found

print (sequentialSearch([2,3,6,5,1,9,8],7))