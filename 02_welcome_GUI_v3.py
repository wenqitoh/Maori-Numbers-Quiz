"""Component 2 - Welcome GUI v3
create a 'CHECK' button to enable/disable 'NEXT' button.
add in C1 int_checker to combine with 'CHECK' button
Wen-Qi Toh
23/5/22"""

from tkinter import *
from functools import partial   # to prevent unwanted windows


class Welcome:
    def __init__(self):
        global num_of_questions, bg_colour

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
                                           bg=bg_colour, padx=10, pady=10,
                                           justify=CENTER)
        self.welcome_heading_label.grid(row=0, columnspan=4)

        # Welcome information (row 1)
        self.welcome_info_label = Label(self.welcome_frame, text="TO BEGIN THE QUIZ:\n"
                                        "Please enter a number (below or equal "
                                        "to 10) into the box\nbelow of how "
                                        "many questions you would like to "
                                        "answer.\nIf you don't know how to "
                                        "play, click 'HELP' button on the\n"
                                        "main quiz screen after pressing 'NEXT'.",
                                        font="Arial 12", bg=bg_colour,
                                        justify=CENTER, padx=10, pady=10)
        self.welcome_info_label.grid(row=1, columnspan=4)

        # num of question indication label (row 2)
        self.question_num_lbl = Label(self.welcome_frame,
                                      font="Arial 10 italic",
                                      text="Enter your number of questions "
                                      "below...", bg=bg_colour, justify=CENTER)
        self.question_num_lbl.grid(row=2, columnspan=4)
        # User num of questions entry box (row 3)
        self.question_num_entry = Entry(self.welcome_frame,
                                        font="Arial 12", width=5, justify=CENTER)
        self.question_num_entry.grid(row=3, columnspan=4)

        # blank label for error messages
        self.error_msg_lbl = Label(self.welcome_frame, font="Arial 12 bold",
                                   bg=bg_colour, pady=10, padx=10)
        self.error_msg_lbl.grid(row=4, columnspan=4)

        # 'check' button (row 5, column 1) to check that num of questions is within boundary
        self.check_button = Button(self.welcome_frame, text="CHECK",
                                   font="arial 14", padx=10, pady=10,
                                   command=self.int_check)
        self.check_button.grid(row=5, sticky=E, columnspan=3)

        # 'next' button (row 5, column 2)
        self.next_button = Button(self.welcome_frame, text="NEXT",
                                  font="arial 14", padx=10, pady=10,
                                  command=self.quiz)
        self.next_button.grid(row=5, sticky=E, columnspan=4)
        self.next_button.config(state="disabled")

    def int_check(self):
        global num_of_questions
        # turn question entry into a variable
        error_msg = "Error! Number must be between 1-10!"
        error_fg = "#D04747"
        num_of_questions = int(self.question_num_entry.get())

        # check that user entered number is between boundary values
        if 1 <= num_of_questions <= 10:
            self.error_msg_lbl.configure(fg=bg_colour)
            self.next_button.config(state="normal")
            return num_of_questions
        else:
            self.error_msg_lbl.configure(text=error_msg, fg=error_fg)

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
