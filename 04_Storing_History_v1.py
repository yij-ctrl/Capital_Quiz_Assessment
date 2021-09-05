"""Program that stores history and prints all of the 5 inputted items and the most recent 3.
Jung Woo Yi
Version 1 – 31/08/2021
"""

# List to store inputs
inputs_list = []

for i in range(0, 5):  # The user can input 5 items
    item = input("Enter item: ")
    inputs_list.append(item)

inputs_list.reverse()
print("\nALL ITEMS\n")
print(inputs_list)  # Prints all 5 items that were inputted
print("\nLAST 3 ITEMS\n")

# Prints last 3 items
for i in range(0, 3):
    print(inputs_list[i])
