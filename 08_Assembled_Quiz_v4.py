"""This program/'component' is the assembled quiz.
This version disables the submit button until the next button is pressed. This version also displays information for
users in the help frame.
Version 4 – 08/09/2021
"""

# Importing
from tkinter import *
from functools import partial
import random
from Capitals_List_v2 import capitals


class Quiz:
    def __init__(self):
        self.quiz_results = []
        background_colour = "light blue"  # Colour formatting

        # Creating and formatting the 'main' frame of the quiz game
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

        # Entry box formatting for the user's input
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

        # Button that is used to mark the user's input
        self.submit_button = Button(self.capital_quiz_frame,
                                    text="Submit",
                                    font=("Arial", "14"),
                                    command=self.mark_answer)
        self.submit_button.grid(row=5)

        # Button that brings up the 'history' window
        self.history_button = Button(self.capital_quiz_frame,
                                     text="History",
                                     font=("Arial", "14"),
                                     padx=10, pady=10,
                                     command=lambda: self.history(self.quiz_results))
        self.history_button.grid(row=6, pady=20)

        # Button that brings up the 'Help' window
        self.help_button = Button(self.capital_quiz_frame,
                                  text="Help",
                                  font=("Arial", "14"),
                                  padx=10, pady=10,
                                  command=self.help)
        self.help_button.grid(row=7)

    def history(self, quiz_history):
        History(self, quiz_history)

    def help(self):
        get_help = Help(self)
        # Displaying text to help users understand the help section
        get_help.help_text.configure(text="To start the quiz, press the next button. After you answer a question, "
                                          "press the submit button. After you see your result, you can move onto the "
                                          "next question by pressing the next button. If you want to see your "
                                          "statistics, press the history button. Thank you for playing Capitals Quiz!")

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

        # Disabling the next button until the submit button is pressed (it is reactivated in the mark_answer function)
        self.next_button.config(state=DISABLED)

        # Reactivating the submit button
        self.submit_button.config(state=NORMAL)

    # Function that checks whether the answer is correct or not
    def mark_answer(self):
        global get_country, country, capital
        inputted_capital = self.entry_box.get()
        if capital == inputted_capital:
            self.result_label.configure(text="Correct", fg="black")
            self.quiz_results.append("Country: {}, Capital: {}, Your Answer: {}, Result: Correct"
                                     .format(country, capital, inputted_capital))
            self.next_button.config(state=NORMAL)  # Reactivating the next button
            self.submit_button.config(state=DISABLED)  # Disabling the submit button
            if len(capitals) > 0:
                capitals.pop(get_country)
            if len(capitals) > 0:
                get_country = random.randint(0, len(capitals) - 1)  # This gets a list from within the whole list
                country = capitals[get_country][1]  # This gets the country from the list
                capital = capitals[get_country][0]  # This gets the respective capital for the country in the line above
        else:
            self.result_label.configure(text="Incorrect. The correct answer was {}".format(capital), fg="black")
            self.quiz_results.append("Country: {}, Capital: {}, Your Answer: {}, Result: Incorrect"
                                     .format(country, capital, inputted_capital))
            self.next_button.config(state=NORMAL)  # Reactivating the next button
            self.submit_button.config(state=DISABLED)  # Disabling the submit button
            if len(capitals) > 0:
                capitals.pop(get_country)
            if len(capitals) > 0:
                get_country = random.randint(0, len(capitals) - 1)  # This gets a list from within the whole list
                country = capitals[get_country][1]  # This gets the country from the list
                capital = capitals[get_country][0]  # This gets the respective capital for the country in the line above
            elif len(capitals) == 0:
                self.result_label.configure(text="Finished", fg="black")


# Formatting the 'history' window
class History:
    def __init__(self, partner, quiz_history):
        background = "light green"  # Background colour
        partner.history_button.config(state=DISABLED)  # Disabling the "history" button

        self.history_box = Toplevel()
        self.history_box.protocol('WM_DELETE_WINDOW', partial(self.close_history, partner))

        # Setting up the history frame
        self.history_frame = Frame(self.history_box, width=300, bg=background)
        self.history_frame.grid()

        # Creating a label that identifies the frame as a history frame
        self.history_heading = Label(self.history_frame, text="History", font="Arial 14 bold", bg=background)
        self.history_heading.grid(row=0)

        self.history_text = Label(self.history_frame, text="", justify=LEFT, width=40, bg=background, wrap=250,
                                  padx=10, pady=10)
        self.history_text.grid(row=1)

        history_string = ""
        if len(quiz_history) >= 7:
            for i in range(0, 7):
                history_string += quiz_history[len(quiz_history) - i - 1] + "\n"
        else:
            for i in quiz_history:
                history_string += quiz_history[len(quiz_history) - quiz_history.index(i) - 1] + "\n"
                self.history_text.config(text="The quiz results appear here. If you would like to save your results, "
                                              "click the export button and follow the instruction(s).")

        self.calculation_label = Label(self.history_frame, text=history_string, bg=background, font="Arial 12",
                                       justify=LEFT)
        self.calculation_label.grid(row=2)

        # Setting up the frame that will hold the dismiss and export buttons
        self.dismiss_export_frame = Frame(self.history_frame)
        self.dismiss_export_frame.grid(row=3, pady=10)

        # Formatting the export button
        self.export_button = Button(self.dismiss_export_frame, text="Export", width=10, font="Arial 12 bold",
                                    command=lambda: self.export(quiz_history))
        self.export_button.grid(row=0, column=0)

        # Formatting the dismiss button which can be used to 'delete' the frame
        self.dismiss_button = Button(self.dismiss_export_frame, text="Dismiss", width=10, bg=background,
                                     font="Arial 12 bold", command=partial(self.close_history, partner))
        self.dismiss_button.grid(row=0, column=1)

    # Exiting out of the 'history' window
    def close_history(self, partner):
        partner.history_button.config(state=NORMAL)  # The button is reactivated
        self.history_box.destroy()

    def export(self, quiz_history):
        Export(self, quiz_history)


# Formatting the 'export' window
class Export:
    def __init__(self, partner, quiz_history):
        background = "light blue"
        partner.export_button.config(state=DISABLED)  # Disabling the "export" button

        self.export_box = Toplevel()
        self.export_box.protocol('WM_DELETE_WINDOW', partial(self.close_export, partner))

        # Creating a frame for the export section of the quiz
        self.export_frame = Frame(self.export_box, width=300, bg=background)
        self.export_frame.grid()

        # Creating and formatting a heading for the export frame
        self.export_heading = Label(self.export_frame, text="Export", font="Arial 14 bold", bg=background)
        self.export_heading.grid(row=0)

        # Instructing the user to input a filename
        self.export_text = Label(self.export_frame, text="Please enter a filename:", justify=LEFT, width=40,
                                 bg=background, wrap=250)
        self.export_text.grid(row=2, pady=10)

        # This is the entry box for entering the filename
        self.filename_entry = Entry(self.export_frame, font="Arial 14 bold", justify=CENTER, width=20)
        self.filename_entry.grid(row=3, pady=10)

        # Label to display any error messages
        self.error_label = Label(self.export_frame, text="", bg=background, fg="maroon")
        self.error_label.grid(row=4)

        # Creating/Positioning a frame for 'cancel' and 'save' buttons
        self.cancel_save_frame = Frame(self.export_frame)
        self.cancel_save_frame.grid(row=5, pady=10)

        # Button that can be used to save the results
        self.save_button = Button(self.cancel_save_frame, text="Save", font="Arial 10 bold", width=10,
                                  command=partial(lambda: self.save_history(partner, quiz_history)))
        self.save_button.grid(row=0, column=0)

        # Button that 'deletes' the frame
        self.cancel_btn = Button(self.cancel_save_frame, text="Dismiss", font="Arial 10 bold", bg=background, width=10,
                                 command=partial(self.close_export, partner))
        self.cancel_btn.grid(row=0, column=1)

    def save_history(self, partner, quiz_history):
        error = "no"
        valid = "[A-Za-z0-9_]"
        filename = self.filename_entry.get()
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
            self.error_label.config(text="Invalid Filename – {}\n".format(error_message))  # Displaying an error message
        else:
            filename = filename + ".txt"  # Adds an extension ('.txt')
            file = open(filename, "w+")

            for i in quiz_history:
                file.write(i + "\n")  # Each piece of information is on a different line
            file.close()
            self.close_export(partner)

    # Exiting out of the 'export' window
    def close_export(self, partner):
        partner.export_button.config(state=NORMAL)  # The button can be pressed again
        self.export_box.destroy()


# Formatting the 'Help' window
class Help:
    def __init__(self, partner):
        background = "light green"  # Colour formatting
        partner.help_button.config(state=DISABLED)  # Disabling the "Help" button

        self.help_box = Toplevel()
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # Setting up the frame for the help section
        self.help_frame = Frame(self.help_box, width=300, bg=background)
        self.help_frame.grid()

        # Creating a heading for the help frame
        self.help_heading = Label(self.help_frame, text="Help", font="Arial 14 bold", bg=background)
        self.help_heading.grid(row=0)

        self.help_text = Label(self.help_frame, text="", justify=LEFT, width=40, bg=background, wrap=250)
        self.help_text.grid(row=1)

        # Button that ca be used to 'delete' the frame
        self.cancel_btn = Button(self.help_frame, text="Dismiss", width=10, bg=background, font="Arial 10 bold",
                                 command=partial(self.close_help, partner))
        self.cancel_btn.grid(row=2, pady=10)

    # Exiting out of the 'Help' window
    def close_help(self, partner):
        partner.help_button.config(state=NORMAL)  # The user can press the button again
        self.help_box.destroy()


# Main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Capitals Quiz")
    something = Quiz()
    root.mainloop()
