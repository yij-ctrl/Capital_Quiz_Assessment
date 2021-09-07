"""Program that stores history and prints all of the items entered and displays the most recent three items.
This version allows the user to input as many items as they want compared to a set number of items (five) that the user
has to input in version 1.
Jung Woo Yi
Version 2 – 07/09/2021
"""

# List to store inputs
inputs_list = []

# Inputting items
item = ""
while item != "q":
    item = input("Enter item: ")
    if item == "q":  # The user can enter 'q' to quit
        break
    inputs_list.append(item)

inputs_list.reverse()
print("\nALL ITEMS\n")
print(inputs_list)  # Prints all items that were inputted
print("\nLAST 3 ITEMS\n")

# Prints last 3 items
for i in range(0, 3):
    print(inputs_list[i])
