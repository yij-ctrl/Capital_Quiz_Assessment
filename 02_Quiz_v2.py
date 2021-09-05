"""Program that runs a quiz based on capitals.
Jung Woo Yi
Version 2 – 02/08/2021
"""

# Importing
import random

# List that contains capitals and countries
capitals = [['Wellington', 'New Zealand'], ['Canberra', 'Australia'], ['Washington D.C.', 'United States of America']]
completed = []

get_country = random.randint(0, 2)  # This gets a list from within the whole list
country = capitals[get_country][1]  # This gets the country from the list
capital = capitals[get_country][0]  # This gets the respective capital for the country in the line above
print(country)
print(capital)

question = ""
while len(completed) < 3:
    # Asks the user the capital of the country
    question = input("What is the capital of {}? ".format(country))
    if question == capital:
        print("Correct")
        completed.append(country)
        get_country = random.randint(0, 2)  # This gets a list from within the whole list
        country = capitals[get_country][1]  # This gets the country from the list
        capital = capitals[get_country][0]  # This gets the respective capital for the country in the line above
        while country == [completed]:
            get_country = random.randint(0, 2)  # This gets a list from within the whole list
            country = capitals[get_country][1]  # This gets the country from the list
            capital = capitals[get_country][0]  # This gets the respective capital for the country in the line above
    else:
        print("Incorrect")
