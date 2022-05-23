"""Component 2 - Welcome GUI v1
create Welcome and Quiz frame, destroy Welcome frame and transition to Quiz
frame when 'NEXT' is pressed.
Quiz frame to be developed later in Quiz GUI component
Wen-Qi Toh
15/5/22"""

from tkinter import *
from functools import partial   # to prevent unwanted windows


class Welcome:
    def __init__(self):

        # formatting variable...
        bg_colour = "#D7BDE2"   # lilac

        # Welcome GUI
        self.welcome_frame = Frame(width=300, height=300, bg=bg_colour,
                                   padx=10, pady=10)
        self.welcome_frame.grid()

        # Welcome GUI Heading (row 0)
        self.welcome_heading_label = Label(self.welcome_frame,
                                           text="Welcome!",
                                           font=("arial", "16", "bold"),
                                           bg=bg_colour, padx=10, pady=10)
        self.welcome_heading_label.grid(row=0)

        # Welcome button - 'next' button (row 1)
        self.welcome_button = Button(self.welcome_frame, text="NEXT",
                                     font="arial 14", padx=10, pady=10,
                                     command=self.quiz)
        self.welcome_button.grid(row=1)

    def quiz(self):
        print("You clicked 'next' for the quiz GUI")
        get_quiz = Quiz()
        get_quiz.quiz_text.configure(text="this is the main quiz frame to be"
                                          " developed later")
        self.welcome_frame.destroy()


# quiz GUI will be developed later in the project
class Quiz:
    def __init__(self):
        background = "#AED49F"  # light green

        # set up main Quiz GUI frame
        self.quiz_frame = Frame(width=300, bg=background)
        self.quiz_frame.grid()

        # set up quiz heading(row 0)
        self.quiz_heading = Label(self.quiz_frame, text="Maori Numbers Quiz",
                                  font="arial 10 bold", bg=background)
        self.quiz_heading.grid(row=0)

        # quiz text (label, row 1)
        self.quiz_text = Label(self.quiz_frame, text="", justify=LEFT,
                               width=40, bg=background, wrap=250)
        self.quiz_text.grid(row=1)

        # Quit button (row 2)
        # Leave with no function, to be developed in later component/s
        self.quit_btn = Button(self.quiz_frame, text="QUIT", width=10,
                               bg="#CC5E25", font="arial 10 bold")   # rust bg

        self.quit_btn.grid(row=2, pady=10)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Maori Numbers Quiz")
    something = Welcome()
    root.mainloop()
