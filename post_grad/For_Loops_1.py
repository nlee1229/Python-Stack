# 1. Basic - Print all integers from 0 to 150.
# for x in range (0, 151, 1):
#     print(x)

#or

# for x in range(151):
#     print(x)


# 2. Print all the multiples of 5 from 5 to 1,000
# for x in range(5, 1001, 5):
#     print(x)

# 3. Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo"
for x in range(1, 101, 1):
    if x % 5 == 0:
        print("Coding")
    if x % 10 == 0:
        print("Coding Dojo")
    else:
        print(x)
    