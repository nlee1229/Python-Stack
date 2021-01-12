
# Zip lists into dictionary

# Given two lists, create a dictionary containing keys from the first list, 
# and values from the second.

# Input: ["abc", 3, "yo"], [42, "wassup", True]
# Output: {
#   "abc": 42,
#   3: "wassup",
#   "yo": True,
# }

def zip_lists(key_list, value_list):
    for j in range(0, len(value_list)): 
        zip_dict = { i : value_list[j] for i in key_list}

    return zip_dict

key_list = ["abc", 3, "yo"]
value_list = [42, "wassup", True]

print(zip_lists(key_list, value_list))


# Invert Hash

# Given a dictionary, return a new dictionary that has the keys and the values 
# swapped so that the keys become the values and the values become the keys

# Input: { "name": "Zaphod", "charm": "high", "morals": "dicey" }
# Output: { "Zaphod": "name", "high": "charm", "dicey": "morals" }

def invert_hash(input_dict):
    inv_dict = { i: k for k, i in input_dict.items()}
    return str(inv_dict)

ini_dict = { "name": "Zaphod", "charm": "high", "morals": "dicey" }
print(invert_hash(ini_dict))
