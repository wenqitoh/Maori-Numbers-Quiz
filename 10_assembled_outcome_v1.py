"""Component 11 - assembled outcome v1
using C6 working_quiz_gui_v5, adding 04 help_GUI_v5, for help button
add help text/instructions
Wen-Qi Toh
1/6/22"""

import random
from tkinter import *
from functools import partial   # to prevent unwanted windows


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
                                text="Enter any letter then click 'Check', "
                                     " then 'Next' to begin.", wrap=250,
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
                                  padx=7, pady=7, width=8, command=self.help)
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
                        user_ans_list.append(user_ans)
                        right.append(user_ans)
                    else:   # user entered a word but incorrect answer
                        print("wrong answer")
                        self.quiz_label.config(fg="red", text="Incorrect :(")
                        user_ans_list.append(user_ans)
                        wrong.append(user_ans)
                else:   # user didn't enter answer using letters
                    print(error_msg)
                    self.quiz_label.configure(text=error_msg, fg=error_fg)
                    self.user_ans_entry.delete(0, END)

                ans_list.remove(number)
                print("removed", number)
                print(ans_list)
                print("Number of questions =", num_of_questions)
                count += 1
                print("count = ", count)
                print("right = ", len(right))
                print("wrong = ", len(wrong))

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

    def help(self):
        print("You asked for help")
        get_help = Help(self)
        get_help.help_text.configure(text="Enter the Maori word for the number\n"
                                          "shown on the screen. Once you have\n"
                                          "typed in your answer, click 'CHECK'\n"
                                          "then 'NEXT' to continue on to the\n"
                                          "next question.\n"
                                          "Click onto 'QUIZ HISTORY' to see \n"
                                          "your quiz statistics.")


class Help:
    def __init__(self, partner):
        background = "#AED49F"  # light green

        # disable help button
        partner.help_button.config(state=DISABLED)

        # set up child window (ie help box)
        self.help_box = Toplevel()

        self.help_box.protocol("WM_DELETE_WINDOW", partial(self.close_help,
                                                           partner))
        # set up GUI frame
        self.help_frame = Frame(self.help_box, width=300, bg=background)
        self.help_frame.grid()

        # set up help heading(row 0)
        self.help_heading = Label(self.help_frame, text="Help/Instructions",
                                  font="arial 14 bold", bg=background)
        self.help_heading.grid(row=0, pady=10, padx=10)

        # help text (label, row 1)
        self.help_text = Label(self.help_frame, text="", justify=LEFT,
                               font="Arial 12", width=40, bg=background)
        self.help_text.grid(row=1, pady=10, padx=10)

        # dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss", width=10,
                                  bg="#CC5E25", font="arial 10 bold",   # rust bg
                                  command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        # put help button back to normal...
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


# variables and lists
ans_list = [[1, "Tahi"], [2, "Rua"], [3, "Toru"], [4, "Wha"], [5, "Rima"],
            [6, "Onu"], [7, "Whitu"], [8, "Waru"], [9, "Iwa"], [10, "Tekau"]]
user_ans_list = []
right = []
wrong = []
pie = False
num_of_questions = 7

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Maori Numbers Quiz")
    something = Quiz()
    root.mainloop()
