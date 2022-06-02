"""Component 6 - working quiz GUI v5
updated this to change the lists & code a bit, for use in 09_results_GUI_v3
Wen-Qi Toh
2/6/22"""

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
        self.quiz_questions = Label(self.quiz_frame, font="arial 16 bold",
                                    text="", justify=CENTER, width=3,
                                    bg="white", pady=10, padx=10)
        self.quiz_questions.grid(row=1, columnspan=4)

        # quiz text (label, row 2)
        self.quiz_text = Label(self.quiz_frame, text="Type your answer below,"
                                                     "click 'CHECK', then click"
                                                     " 'NEXT' to continue.",
                               justify=CENTER, font="arial 10 italic", padx=10,
                               pady=10, width=40, fg=background,
                               bg=background, wrap=250)
        self.quiz_text.grid(row=2)

        # user answer entry (entry, row 3)
        self.user_ans_entry = Entry(self.quiz_frame, font="Arial 14",
                                    width=20, justify=CENTER)
        self.user_ans_entry.grid(row=3, columnspan=4, pady=10, padx=10)

        # incorrect/correct quiz label (label, row 4)
        self.quiz_label = Label(self.quiz_frame, font="Arial 12 bold",
                                text="Enter any letter then click 'Next' "
                                     "to begin.",
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
        global count
        # error colours & message
        error_msg = "Error! Answer must be a word, using letters!"
        error_fg = "#D04747"
        count = 0
        # turn question entry into a variable
        user_ans = self.user_ans_entry.get().capitalize()

        if pie:
            try:    # to stop PyCharm error msg from appearing - ValueError
                if user_ans.isalpha():  # only allows word/letter answers
                    print("answer is a word")
                    self.quiz_label.config(fg="green", text="click 'Next' to continue")
                    self.check_button.config(state="disabled")
                    self.next_button.config(state="normal")
                    if user_ans == number[1]:
                        print("correct!")
                        self.quiz_label.config(fg="green", text="Correct!")
                        user_ans_list.append(f"{number[0]} in Maori is {user_ans}")     # for outputting later in Results GUI
                        right.append(user_ans)
                    else:   # user entered a word but incorrect answer
                        print("wrong answer")
                        self.quiz_label.config(fg="red", text="Incorrect :(")
                        user_ans_list.append(f"{number[0]} in Maori is {user_ans}")     # for outputting later in Results GUI
                        wrong.append(user_ans)
                else:   # user didn't enter answer using letters
                    print(error_msg)
                    self.quiz_label.configure(text=error_msg, fg=error_fg)
                    self.user_ans_entry.delete(0, END)

                ans_list.remove(number)
                print("removed", number)
                print(ans_list)
                print("Number of questions =", num_of_questions)
                print("right = ", len(right))
                print("wrong = ", len(wrong))
                print("user ans list: ", user_ans_list)

                if len(right) + len(wrong) == num_of_questions:   # stop quiz if number of answered = number of
                    self.check_button.config(state="disabled")    # questions specified
                    self.next_button.config(state="disabled")
                    self.quiz_label.config(text="End of Quiz! Click on 'Results' button"
                                                " \nto see how well you did.")
            except ValueError:
                print(error_msg)
        else:
            self.next_button.config(state="normal")
            print("let's get started!")

    # 'Next' function
    def next_fn(self):
        global number, pie
        pie = True
        self.quiz_label.config(fg=background)   # makes quiz_label blank again
        number = random.choice(ans_list)
        self.quiz_questions.config(text=number[0])  # displays number in the quiz question box, for user to answer
        self.quiz_text.config(fg="black")
        self.user_ans_entry.delete(0, END)  # clears the user answer entry box
        self.check_button.config(state="normal")
        self.next_button.config(state="disabled")

    # function to quit Quiz GUI
    def quit(self):
        self.quiz_frame.destroy()

# variables and lists
ans_list = [[1, "Tahi"], [2, "Rua"], [3, "Toru"], [4, "Wha"], [5, "Rima"],
            [6, "Onu"], [7, "Whitu"], [8, "Waru"], [9, "Iwa"], [10, "Tekau"]]
user_ans_list = []
right = []
wrong = []
pie = False
num_of_questions = 4

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Maori Numbers Quiz")
    something = Quiz()
    root.mainloop()
