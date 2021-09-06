"""Program that integrates the first component into a GUI.
This version disables the next button until submit is pressed.
Jung Woo Yi
Version 3 – 01/09/2021
"""

# Importing
from tkinter import *
from functools import partial
import random
from Capitals_List_v2 import capitals


class Quiz:
    def __init__(self):
        background_colour = "light blue"  # Colour formatting

        # Creating the frame for the quiz game
        self.capital_quiz_frame = Frame(width=300, height=300, bg=background_colour, pady=10)  # Window size
        self.capital_quiz_frame.grid()

        # Label for the heading of the 'main' quiz frame
        self.capital_quiz_label = Label(self.capital_quiz_frame,
                                        text="Capitals Quiz",
                                        font=("Arial", "16", "bold"),  # Font formatting
                                        bg=background_colour,
                                        padx=10, pady=10)
        self.capital_quiz_label.grid(row=0)

        # Label where the question will be asked to the user
        self.question_label = Label(self.capital_quiz_frame,
                                    bg=background_colour,
                                    pady=10)
        self.question_label.grid(row=1)

        # Label that displays the result of the question
        self.result_label = Label(self.capital_quiz_frame,
                                  bg=background_colour,
                                  pady=10)
        self.result_label.grid(row=2)

        # Entry box formatting
        self.entry_box = Entry(self.capital_quiz_frame,
                               font="Arial 14 bold",
                               width=20)
        self.entry_box.grid(row=3)

        # Formatting the next button
        # When pressed, it should go through the run_quiz function
        self.next_button = Button(self.capital_quiz_frame,
                                  text="Next",
                                  font=("Arial", "14"),
                                  command=self.run_quiz)
        self.next_button.grid(row=4)

        # Button that 'marks' the answer
        self.submit_button = Button(self.capital_quiz_frame,
                                    text="Submit",
                                    font=("Arial", "14"),
                                    command=self.mark_answer)
        self.submit_button.grid(row=5)

        # Button that brings up the 'Help' window
        self.help_button = Button(self.capital_quiz_frame,
                                  text="Help",
                                  font=("Arial", "14"),
                                  padx=10, pady=10,
                                  command=self.help)
        self.help_button.grid(row=6, pady=10)  # 'pady=10' helps with spacing

    def help(self):
        get_help = Help(self)
        get_help.help_text.configure(text="Text Here")  # Help text is customisable

    get_country = random.randint(0, len(capitals) - 1)  # This gets a list from within the whole list
    country = capitals[get_country][1]  # This gets the country from the list
    capital = capitals[get_country][0]  # This gets the respective capital for the country in the line above

    # Function that generates the next question
    def run_quiz(self):
        global get_country, country, capital
        get_country = random.randint(0, len(capitals) - 1)  # This gets a list from within the whole list
        country = capitals[get_country][1]  # This gets the country from the list
        capital = capitals[get_country][0]  # This gets the respective capital for the country in the line above

        # This changes the result_label text to nothing which removes the correct or incorrect message when moving on
        self.result_label.configure(text="", fg="black")

        # Asks the user the capital of the country
        question = "What is the capital of {}?".format(country)
        self.question_label.configure(text=question, fg="black")  # Displaying the question in the GUI

        # Disabling the next button until the submit button is pressed (is it reactivated in the mark_answer function
        self.next_button.config(state=DISABLED)

    # Function that checks whether the answer is correct or not
    def mark_answer(self):
        global get_country, country, capital
        inputted_capital = self.entry_box.get()
        if capital == inputted_capital:
            self.result_label.configure(text="Correct", fg="black")
            self.next_button.config(state=NORMAL)  # Reactivating the next button
            if len(capitals) > 0:
                capitals.pop(get_country)
            if len(capitals) > 0:
                get_country = random.randint(0, len(capitals) - 1)  # This gets a list from within the whole list
                country = capitals[get_country][1]  # This gets the country from the list
                capital = capitals[get_country][0]  # This gets the respective capital for the country in the line above
        else:
            self.result_label.configure(text="Incorrect. The correct answer was {}".format(capital), fg="black")
            self.next_button.config(state=NORMAL)  # Reactivating the next button
            if len(capitals) > 0:
                capitals.pop(get_country)
            if len(capitals) > 0:
                get_country = random.randint(0, len(capitals) - 1)  # This gets a list from within the whole list
                country = capitals[get_country][1]  # This gets the country from the list
                capital = capitals[get_country][0]  # This gets the respective capital for the country in the line above
            elif len(capitals) == 0:
                self.result_label.configure(text="Finished", fg="black")


# Formatting the 'Help' window
class Help:
    def __init__(self, partner):
        background = "light green"
        partner.help_button.config(state=DISABLED)  # Disabling the "Help" button

        self.help_box = Toplevel()
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # Creating a frame for the help section
        self.help_frame = Frame(self.help_box, width=300, bg=background)
        self.help_frame.grid()

        # Creating and formatting a heading for the help frame
        self.help_heading = Label(self.help_frame, text="Help", font="Arial 14 bold", bg=background)
        self.help_heading.grid(row=0)

        self.help_text = Label(self.help_frame, text="", justify=LEFT, width=40, bg=background, wrap=250)
        self.help_text.grid(row=1)

        # Creating and formatting a button that can be used to 'delete' the help frame
        self.cancel_btn = Button(self.help_frame, text="Dismiss", width=10, bg=background, font="Arial 10 bold",
                                 command=partial(self.close_help, partner))
        self.cancel_btn.grid(row=2, pady=10)

    # Exiting out of the 'Help' window
    def close_help(self, partner):
        partner.help_button.config(state=NORMAL)  # The help button can be pressed again
        self.help_box.destroy()


# Main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Capitals Quiz")
    something = Quiz()
    root.mainloop()
