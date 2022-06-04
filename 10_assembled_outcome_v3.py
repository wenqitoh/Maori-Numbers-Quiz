"""Component 11 - assembled outcome v3
adding C8 Results GUI to assembled outcome v2
removing unnecessary code from testing eg. print statements
change bg colour of Results GUI
Wen-Qi Toh
2/6/22"""

import random
from tkinter import *
from functools import partial   # to prevent unwanted windows


class Welcome:
    def __init__(self):
        global bg_colour
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
                                        "answer, \nthen click 'CHECK'."
                                        " If you don't know how to "
                                        "play, click\n'HELP' button on the "
                                        "main quiz screen\nafter pressing 'NEXT'.",
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
        num_of_questions = self.question_num_entry.get()

        try:
            num_of_questions = int(num_of_questions)
            # check that user entered number is between boundary values
            if 1 <= num_of_questions <= 10:
                self.error_msg_lbl.configure(fg=bg_colour)
                self.next_button.config(state="normal")
            else:
                self.error_msg_lbl.configure(text=error_msg, fg=error_fg)
                self.next_button.config(state="disabled")

        except ValueError:
            self.error_msg_lbl.configure(text=error_msg, fg=error_fg)
            self.next_button.config(state="disabled")

    def quiz(self):
        get_quiz = Quiz()
        self.welcome_frame.destroy()


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
                                                     "click 'CHECK' then click"
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
                                text="Enter any letter then click 'Check'"
                                     " then 'Next' to begin.", wrap=250,
                                bg=background, pady=5, padx=5, justify=CENTER)
        self.quiz_label.grid(row=4, columnspan=3)

        # frame to hold 'next' & 'check' buttons (row 5)
        self.check_nxt_frame = Frame(self.quiz_frame, bg=background)
        self.check_nxt_frame.grid(row=5, pady=10)
        # 'Check' button (row 0, column 0)
        self.check_button = Button(self.check_nxt_frame, text="CHECK",
                                   font="arial 12 bold", bg="#FF5733",  # orange/red
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
                                     font="arial 11 bold", padx=7, pady=7,
                                     width=8, command=self.results)
        self.results_button.grid(row=0, column=0)

        # 'Help' button (row 0, column 1)
        self.help_button = Button(self.buttons_frame, text="Help",
                                  font="arial 11 bold",
                                  padx=7, pady=7, width=8, command=self.help)
        self.help_button.grid(row=0, column=1)

        # Quit button (row 0, column 2)
        self.quit_button = Button(self.buttons_frame, text="Quit",
                                  font="arial 11 bold", bg="#B1C6EC",   # blue
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

        if pie:
            try:    # to stop PyCharm error msg from appearing - ValueError
                if user_ans.isalpha():  # only allows word/letter answers
                    self.quiz_label.config(fg="green", text="click 'Next' to continue")
                    self.check_button.config(state="disabled")
                    self.next_button.config(state="normal")
                    if user_ans == number[1]:
                        self.quiz_label.config(fg="green", text="Correct!")
                        user_ans_list.append(f"{number[0]} in Maori is {user_ans}")
                        right.append(user_ans)
                    else:   # user entered a word but incorrect answer
                        self.quiz_label.config(fg="red", text="Incorrect :(")
                        user_ans_list.append(f"{number[0]} in Maori is {user_ans}")
                        wrong.append(user_ans)
                else:   # user didn't enter answer using letters
                    self.quiz_label.configure(text=error_msg, fg=error_fg)
                    self.user_ans_entry.delete(0, END)

                ans_list.remove(number)

                if len(right) + len(wrong) == num_of_questions:   # stop quiz if number of answered = number of
                    self.check_button.config(state="disabled")    # questions specified
                    self.next_button.config(state="disabled")
                    self.quiz_label.config(text="End of Quiz! Click on 'Results' button"
                                                " \nto see how well you did.")
            except ValueError:
                print(error_msg)
        else:
            self.next_button.config(state="normal")

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
        get_help = Help(self)
        get_help.help_text.configure(text="Enter the Maori word for the number\n"
                                          "shown on the screen. Once you have\n"
                                          "typed in your answer, click 'CHECK'\n"
                                          "then 'NEXT' to continue on to the\n"
                                          "next question.\n"
                                          "Click onto 'QUIZ HISTORY' to see \n"
                                          "your quiz statistics.")

    def results(self):
        get_results = Results(self)


class Help:
    def __init__(self, partner):
        background_2 = "#AED49F"  # light green

        # disable help button
        partner.help_button.config(state=DISABLED)

        # set up child window (ie help box)
        self.help_box = Toplevel()

        self.help_box.protocol("WM_DELETE_WINDOW", partial(self.close_help,
                                                           partner))
        # set up GUI frame
        self.help_frame = Frame(self.help_box, width=300, bg=background_2)
        self.help_frame.grid()

        # set up help heading(row 0)
        self.help_heading = Label(self.help_frame, text="Help/Instructions",
                                  font="arial 14 bold", bg=background_2)
        self.help_heading.grid(row=0, pady=10, padx=10)

        # help text (label, row 1)
        self.help_text = Label(self.help_frame, text="", justify=LEFT,
                               font="Arial 12", width=40, bg=background_2)
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


class Results:
    def __init__(self, partner):

        background_3 = "#E5DF52"  # mustardy yellow

        # disable results button
        partner.results_button.config(state=DISABLED)

        # set up child window (ie results box)
        self.results_box = Toplevel()

        self.results_box.protocol("WM_DELETE_WINDOW", partial(self.close_results,
                                                              partner))
        # set up GUI frame
        self.results_frame = Frame(self.results_box, width=300, bg=background_3)
        self.results_frame.grid()

        # set up results heading(row 0)
        self.results_heading = Label(self.results_frame, text="Results",
                                     font="arial 16 bold", bg=background_3,
                                     pady=10, padx=10)
        self.results_heading.grid(row=0)

        # results text (label, row 1)
        self.results_text = Label(self.results_frame, justify=LEFT,
                                  text=f"Number of Questions: {num_of_questions}"
                                       f"\nScore: {len(right)}/{num_of_questions}",
                                       width=40, bg=background_3, wrap=250,
                                       font="Arial 12 italic")
        self.results_text.grid(row=1)

        # user question & answers (label, row 2)
        self.user_q_a = Label(self.results_frame, justify=CENTER, text="",
                              bg=background_3, font="Arial 12", wrap=200)
        self.user_q_a.grid(row=2)

        # frame for the buttons (row 3)
        self.result_btns_frame = Frame(self.results_frame, bg=background_3)
        self.result_btns_frame.grid(row=3, pady=10)

        # export button (for later) (row 0, column 0)
        self.export_button = Button(self.result_btns_frame, text="Export",
                                    width=10, font="arial 10 bold",
                                    pady=5, padx=5, bg="#ECB1D4")   # pink
        self.export_button.grid(row=0, column=0)

        # results button for user to see their answers (row 0, column 1)
        self.results_button = Button(self.result_btns_frame, text="See Answers",
                                     width=10, font="arial 10 bold", pady=5,
                                     padx=5, command=self.output_q_a,
                                     bg="#7C59B0")  # dark purple
        self.results_button.grid(row=0, column=1)
        # dismiss button (row 0, column 2)
        self.dismiss_btn = Button(self.result_btns_frame, text="Dismiss", width=10,
                                  bg="#CC5E25", font="arial 10 bold",   # rust bg
                                  pady=5, padx=5,
                                  command=partial(self.close_results, partner))
        self.dismiss_btn.grid(row=0, column=2)

    def close_results(self, partner):
        # put results button back to normal...
        partner.results_button.config(state=NORMAL)
        self.results_box.destroy()

    def output_q_a(self):
        to_separate = ""
        for item in user_ans_list:
            to_separate += f"{item}\n"
        self.user_q_a.config(text=to_separate)


# variables and lists
ans_list = [[1, "Tahi"], [2, "Rua"], [3, "Toru"], [4, "Wha"], [5, "Rima"],
            [6, "Onu"], [7, "Whitu"], [8, "Waru"], [9, "Iwa"], [10, "Tekau"]]
user_ans_list = []
right = []
wrong = []
pie = False   # pie is a random place holder var to use try/except loop in check_fn

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Maori Numbers Quiz")
    something = Welcome()
    root.mainloop()
