"""Program that has an improved main quiz window for the Capital Quiz game.
This program is an alternate program for 03_Main_Quiz_Window_v1. The difference is that this program has a space/gap
between the entry box and the help button.
Jung Woo Yi
Version 1 – 29/08/2021
"""

# Importing
from tkinter import *
from functools import partial


class Quiz:
    def __init__(self):
        background_colour = "light blue"  # Colour formatting

        # Creating and formatting a frame for the 'main' window of the Capital Quiz game
        self.capital_quiz_frame = Frame(width=300, height=300, bg=background_colour, pady=10)  # Window size
        self.capital_quiz_frame.grid()

        # Creating and formatting a label for the 'main' window
        self._capital_quiz_label = Label(self.capital_quiz_frame,
                                         text="Capitals Quiz",
                                         font=("Arial", "16", "bold"),  # Font formatting
                                         bg=background_colour,
                                         padx=10, pady=10)
        self._capital_quiz_label.grid(row=0)

        # Creating and formatting a label for instructions
        self.instructions_label = Label(self.capital_quiz_frame,
                                        text="Instructions Here",  # Instructions message can be changed
                                        bg=background_colour,
                                        font="Arial 10 italic",  # Font formatting
                                        wrap=250,
                                        justify=LEFT,
                                        padx=10,
                                        pady=10)
        self.instructions_label.grid(row=1)

        # Entry box formatting
        self.entry_box = Entry(self.capital_quiz_frame,
                               font="Arial 14 bold",
                               width=20)
        self.entry_box.grid(row=2)

        # Button that brings up the 'Help' window
        self.help_button = Button(self.capital_quiz_frame,
                                  text="Help",
                                  font=("Arial", "14"),
                                  padx=10, pady=10,
                                  command=self.help)
        self.help_button.grid(row=3, pady=10)  # 'pady=10' helps with spacing

    def help(self):
        get_help = Help(self)
        get_help.help_text.configure(text="Text Here")  # Instructions can be displayed


# Formatting the 'Help' window
class Help:
    def __init__(self, partner):
        background = "orange"  # Colour formatting
        partner.help_button.config(state=DISABLED)  # Disabling the "Help" button

        self.help_box = Toplevel()
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # Creating and formatting the help frame
        self.help_frame = Frame(self.help_box, width=300, bg=background)
        self.help_frame.grid()

        # Creating and formatting a heading for the help frame
        self.help_heading = Label(self.help_frame, text="Help", font="Arial 14 bold", bg=background)
        self.help_heading.grid(row=0)

        self.help_text = Label(self.help_frame, text="", justify=LEFT, width=40, bg=background, wrap=250)
        self.help_text.grid(row=1)

        # Creating and formatting a cancel button that 'deletes' the help frame
        self.cancel_btn = Button(self.help_frame, text="Cancel", width=10, bg=background, font="Arial 10 bold",
                                 command=partial(self.close_help, partner))
        self.cancel_btn.grid(row=2, pady=10)

    # Exiting out of the 'Help' window
    def close_help(self, partner):
        partner.help_button.config(state=NORMAL)  # Users are able to press the help button again
        self.help_box.destroy()


# Main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Capitals Quiz")
    something = Quiz()
    root.mainloop()
