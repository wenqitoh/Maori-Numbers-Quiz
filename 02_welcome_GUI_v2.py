"""Component 2 - Welcome GUI v2
create user entry box
make it a global var for future use
add in welcome text
Wen-Qi Toh
16/5/22"""

from tkinter import *
from functools import partial   # to prevent unwanted windows


class Welcome:
    def __init__(self):
        global num_of_questions

        # formatting variable...
        bg_colour = "#FDBCBC"   # light pink/red

        # Welcome GUI
        self.welcome_frame = Frame(width=300, height=300, bg=bg_colour,
                                   padx=10, pady=10)
        self.welcome_frame.grid()

        # Welcome GUI Heading (row 0)
        self.welcome_heading_label = Label(self.welcome_frame,
                                           text="Welcome to the Maori Numbers Quiz!",
                                           font=("arial", "16", "bold"),
                                           bg=bg_colour, padx=10, pady=10)
        self.welcome_heading_label.grid(row=0)

        # Welcome information (row 1)
        self.welcome_info_label = Label(self.welcome_frame, text="TO BEGIN THE QUIZ:\n"
                                        "Please enter a number (below or equal "
                                        "to 10) into the box\nbelow of how "
                                        "many questions you would like to "
                                        "answer.\nIf you don't know how to "
                                        "play, click 'HELP' button on the\n"
                                        "main quiz screen after pressing 'NEXT'.",
                                        font="Arial 12", bg=bg_colour,
                                        justify=LEFT, padx=10, pady=10)
        self.welcome_info_label.grid(row=1)

        # num of question indication label (row 2)
        self.question_num_lbl = Label(self.welcome_frame,
                                      font="Arial 10 italic",
                                      text="Enter your number of questions "
                                           "below...", bg=bg_colour)
        self.question_num_lbl.grid(row=2)
        # User num of questions entry box (row 3)
        self.question_num_entry = Entry(self.welcome_frame,
                                        font="Arial 12", width=5)
        self.question_num_entry.grid(row=3, pady=10)

        # Welcome button - 'next' button (row 4)
        self.welcome_button = Button(self.welcome_frame, text="NEXT",
                                     font="arial 14", padx=10, pady=10,
                                     command=self.quiz)
        self.welcome_button.grid(row=4)

    def quiz(self):
        print("You clicked 'next' for the quiz GUI")
        get_quiz = Quiz()
        get_quiz.quiz_text.configure(text="this is the main quiz frame to be"
                                          " developed later")
        # print(num_of_questions)
        self.welcome_frame.destroy()


# quiz GUI will be developed later in the project
class Quiz:
    def __init__(self):
        background = "#D7BDE2"  # lilac

        # set up main Quiz GUI frame
        self.quiz_frame = Frame(width=300, bg=background)
        self.quiz_frame.grid()

        # set up quiz heading(row 0)
        self.quiz_heading = Label(self.quiz_frame, text="Maori Numbers Quiz",
                                  font="arial 12 bold", bg=background)
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


