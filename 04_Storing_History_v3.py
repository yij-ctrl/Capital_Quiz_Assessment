"""Program that stores history and prints all of the items entered and displays the most recent three items (if
applicable).
This version is an improvement to version 2 as it does not pop up with an error message when less than three items are
inputted.
Jung Woo Yi
Version 3 – 07/09/2021
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

# If the length of the list is greater than or equal to three, it will print the most recent three items
if len(inputs_list) >= 3:
    # Prints last 3 items
    for i in range(0, 3):
        print(inputs_list[i])
# If the length of the list is less than three, it will print all items in the list
elif len(inputs_list) < 3:  # If the length of the list is less than three
    for i in inputs_list:
        print(i)
