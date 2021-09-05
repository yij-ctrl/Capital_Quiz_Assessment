"""Program that creates a main window/frame for the Capitals Quiz and a help frame that can provide instructions to
users.
This version has a functioning 'cancel' button that allows the user to 'delete' the help frame. This version also
stops users from creating multiple help windows.
Jung Woo Yi
Version 3 – 16/08/2021
"""

# Importing
from tkinter import *
from functools import partial


class Quiz:
    def __init__(self):
        background_colour = "light blue"  # Setting the background colour

        # Creating and formatting the 'main' frame of the Capital Quiz
        self.capital_quiz_frame = Frame(width=300, height=300, bg=background_colour, pady=10)
        self.capital_quiz_frame.grid()

        # Creating and formatting a label where text can go for the Capital Quiz 'main' frame
        self.capital_quiz_label = Label(self.capital_quiz_frame,
                                        text="Capitals Quiz",
                                        font=("Arial", "16", "bold"),  # Font formatting
                                        bg=background_colour,
                                        padx=10, pady=10)
        self.capital_quiz_label.grid(row=0)

        # Button that brings up the 'Help' window
        self.help_button = Button(self.capital_quiz_frame,
                                  text="Help",
                                  font=("Arial", "14"),  # FOnt formatting
                                  padx=10, pady=10,
                                  command=self.help)
        self.help_button.grid(row=1)

    def help(self):
        print("Help Section")
        get_help = Help(self)
        get_help.help_text.configure(text="Text Here")


# Formatting the 'Help' window
class Help:
    def __init__(self, partner):
        background = "orange"  # Setting the background colour

        partner.help_button.config(state=DISABLED)  # Disabling the "Help" button

        self.help_box = Toplevel()
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # Creating and formatting the help frame
        self.help_frame = Frame(self.help_box, width=300, bg=background)
        self.help_frame.grid()

        # Creating and formatting a label where the heading for the help frame can go
        self.help_heading = Label(self.help_frame, text="Help", font="Arial 14 bold", bg=background)
        self.help_heading.grid(row=0)

        self.help_text = Label(self.help_frame, text="", justify=LEFT, width=40, bg=background, wrap=250)
        self.help_text.grid(row=1)

        # Creating and formatting a button that allows the users to 'delete' the help frame
        self.cancel_btn = Button(self.help_frame, text="Cancel", width=10, bg=background, font="Arial 10 bold",
                                 command=partial(self.close_help, partner))
        self.cancel_btn.grid(row=2, pady=10)

    # Exiting out of the 'Help' window
    def close_help(self, partner):
        partner.help_button.config(state=NORMAL)  # Allowing the button to be pressed again
        self.help_box.destroy()


# Main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Capitals Quiz")
    something = Quiz()
    root.mainloop()
