"""Program that gives extra information for the temperature capital_quiz.
Jung Woo Yi
Version 1 – 16/08/2021
"""

from tkinter import *
import random


class Quiz:
    def __init__(self):
        print("Hey")
        background_colour = "green"
        self.capital_quiz_frame = Frame(width=300, height=300, bg=background_colour)
        self.capital_quiz_frame.grid()
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
