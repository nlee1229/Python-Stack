
# Given a string containing space separated words
# Reverse each word in the string.
# If you need to, use .split to start, then try to do it without.

# Input: "hello" .split()
# Output: "olleh"

# Input: "hello world".split(' ') =  ['hello','world']
# Output: "olleh dlrow"

# Input: "abc def ghi"
# Output: "cba fed ihg"
            ihg fed cba


def reverse(stringy):
    newList = stringy.split()
    for i in range(len(newList)):
        work = list(newList[i])
        for j in range(round(len(work)/2)):
            work[j], work[len(work)-1-j] = work[len(work)-1-j], work[j]
        newList[i] = "".join(work)
    return " ".join(newList)

print(reverse("abc def ghi"))

OR

def reverse(stringy):
    newString = stringy.split(" ")
    for i in range(len(newString)):
        newString[i] = newString[i].reverse()
    return " ".join(newString)




# Given a string,
# return a new string with the duplicates excluded
# Bonus: Keep only the last instance of each character.

# Input: "abcABC"
# Output: "abcABC"

# Input: "helloo"
# Output: "helo"




