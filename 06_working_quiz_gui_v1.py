"""Component 6 - working quiz gui v1
adding C3 quiz questions to C5 quiz GUI, to form a working quiz, with 'next'
and 'check' buttons
add C1 int checker to 'Check' button
Wen-Qi Toh
26/5/22"""

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
        self.quiz_questions = Label(self.quiz_frame, text="Question goes here",
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
                                   command=self.int_check)
        self.check_button.grid(row=0, column=0, pady=10)

        # 'Next' button (row 0, column 1)
        self.next_button = Button(self.check_nxt_frame, text="NEXT",
                                  font="arial 12 bold", bg="#FFC300",   # yellow
                                  width=11, padx=5, pady=7, justify=CENTER)
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
                                  padx=7, pady=7, width=8)

        self.quit_button.grid(row=0, column=2)

    def int_check(self):
        # error colours & message
        error_msg = "Error! Answer must be a word, using letters!"
        error_fg = "#D04747"
        num_of_questions = 7    # set number for now, will change when combined with Welcome GUI
        try:
            # turn question entry into a variable
            user_ans = self.user_ans_entry.get()
            # check that user entered number is between boundary values
            if user_ans.isalpha():
                print("correct!")
                self.quiz_label.configure(fg=background)
                self.next_button.config(state="normal")
                user_ans_list.append(user_ans)
                return user_ans

            else:
                print("incorrect :(")
                self.quiz_label.configure(text=error_msg, fg=error_fg)
                self.next_button.config(state="disabled")

        except ValueError:
            print("incorrect :(")
            self.quiz_label.configure(text=error_msg, fg=error_fg)
            self.next_button.config(state="disabled")

        #
        # self.pop_out(num_of_questions, ans_list)

    def pop_out(self, num, list):
        print("Number of questions =", num)
        for x in range(num):
            print("x =", x)
            number = random.choice(list)
            user_entered = self.user_ans_entry
            self.quiz_questions.config(text=number[0])

            if user_entered == number[1]:
                print("correct!")
                self.quiz_label.config(fg="green", text="Correct!")
            else:
                print("incorrect :(")
                self.quiz_label.config(fg="red", text="Incorrect :(")
            print("removed", number)
            list.remove(number)
            print(list)


ans_list = [[1, "Tahi"], [2, "Rua"], [3, "Toru"], [4, "Wha"], [5, "Rima"],
            [6, "Onu"], [7, "Whitu"], [8, "Waru"], [9, "Iwa"], [10, "Tekau"]]
user_ans_list = []



# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Maori Numbers Quiz")
    something = Quiz()
    root.mainloop()
