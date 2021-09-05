"""Program that creates a main window/frame for the Capitals Quiz
Jung Woo Yi
Version 1 – 16/08/2021
"""

# Importing
from tkinter import *
import random


class Quiz:
    def __init__(self):
        print("Hey")
        background_colour = "green"  # Setting the background colour

        # Creating a frame
        self.capital_quiz_frame = Frame(width=300, height=300, bg=background_colour)
        self.capital_quiz_frame.grid()

        # Creating a label to display text and formatting it
        self.capital_quiz_label = Label(text="Capitals Quiz",
                                        font=("Arial", "16", "bold"),
                                        bg=background_colour,
                                        padx=10, pady=10)
        self.capital_quiz_label.grid(row=0)


# Main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Capitals Quiz")
    something = Quiz()
    root.mainloop()
