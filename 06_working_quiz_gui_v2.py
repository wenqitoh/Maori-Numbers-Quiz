"""Component 6 - working quiz GUI v2
adding C3 quiz questions to C5 quiz GUI, to form a working quiz, with 'next'
and 'check' buttons
Make 'next' & 'check' functions to apply to the respective buttons, allowing
user to run the quiz.
Wen-Qi Toh
29/5/22"""

import random
from tkinter import *


class Quiz:
    def __init__(self):
        global background
        background = "#D7BDE2"  # lilac

        # set up main Quiz GUI frame
        self.quiz_frame = Frame(width=300, bg=background)
        self.quiz_frame.grid()

        # set up quiz heading(row 0)
        self.quiz_heading = Label(self.quiz_frame, text="Maori Numbers Quiz",
                                  font="arial 16 bold", bg=background,
                                  justify=CENTER, pady=10, padx=10)
        self.quiz_heading.grid(row=0, columnspan=4)

        # box for questions to be displayed (label, row 1)
        self.quiz_questions = Label(self.quiz_frame, text="Enter 'Z' to begin",
                                    justify=CENTER, width=20, bg="white",
                                    pady=10, padx=10)
        self.quiz_questions.grid(row=1)

        # quiz text (label, row 2)
        self.quiz_text = Label(self.quiz_frame, text="Type your answer below,"
                                                     "click 'CHECK', then click"
                                                     " 'NEXT' to continue.",
                               justify=CENTER, font="arial 10 italic", padx=10,
                               pady=10, width=40, bg=background, wrap=250)
        self.quiz_text.grid(row=2)

        # user answer entry (entry, row 3)
        self.user_ans_entry = Entry(self.quiz_frame, font="Arial 14",
                                    width=20, justify=CENTER)
        self.user_ans_entry.grid(row=3, columnspan=4, pady=10, padx=10)

        # incorrect/correct quiz label (label, row 4)
        self.quiz_label = Label(self.quiz_frame, font="Arial 12 bold",
                                text="Quiz label here",
                                bg=background, pady=5, padx=5, justify=CENTER)
        self.quiz_label.grid(row=4, columnspan=3)

        # frame to hold 'next' & 'check' buttons (row 5)
        self.check_nxt_frame = Frame(self.quiz_frame, bg=background)
        self.check_nxt_frame.grid(row=5, pady=10)
        # 'Check' button (row 0, column 0)
        self.check_button = Button(self.check_nxt_frame, text="CHECK",
                                   font="arial 12 bold", bg="#FF5733",    # orange/red
                                   width=11, padx=5, pady=7, justify=CENTER,
                                   command=self.check_fn)
        self.check_button.grid(row=0, column=0, pady=10)

        # 'Next' button (row 0, column 1)
        self.next_button = Button(self.check_nxt_frame, text="NEXT",
                                  font="arial 12 bold", bg="#FFC300",   # yellow
                                  width=11, padx=5, pady=7, justify=CENTER,
                                  command=self.next_fn)
        self.next_button.grid(row=0, column=1, pady=10, padx=5)
        self.next_button.config(state="disabled")

        # frame to hold other buttons (row 6)
        self.buttons_frame = Frame(self.quiz_frame, bg=background)
        self.buttons_frame.grid(row=6, pady=10)
        # 'Results' button (row 0, column 0)
        self.results_button = Button(self.buttons_frame, text="Results",
                                     font="arial 11 bold",
                                     padx=7, pady=7, width=8)
        self.results_button.grid(row=0, column=0)

        # 'Help' button (row 0, column 1)
        self.help_button = Button(self.buttons_frame, text="Help",
                                  font="arial 11 bold",
                                  padx=7, pady=7, width=8)
        self.help_button.grid(row=0, column=1)

        # Quit button (row 0, column 2)
        self.quit_button = Button(self.buttons_frame, text="Quit",
                                  font="arial 11 bold", bg="#B1C6EC",    # blue
                                  padx=7, pady=7, width=8,
                                  command=self.quit)

        self.quit_button.grid(row=0, column=2)

    # 'Check' function
    def check_fn(self):
        # error colours & message
        error_msg = "Error! Answer must be a word, using letters!"
        error_fg = "#D04747"
        # turn question entry into a variable
        user_ans = self.user_ans_entry.get().capitalize()


        if user_ans == "Z":  # to start the quiz
            print("Let's get started!")
            self.quiz_label.config(fg="green", text="click 'Next' to begin")
            self.next_button.config(state="normal")
        elif user_ans.isalpha():
            print("answer is a word")
            self.quiz_label.config(fg="green", text="click 'Next' to continue")
            self.next_button.config(state="normal")
        else:
            print(error_msg)
            self.quiz_label.configure(text=error_msg, fg=error_fg)
            self.user_ans_entry.delete(0, END)

        if user_ans == number[1]:
            print("correct!")
            self.quiz_label.config(fg="green", text="Correct!")
            user_ans_list.append(user_ans)
        else:
            print("wrong answer")
            self.quiz_label.config(fg="red", text="Incorrect :(")
            user_ans_list.append(user_ans)

        ans_list.remove(number)
        print("removed", number)
        print(ans_list)
        print("Number of questions =", num_of_questions)

    # 'Next' function
    def next_fn(self):
        global number
        self.quiz_label.config(fg=background)   # makes quiz_label blank again
        number = random.choice(ans_list)
        self.quiz_questions.config(text=number[0])  # displays number in the quiz question box, for user to answer
        self.user_ans_entry.delete(0, END)  # clears the user answer entry box
        self.next_button.config(state="disabled")

    # function to quit Quiz GUI
    def quit(self):
        self.quiz_frame.destroy()


ans_list = [[1, "Tahi"], [2, "Rua"], [3, "Toru"], [4, "Wha"], [5, "Rima"],
            [6, "Onu"], [7, "Whitu"], [8, "Waru"], [9, "Iwa"], [10, "Tekau"]]
user_ans_list = []
num_of_questions = 7


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Maori Numbers Quiz")
    something = Quiz()
    root.mainloop()
