"""Program that creates a main window/frame for the Capitals Quiz.
This version adds a frame for the help section where extra information can be displayed and it has a cancel button to
'delete' the help frame. It also removes a redundant 'import random' piece of code.
Jung Woo Yi
Version 2 – 16/08/2021
"""

# Importing
from tkinter import *


class Quiz:
    def __init__(self):
        background_colour = "light blue"  # Setting the background colour

        # Setting the dimensions of the frame
        self.capital_quiz_frame = Frame(width=300, height=300, bg=background_colour, pady=10)
        self.capital_quiz_frame.grid()

        # Creating and formatting a label to display text
        self.capital_quiz_label = Label(self.capital_quiz_frame,
                                        text="Capitals Quiz",
                                        font=("Arial", "16", "bold"),
                                        bg=background_colour,
                                        padx=10, pady=10)
        self.capital_quiz_label.grid(row=0)

        # Creating and formatting a button that can be used to bring up the help frame
        self.help_button = Button(self.capital_quiz_frame,
                                  text="Help",
                                  font=("Arial", "14"),
                                  padx=10, pady=10,
                                  command=self.help)
        self.help_button.grid(row=1)

    def help(self):
        print("Help Section")  # This is to help check if the help button functions
        get_help = Help()
        get_help.help_text.configure(text="Text Here")


class Help:
    def __init__(self):
        background = "orange"  # Setting the background colour

        self.help_box = Toplevel()

        # Creating and formatting the help frame
        self.help_frame = Frame(self.help_box, width=300, bg=background)
        self.help_frame.grid()

        # Creating a label to put text in for the heading of the help frame
        self.help_heading = Label(self.help_frame, text="Help", font="Arial 14 bold", bg=background)
        self.help_heading.grid(row=0)

        self.help_text = Label(self.help_frame, text="", justify=LEFT, width=40, bg=background, wrap=250)
        self.help_text.grid(row=1)

        # Creating and formatting a button to exit out of the help window
        self.cancel_btn = Button(self.help_frame, text="Cancel", width=10, bg=background, font="Arial 10 bold",
                                 command=self.close_help)
        self.cancel_btn.grid(row=2, pady=10)

    def close_help(self):
        self.help_box.destroy()


# Main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Capitals Quiz")
    something = Quiz()
    root.mainloop()
