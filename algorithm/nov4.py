
# Parens Valid
# Given an str that has parenthesis in it
# return whether the parenthesis are valid

# Input: "Y(3(p)p(3)r)s"
# Output: True

# Input: "N(0(p)3"
# Output: False

# Input: "N(0)t ) 0(k"
# Output: False

# Input: "a(b))(c"
# Output: False


def validate(stringy):
    count = 0
    for i in stringy:
        if count < 0:
            return False
        if i == '(':
            count += 1
        if i == ')':
            count -= 1
    if count != 0:
        return False
    else: 
        return True

print(validate("Y(3(p)p(3)r)s"))
print(validate("N(0(p)3"))
print(validate("N(0)t ) 0(k"))
print(validate("a(b))(c"))
