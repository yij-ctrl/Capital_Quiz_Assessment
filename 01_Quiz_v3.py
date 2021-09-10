"""Program that runs a quiz based on capitals. It asks the users what the capital of a certain country is.
This version displays statistics at the end of the game which the previous version did not do.
Jung Woo Yi
Version 3 – 09/08/2021
"""

# Importing
import random
from Capitals_List_v2 import capitals  # Importing the list of capitals from capitals_list

answered = 0  # This is the number of questions answered
correct = 0  # This is the number of questions that were answered correctly

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
        print("Correct\n")
        if len(capitals) > 0:
            capitals.pop(get_country)
        if len(capitals) > 0:
            get_country = random.randint(0, len(capitals) - 1)  # This gets a list from within the whole list
            country = capitals[get_country][1]  # This gets the country from the list
            capital = capitals[get_country][0]  # This gets the respective capital for the country in the line above
        else:
            print("Finished")
            print("\nNumber of questions answered correctly: {}\n"
                  "Number of questions answered: {}\n"
                  "Percentage: {:.2f}% (2 d. p.)".format(correct, answered, correct / answered * 100))
            break
    elif question == "Q" or question == "q":
        if answered == 0:
            print("Finished")
            break
        else:
            print("\nNumber of questions answered correctly: {}\n"
                  "Number of questions answered: {}\n"
                  "Percentage: {:.2f}% (2 d. p.)".format(correct, answered, correct / answered * 100))
            break
    else:
        answered += 1
        print("Incorrect\n"
              "The correct answer was {}\n".format(capital))
        if len(capitals) > 0:
            capitals.pop(get_country)
        if len(capitals) > 0:
            get_country = random.randint(0, len(capitals) - 1)  # This gets a list from within the whole list
            country = capitals[get_country][1]  # This gets the country from the list
            capital = capitals[get_country][0]  # This gets the respective capital for the country in the line above
        elif len(capitals) == 0:
            # Displays statistics at the end of the game
            print("Finished\n"
                  "Number of questions answered correctly: {}\n"
                  "Number of questions answered: {}\n"
                  "Percentage: {:.2f}% (2 d. p.)".format(correct, answered, correct / answered * 100))
            break
