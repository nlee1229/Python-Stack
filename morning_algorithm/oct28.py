
# String Encode
# You are given a string that may contain sequences of consecutive characters.
# Create a function to shorten a string by including the character,
# then the number of times it appears. 

# Input: "aaaabbcddd"
# Output: "a4b2c1d3"

# Input: "aaaAAA"
# Output: "a3A3"

# Input: "abcd"
# Output: "????"

# Input: "bbcc"
# Output: "b2c2"

def encode(stringx):
    count = 1 
    if stringx == "": #we are taking care of the exception here"
        return (f'""') #if the string is empty, it will return an empty string
    workList = [stringx[0]] #if it's not empty, that means there is content in the string
    for i in range (len(stringx)): #we go in in order to go through entire list and see what we can compress it from
        if i == len(stringx)-1: #exception case where you have hit the final character. Once you hit the final character, there is nothing to compare it to
            workList.append(str(count))
        elif stringx[i] == stringx[i+1]: # if character i = i+1 then increase the count by 1. saying if there is another same letter, we increase the count on this
            count += 1
        elif (stringx[i] != stringx[i+1]): 
            workList.append(str(count))
            count = 1 #resetting the count bc we're going back to 1 in the new character
            workList.append(stringx[i+1]) #return new char. in the list

    return "".join(workList)

print(encode("aaaabbcddd"))
print(encode("aaaAAA"))
print(encode("abcd"))
print(encode("bbcc"))
print(encode(""))


# String Decode

# Given an encoded string using the algorithm above, decode the string
# to the original format

# Input: "a4b2c1d3"
# Output: "aaaabbcddd"

# Input: "b2c2"
# Output: "bbcc"

# def decode(stringx):


def decode(stringx):
    retList = []
    if stringx == "":
        return (f'""')
    for i in range(len(stringx)):
        if i%2 == 0:
            retList.append(stringx[i])
        elif i%2 == 1:
            for j in range(int(stringx[i])-1):
                retList.append(stringx[i-1])
    return "".join(retList)

print(decode("a4b2c1d3"))
print(decode("b2c2"))