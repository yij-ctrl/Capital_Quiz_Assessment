"""Program that runs a quiz based on capitals. It asks the users what the capital of a certain country is.
This version allows the user to quit on the first question without crashing.
Jung Woo Yi
Version 9 – 09/08/2021
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
        print("Correct\n")  # Message displayed when the answer is right
        if len(capitals) > 0:
            capitals.pop(get_country)
        if len(capitals) > 0:
            get_country = random.randint(0, len(capitals) - 1)  # This gets a list from within the whole list
            country = capitals[get_country][1]  # This gets the country from the list
            capital = capitals[get_country][0]  # This gets the respective capital for the country in the line above
        else:
            print("Finished")
            # Displays statistics
            print("\nNumber of questions answered correctly: {}\n"
                  "Number of questions answered: {}\n"
                  "Percentage: {:.2f}% (2 d. p.)".format(correct, answered, correct / answered * 100))
            break
    elif question == "Q" or question == "q":
        if answered == 0:
            print("Finished")  # Message displayed when all of the questions have been answered
            break
        else:
            # Displays statistics
            print("\nNumber of questions answered correctly: {}\n"
                  "Number of questions answered: {}\n"
                  "Percentage: {:.2f}% (2 d. p.)".format(correct, answered, correct / answered * 100))
            break
    else:
        answered += 1
        print("Incorrect\n"
              "The correct answer was {}\n".format(capital))  # Message displayed when the answer is wrong
        if len(capitals) > 0:
            capitals.pop(get_country)
        if len(capitals) > 0:
            get_country = random.randint(0, len(capitals) - 1)  # This gets a list from within the whole list
            country = capitals[get_country][1]  # This gets the country from the list
            capital = capitals[get_country][0]  # This gets the respective capital for the country in the line above
        elif len(capitals) == 0:
            print("Finished")  # Message displayed when all of the questions have been answered
            break
