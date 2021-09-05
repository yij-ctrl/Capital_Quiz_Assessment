"""Program that creates a file from the user's input with information in the list.
This is an alternate version of 05_Filename_Checking_v2 and instead of separating items with commas, it adds a new item
on the next line.
Jung Woo Yi
Version 1 – 31/08/2021
"""

# List that holds information
information = ['Qwerty', 'Hello', 'Hi', 'Temperature']

filename = input("Filename: ")  # The user inputs a filename
filename = filename + ".txt"  # Adds an extension
file = open(filename, "w+")

for i in information:
    file.write(i + "\n")  # Each piece of information is on a different line
file.close()
