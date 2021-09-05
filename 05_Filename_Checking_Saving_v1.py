"""Program that creates a file from the user's input with information in the list.
Jung Woo Yi
Version 1 – 31/08/2021
"""

# List that holds information
information = ['Qwerty', 'Hello', 'Hi', 'Temperature']

filename = input("Filename: ")  # The user inputs a filename
file = open(filename, "w+")

for i in information:
    file.write(i)
file.close()
