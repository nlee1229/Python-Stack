def oddOut(someList):
    count = 0
    #loop through both lists
    for i in range(len(someList)):
        for j in range(len(someList)):
            #increment counter if duplicates of the i list are found in j
            if someList[i] == someList[j]:
                count += 1
        
        #reset counter if duplicates were found and begin loop again
        if count > 1:
            count = 0
        #if no matches are found, return the value of the list at current index
        else:
            return someList[i]

    #if the loops end without finding any non-duplicates, return none
    return None

test1 = [3, 5, 5]
test2 = [3, 3, 5]
test3 = [3, 5, 4, 3, 4, 6, 5]

print(oddOut(test1))