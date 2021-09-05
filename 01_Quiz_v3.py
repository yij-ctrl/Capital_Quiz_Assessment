"""Program that runs a quiz based on capitals. It asks users what the capital of a country is.
This version is more efficient when compared to version 2 as it uses 'len'.
Jung Woo Yi
Version 3 – 02/08/2021
"""

# Importing
import random

# List that contains capitals and countries
capitals = [['Wellington', 'New Zealand'], ['Canberra', 'Australia'], ['Washington D.C.', 'United States of America']]

get_country = random.randint(0, 2)  # This gets a list from within the whole list
country = capitals[get_country][1]  # This gets the country from the list
capital = capitals[get_country][0]  # This gets the respective capital for the country in the line above

question = ""
while question != "Q":
    # Asks the user the capital of the country
    question = input("What is the capital of {}? ".format(country))
    if question == capital:
        print("Correct")
        if len(capitals) > 0:
            capitals.pop(get_country)
        if len(capitals) > 0:
            get_country = random.randint(0, len(capitals) - 1)  # This gets a list from within the whole list
            country = capitals[get_country][1]  # This gets the country from the list
            capital = capitals[get_country][0]  # This gets the respective capital for the country in the line above
        else:
            print("Finished")
            break
    else:
        print("Incorrect")
