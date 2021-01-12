#1. Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big". Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]

def biggie_size(list):
    for i in range(len(list)):
        if list[i]>0:
            list[i]= "big"
    return list

print(biggie_size([-1, 3, 5, -5]))



#2. Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
#Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
#Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

def count_positives(list):
    counter = 0 #tracks the total # of positive values in the list  #3
    for i in range(len(list)):  #1
        if list[i]>0:  #2 is the specific value @ [i] positive?
            counter+=1 #or counter = counter+1  #4 
    list[len(list)-1] = counter #we are putting the counter in the given list
    return list

print(count_positives([1,6,-4,-2,-7,-2]))
print(count_positives([-1,1,1,1]))


#3. Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
#Example: sum_total([1,2,3,4]) should return 10
#Example: sum_total() should return 7

def sumTotal(list):
    sum = 0
    for i in range(len(list)):
        sum+=list[i]
    return sum

print(sumTotal([6,3,-2]))


#4. Average - Create a function that takes a list and returns the average of all the values.x
#Example: average([1,2,3,4]) should return 2.5
def average(list):
    sum=0
    avg=0
    for x in range(len(list)):
        sum+=list[x]
    avg= float(sum)/len(list) 
    
    return avg

print(average([1,2,3,4]))


#5. Length - Create a function that takes a list and returns the length of the list.
#Example: length([37,2,1,-9]) should return 4
#Example: length([]) should return 0

def length(list):
    return len(list)
print(length([37,2,1,-9]))




#6. Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
#Example: minimum([37,2,1,-9]) should return -9
#Example: minimum([]) should return False

def Minimum(x):
    if len(x) < 1:
        return "False"
    mini = 0
    for i in range (0, len(x), 1):
        if x[i] < mini:
            mini = x[i]
    return mini    
        
print(Minimum([37,2,1,-9]))


#7. Maximum - Create a function that takes a list and returns the maximum value in the list. If the list is empty, have the function return False.
#Example: maximum([37,2,1,-9]) should return 37
#Example: maximum([]) should return False

def Maximum(x): 
    if len(x) < 1:
        return "False"
    max = 0
    for i in range(0, len(x), 1):
        if x[i] > max:
            max= x[i]
    return max

print(Maximum([37,2,1,-9]))

#8. Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
#Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

def ultimate_analysis(list):
    results = {
        'sumTotal' : sum_total(list),
        'average' : average(list),
        'minimum' : Minimum(list),
        'maximum' : Maximum(list),
        'length' : length(list)
    }


#9. Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
#Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

def reverse_list(listy):
    listy.reverse()
    return listy
print(reverse_list([37,2,1,-9]))






