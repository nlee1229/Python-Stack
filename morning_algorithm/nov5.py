# Given an array of dictionaries to represent new inventory,
# and an array of dictionaries to represent current inventory,
# update the quantities of the current inventory

# if the item doesn't exist in current inventory, add it to the inventory
# return the current inventory after updating it.

# new_inv = [
#   { name: "Grain of Rice", quantity: 9000 },
#   { name: "Peanut Butter", quantity: 50 },
#   { name: "Royal Jelly", quantity: 20 },
# ]
# curr_inv = [
#   { name: "Peanut Butter", quantity: 20 },
#   { name: "Grain of Rice", quantity: 1 },
# ]

# expected = [
#   { name: "Peanut Butter", quantity: 70 },
#   { name: "Grain of Rice", quantity: 9001 },
#   { name: "Royal Jelly", quantity: 20 },
# ]

def update_inventory(new_inv, curr_inv):
    for i in range:
        if new_inv[i]['name'] == curr_inv[i]['name']:
            curr_inv[i]['quantity'] += new_inv[i]['quantity']
        else:
            curr_inv.append(new_inv[i])
    return curr_inv

update_inventory(new_inv, curr_inv)
update_inventory(curr_inv)

THIS IS A COMMON WAY TO RECEIVE DATA IN API
