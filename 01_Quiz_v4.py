"""Program that runs a quiz based on capitals. It asks the users what the capital of a certain country is.
This version is improved in terms of future-proofing and is easier to use due to using 'len' instead of using the actual
range of the list.
Jung Woo Yi
Version 4 – 02/08/2021
"""

# Importing
import random

# List that contains capitals and countries  (for testing purposes)
capitals = [['Wellington', 'New Zealand'], ['Canberra', 'Australia'], ['Washington D.C.', 'the United States of America'],
            ['Seoul', 'the Republic of Korea'], ['Ottawa', 'Canada']]

get_country = random.randint(0, len(capitals) - 1)  # This gets a list from within the whole list
country = capitals[get_country][1]  # This gets the country from the list
capital = capitals[get_country][0]  # This gets the respective capital for the country in the line above

question = ""
while question != "Q":
    # Asks the user the capital of the country
    question = input("What is the capital of {}? ".format(country))
    if question == capital:
        print("Correct")  # Displays a message when the user gets the answer right
        if len(capitals) > 0:
            capitals.pop(get_country)
        if len(capitals) > 0:
            get_country = random.randint(0, len(capitals) - 1)  # This gets a list from within the whole list
            country = capitals[get_country][1]  # This gets the country from the list
            capital = capitals[get_country][0]  # This gets the respective capital for the country in the line above
        else:
            print("Finished")  # Displays a message when the user is finished
            break
    else:
        print("Incorrect")  # Displays a message when the user gets the answer wrong
