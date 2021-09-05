"""Program that runs a quiz based on capitals. It asks the users what the capital of a certain country is.
This version displays statistics to the user (e.g. how many were correct)
Jung Woo Yi
Version 7 – 05/08/2021
"""

# Importing
import random
from Capitals_List_v1 import capitals  # Importing the list of capitals from capitals_list

answered = 0
correct = 0

get_country = random.randint(0, len(capitals) - 1)  # This gets a list from within the whole list
country = capitals[get_country][1]  # This gets the country from the list
capital = capitals[get_country][0]  # This gets the respective capital for the country in the line above

question = ""
while question != "Q" and question != "q":
    # Asks the user the capital of the country
    question = input("What is the capital of {}? ".format(country))
    if question == capital:
        correct += 1
        answered += 1
        print("Correct\n")  # Message displayed when the answer is correct
        if len(capitals) > 0:
            capitals.pop(get_country)
        if len(capitals) > 0:
            get_country = random.randint(0, len(capitals) - 1)  # This gets a list from within the whole list
            country = capitals[get_country][1]  # This gets the country from the list
            capital = capitals[get_country][0]  # This gets the respective capital for the country in the line above
        else:
            print("Finished")  # Message displayed when the game is finished
            break
    elif question == "Q" or question == "q":
        # Displays statistics to the user
        print("\nNumber of questions answered correctly: {}\n"
              "Number of questions answered: {}\n"
              "Percentage: {:.2f}%".format(correct, answered, correct / answered * 100))
        break
    else:
        answered += 1
        print("Incorrect\n"
              "The correct answer was {}\n".format(capital))  # Message that is displayed when incorrect
