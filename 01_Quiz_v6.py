"""Program that runs a quiz based on capitals. It asks the users what the capital of a certain country is.
This version is improved compared to version 5 as it imports the capitals/countries.
Jung Woo Yi
Version 6 – 05/08/2021
"""

# Importing
import random
from capitals_list_v1 import capitals  # Importing the list of capitals from capitals_list

get_country = random.randint(0, len(capitals) - 1)  # This gets a list from within the whole list
country = capitals[get_country][1]  # This gets the country from the list
capital = capitals[get_country][0]  # This gets the respective capital for the country in the line above

question = ""
while question != "Q" and question != "q":
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
    elif question == "Q" or question == "q":
        break
    else:
        print("Incorrect\n"
              "The correct answer was {}".format(capital))
