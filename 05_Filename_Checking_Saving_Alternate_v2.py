"""Program that creates a file from the user's input with information in the list.
This is an alternate version of 05_Filename_Checking_v2 and instead of separating items with commas, it adds a new item
on the next line. This version checks the filename to ensure that it is valid.
Jung Woo Yi
Version 2 – 31/08/2021
"""

# Importing
import re

# List that holds information
information = ['Qwerty', 'Hello', 'Hi', 'Temperature']

error = "yes"
while error == "yes":
    error = "no"
    filename = input("Filename: ")  # The user inputs a filename
    valid = "[A-Za-z0-9_]"
    for character in filename:
        if re.match(valid, character):
            continue
        elif character == " ":  # When the filename contains a space
            error_message = "The filename cannot contain a space"
        else:
            error_message = "The filename cannot contain {}".format(character)
        error = "yes"
        break

    # When the user does not enter anything for the filename
    if filename == "":
        error_message = "The filename cannot be blank"
        error = "yes"

    if error == "yes":
        print("Invalid: {}".format(error_message))
    else:
        print("Valid filename")

filename = filename + ".txt"  # Adds an extension
file = open(filename, "w+")

for i in information:
    file.write(i + "\n")  # Each piece of information is on a different line
file.close()
