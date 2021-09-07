"""Program that creates a file from the user's input with information in the list.
This version adds a '.txt' extension to the filename. This version also has commas in between the items to separate
them.
Jung Woo Yi
Version 2 – 31/08/2021
"""

# List that holds information
information = ['Qwerty', 'Hello', 'Hi', 'Temperature']

filename = input("Filename: ")  # The user inputs a filename
filename = filename + ".txt"  # Adds an extension
file = open(filename, "w+")

for i in information:
    file.write(i + ", ")
file.close()
