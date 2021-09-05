"""Program that runs a quiz based on capitals.
Jung Woo Yi
Version 1 – 02/08/2021
"""

# Importing
import random

# List that contains capitals and countries (this is for test purposes)
capitals = [['Wellington', 'New Zealand'], ['Canberra', 'Australia'], ['Washington D.C.', 'United States of America']]

get_country = random.randint(0, 2)  # This gets a list from within the whole list
country = capitals[get_country][1]  # This gets the country from the list
capital = capitals[get_country][0]  # This gets the respective capital for the country in the line above
print(country)
print(capital)

# Asks the user the capital of the country
question = input("What is the capital of {}? ".format(country))
if question == capital:
    print("Correct")  # Displays result
else:
    print("Incorrect")
