#1. Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).  Example: countdown(5) should return [5,4,3,2,1,0]

def countdown(i): 
    list_countdown = []
    for x in range(i,-1,-1):
        list_countdown.append(x)
    return list_countdown

print(countdown(5))


#2. Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second. Example: print_and_return([1,2]) should print 1 and return 2

def print_and_return(pr_list):
    print(pr_list[0]) #printing the first item in the list(which is at index0)
    return pr_list[1]

print(print_and_return([1,2]))


#3. First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)

def first_plus_length(flp_list):
    return flp_list[0] + len(flp_list)

print(first_plus_length([1,2,3,4,5]))


#4. Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False... Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]...Example: values_greater_than_second([3]) should return False

def greater_than_second(value_list):
    new_list = []
    if(value_list<2):
        return False
    else: 
        for x in range(0, len(value_list), 1): 
            if(value_list[x]>value_list[1]):
                new_list.append(value_list[x])

        print(len(new_list))
        return new_list

print(greater_than_second([5,2,3,2,1,4]))

#5. This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value. Example: length_and_value(4,7) should return [7,7,7,7] Example: length_and_value(6,2) should return [2,2,2,2,2,2]

def this_length(size,value): 
    new_list = []
    for i in range(0, size, 1): #or you can just put (size)#range counts from 0 to that size
        new_list.append(value) #when you call it, that is when value is defined... last part of the question

    return new_list

print(this_length(4,7))