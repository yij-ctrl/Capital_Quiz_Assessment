"""Program that creates a frame for the history section using a button that the user can press.
This is the second version of an alternate version of 06_History_GUI_v1. This version has the export and dismiss
buttons' font size as the same size and the width of the buttons are equal.
Jung Woo Yi
Version 2 – 31/08/2021
"""

# Importing
from tkinter import *
from functools import partial


class Quiz:
    def __init__(self):
        background_colour = "light green"  # Colour formatting
        self.quiz_frame = Frame(width=300, height=300, bg=background_colour, pady=10)  # Window size
        self.quiz_frame.grid()

        # Formatting for the 'Capitals Quiz' label
        self.capital_quiz_label = Label(self.quiz_frame,
                                        text="Capitals Quiz",
                                        font=("Arial", "16", "bold"),  # Font formatting
                                        bg=background_colour,
                                        padx=10, pady=10)
        self.capital_quiz_label.grid(row=0)

        # Button that brings up the 'history' window
        self.history_button = Button(self.quiz_frame,
                                     text="History",
                                     font=("Arial", "14"),
                                     padx=10, pady=10,
                                     command=self.history)
        self.history_button.grid(row=1)

    def history(self):
        get_history = History(self)
        # Displaying text to help users understand the history section
        get_history.history_text.configure(text="This section displays your history for the quiz. If you would like to "
                                                "save your results, please export the history by clicking the export "
                                                "button")


# Formatting the 'history' window
class History:
    def __init__(self, partner):
        background = "light blue"  # Background colour
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

        # Setting up the frame that will hold the dismiss and export buttons
        self.dismiss_export_frame = Frame(self.history_frame)
        self.dismiss_export_frame.grid(row=3, pady=10)

        # Formatting the export button (it does not currently function)
        self.export_button = Button(self.dismiss_export_frame, text="Export", width=10, font="Arial 12 bold")
        self.export_button.grid(row=0, column=0)

        # Formatting the dismiss button
        self.dismiss_button = Button(self.dismiss_export_frame, text="Dismiss", width=10, bg=background,
                                     font="Arial 12 bold", command=partial(self.close_history, partner))
        self.dismiss_button.grid(row=0, column=1)

    # Exiting out of the 'history' window
    def close_history(self, partner):
        partner.history_button.config(state=NORMAL)  # The button is reactivated
        self.history_box.destroy()


# Main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Capitals Quiz")
    something = Quiz()
    root.mainloop()
