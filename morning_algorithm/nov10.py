
# Missing Value

# You are given a list of length N that contains, in no particular order,
# integers from 0 to N . One integer value is missing.
# Quickly determine and return the missing value.

# Input: [3, 0, 1]
# Output: 2

# Input: [3, 0, 1, 2]
# Output: None


def missingVal(someList, N):
    otherList = []
    #run through the input or list
    for i in range(N):
        #appending(adds an element to the end like push), #otherList is the new list that will come out
        otherList.append(i)
    #this list goes through range
    for i in range(len(otherList)):
        #checks if it is not in the list, if not then it return the value
        if otherList[i] not in someList:
            return otherList[i]
    
    return None
print(missingVal(thisList,3))





# First Non-Reapeated

# Given a list of integers

# Return the first integer from the list that is not repeated anywhere else
# If there are multiple non-repeated integers in the list,
# the "first" one will be the one with the lowest index.

# Input: [3, 5, 5]
# Output: 3

# Input: [3, 3, 5]
# Output: 5

# Input: [3, 5, 4, 3, 4, 6, 5]
# Output: 6

# Input: [5]
# Output: 5

# Input: []
# Output: None


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