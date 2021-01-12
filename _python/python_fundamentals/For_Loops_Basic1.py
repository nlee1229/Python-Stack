#1. Basic - Print all integers from 0 to 150.
for x in range(0, 151, 1):
    print(x)

or 

for x in range(151): 
    print(X)

#2. Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for x in range(5, 1001, 5):
    print(x)

#3. Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for x in range(1, 101, 1): 
    if x % 5 == 0:
        print("Coding") #this is how to modulus in python
    if x % 10 == 0:
        print("Coding Dojo")

#4. Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
sum = 0
for x in range(0, 500001, 1): 
    if x % 2 == 1:
        sum = sum + x
print(sum)  

#5. Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for x in range(2018, 0, -4):
    print(x)


#6. Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
def flexCounter (lowNum, highNum, mult):
    for x in range (lowNum, highNum+1):
        if x % mult == 0:
            print(x)
            
flexCounter(2,9,3)

def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))
