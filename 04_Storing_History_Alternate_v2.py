"""Program that stores history and prints all inputted items and the most recent 3.
This is the second version of the alternate version of 04_Storing_History_v1 that uses deque. This version allows the
user to input as many items as they want.
Jung Woo Yi
Version 2 – 31/08/2021
"""

# Importing
from collections import deque

inputs_list = deque()

# Inputting items
item = ""
while item != "q":
    item = input("Enter item: ")
    if item == "q":  # The user can enter 'q' to quit
        break
    inputs_list.appendleft(item)

print("\nALL ITEMS\n")
print(inputs_list)  # Prints all items that were inputted
print("\nLAST 3 ITEMS\n")
# Prints last 3 items
for i in range(0, 3):
    print(inputs_list[i])
