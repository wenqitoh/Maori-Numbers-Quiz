"""Component 11 - assembled outcome v5
making my own minor adjustments (aesthetics)
improving program after receiving user feedback
Edit code to fit PEP8 standards
Wen-Qi Toh
4/6/22"""

import random
from tkinter import *
from functools import partial   # to prevent unwanted windows
import re   # for file export


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
        num_of_questions = self.question_num_entry.get()

        try:
            num_of_questions = int(num_of_questions)
            # check that user entered number is between boundary values
            if 1 <= num_of_questions <= 10:
                self.error_msg_lbl.configure(fg=bg_colour)
                self.next_button.config(state="normal")
                self.check_button.config(state="disabled")
                self.error_msg_lbl.config(text="number is valid. Click 'NEXT'"
                                               " to continue.", fg="green")
            else:
                self.error_msg_lbl.configure(text=error_msg, fg="red")
                self.next_button.config(state="disabled")
                self.question_num_entry.delete(0, END)  # clears user entry box

        except ValueError:
            self.error_msg_lbl.configure(text=error_msg, fg="red")
            self.next_button.config(state="disabled")
            self.question_num_entry.delete(0, END)  # clears user entry box

    def quiz(self):
        Quiz()
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
                                    bg=background, pady=10, padx=10)
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
                                    width=20, justify=CENTER, bg="white")
        self.user_ans_entry.grid(row=3, columnspan=4, pady=10, padx=10)

        # incorrect/correct quiz label (label, row 4)
        self.quiz_label = Label(self.quiz_frame, font="Arial 12 bold",
                                text="Click 'Check' then 'Next' to begin.",
                                wrap=250, bg=background, pady=5, padx=5,
                                justify=CENTER)
        self.quiz_label.grid(row=4, columnspan=3)

        # frame to hold 'next' & 'check' buttons (row 5)
        self.check_nxt_frame = Frame(self.quiz_frame, bg=background)
        self.check_nxt_frame.grid(row=5, pady=10)
        # 'Check' button (row 0, column 0)
        self.check_button = Button(self.check_nxt_frame, text="CHECK",
                                   width=11, bg="#FF5733",  # orange
                                   font="arial 12 bold", padx=5, pady=7,
                                   justify=CENTER, command=self.check_fn)
        self.check_button.grid(row=0, column=0, pady=10)

        # 'Next' button (row 0, column 1)
        self.next_button = Button(self.check_nxt_frame, text="NEXT",
                                  font="arial 12 bold", bg="#FFC300",  # yellow
                                  width=11, padx=5, pady=7, justify=CENTER,
                                  command=self.next_fn)
        self.next_button.grid(row=0, column=1, pady=10, padx=5)
        self.next_button.config(state="disabled")

        # frame to hold other buttons (row 6)
        self.buttons_frame = Frame(self.quiz_frame, bg=background)
        self.buttons_frame.grid(row=6, pady=10)
        # 'Results' button (row 0, column 0)
        self.results_button = Button(self.buttons_frame, text="Results",
                                     font="arial 11 bold", padx=7,
                                     pady=7, state="disabled", command=lambda:
                                     self.results(user_ans_list), width=8,
                                     bg="#EF92EF")  # pink
        self.results_button.grid(row=0, column=0)

        # 'Help' button (row 0, column 1)
        self.help_button = Button(self.buttons_frame, text="Help",
                                  font="arial 11 bold", bg="#B292EF",  # purple
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
                    self.quiz_label.config(fg="green", text="click 'Next' to "
                                                            "continue")
                    self.check_button.config(state="disabled")
                    self.next_button.config(state="normal")
                    if user_ans == number[1]:
                        self.quiz_label.config(fg="green", text="Correct!")
                        user_ans_list.append(f"{number[0]} in Maori is "
                                             f"{user_ans} (correct)")
                        right.append(user_ans)
                    else:   # user entered a word but incorrect answer
                        self.quiz_label.config(fg="red",
                                               text=f"Incorrect. Correct "
                                                    f"answer is {number[1]}.")
                        user_ans_list.append(f"{number[0]} in Maori is "
                                             f"{user_ans} (incorrect)")
                        wrong.append(user_ans)
                else:   # user didn't enter answer using letters
                    self.quiz_label.configure(text=error_msg, fg=error_fg)
                    self.user_ans_entry.delete(0, END)

                ans_list.remove(number)
                # stop quiz if number of answered = number of questions
                if len(right) + len(wrong) == num_of_questions:
                    self.check_button.config(state="disabled")
                    self.next_button.config(state="disabled")
                    # allows user to see their quiz stats
                    self.results_button.config(state="normal")
                    self.quiz_label.config(text="End of Quiz! Click on "
                                                "'Results' button\nto see how"
                                                " well you did.", fg="blue")
            except ValueError:
                self.quiz_label.config(text=error_msg, fg=error_fg)
                self.user_ans_entry.delete(0, END)
        else:
            self.next_button.config(state="normal")

    # 'Next' function
    def next_fn(self):
        global number, pie
        pie = True
        # configuring all the labels and buttons
        number = random.choice(ans_list)    # random num from list to display
        self.quiz_questions.config(bg="white")
        self.quiz_label.config(fg=background)   # makes quiz_label blank again
        self.quiz_questions.config(text=number[0])
        self.quiz_text.config(fg="black")
        self.user_ans_entry.delete(0, END)  # clears the user answer entry box
        self.check_button.config(state="normal")
        self.next_button.config(state="disabled")

    # function to quit Quiz GUI
    def quit(self):
        self.quiz_frame.destroy()

    def help(self):
        get_help = Help(self)
        get_help.help_text.configure(text="Enter the Maori word for the "
                                          "number\nshown on the screen. Once "
                                          "you have\ntyped in your answer, "
                                          "click 'CHECK'\nthen 'NEXT' to "
                                          "continue on to the\nnext question."
                                          "\nClick onto 'Results' to see \n"
                                          "your quiz statistics at the end.")

    def results(self, data):
        Results(self, data)


class Help:
    def __init__(self, partner):
        bg_2 = "#AED49F"  # light green

        # disable help button
        partner.help_button.config(state=DISABLED)

        # set up child window (ie help box)
        self.help_box = Toplevel()

        self.help_box.protocol("WM_DELETE_WINDOW", partial(self.close_help,
                                                           partner))
        # set up GUI frame
        self.help_frame = Frame(self.help_box, width=300, bg=bg_2)
        self.help_frame.grid()

        # set up help heading(row 0)
        self.help_heading = Label(self.help_frame, text="Help/Instructions",
                                  font="arial 14 bold", bg=bg_2)
        self.help_heading.grid(row=0, pady=10, padx=10)

        # help text (label, row 1)
        self.help_text = Label(self.help_frame, text="", justify=LEFT,
                               font="Arial 12", width=40, bg=bg_2)
        self.help_text.grid(row=1, pady=10, padx=10)

        # dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss", width=10,
                                  bg="#CC5E25", font="arial 10 bold",  # rust
                                  command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        # put help button back to normal...
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


class Results:
    def __init__(self, partner, data):

        bg_3 = "#E5DF52"  # mustardy yellow

        # disable results button
        partner.results_button.config(state=DISABLED)

        # set up child window (ie results box)
        self.results_box = Toplevel()

        self.results_box.protocol("WM_DELETE_WINDOW",
                                  partial(self.close_results, partner))
        # set up GUI frame
        self.results_frame = Frame(self.results_box, width=300, bg=bg_3)
        self.results_frame.grid()

        # set up results heading(row 0)
        self.results_heading = Label(self.results_frame, text="Results",
                                     font="arial 16 bold", bg=bg_3,
                                     pady=10, padx=10)
        self.results_heading.grid(row=0)

        # results text (label, row 1)
        self.results_text = Label(self.results_frame, justify=LEFT,
                                  text=f"Number of Questions: "
                                       f"{num_of_questions}\nScore: "
                                       f"{len(right)}/{num_of_questions}",
                                       width=40, bg=bg_3, wrap=250,
                                       font="Arial 12 italic")
        self.results_text.grid(row=1)

        # user question & answers (label, row 2)
        self.user_q_a = Label(self.results_frame, justify=LEFT, text="",
                              bg=bg_3, font="Arial 12")
        self.user_q_a.grid(row=2)

        # frame for the buttons (row 3)
        self.result_btns_frame = Frame(self.results_frame, bg=bg_3)
        self.result_btns_frame.grid(row=3, pady=10)

        # export button (for later) (row 0, column 0)
        self.export_button = Button(self.result_btns_frame, text="Export",
                                    width=10, font="arial 10 bold",
                                    pady=5, padx=5, bg="#ECB1D4",
                                    command=lambda: self.export(data))   # pink
        self.export_button.grid(row=0, column=0)

        # results button for user to see their answers (row 0, column 1)
        self.see_ans_btn = Button(self.result_btns_frame, text="See Answers",
                                  width=10, font="arial 10 bold", pady=5,
                                  padx=5, command=self.output_q_a,
                                  bg="#7C59B0")  # dark purple
        self.see_ans_btn.grid(row=0, column=1)
        # dismiss button (row 0, column 2)
        self.dismiss_btn = Button(self.result_btns_frame, text="Dismiss",
                                  bg="#CC5E25", font="arial 10 bold",   # rust
                                  width=10, pady=5, padx=5,
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

    def export(self, data):
        Export(self, data)


class Export:
    def __init__(self, partner, data):
        bg_4 = "#E58C52"  # orange

        # disable export button
        partner.export_button.config(state=DISABLED)

        # set up child window (ie export box)
        self.export_box = Toplevel()

        # if users press 'X' at top, closes export and 'releases' export button
        self.export_box.protocol("WM_DELETE_WINDOW", partial(self.close_export,
                                                             partner))
        # set up GUI frame
        self.export_frame = Frame(self.export_box, width=300, bg=bg_4)
        self.export_frame.grid()

        # set up export heading(row 0)
        self.how_heading = Label(self.export_frame, text="Export Instructions",
                                 font="arial 19 bold", bg=bg_4)
        self.how_heading.grid(row=0)

        # export text (label, row 1)
        self.export_text = Label(self.export_frame,
                                 text="Enter a file name in the box below and"
                                      " press the Save button to save your "
                                      "quiz results to a text file.",
                                 justify=LEFT, width=40, bg=bg_4,
                                 font="arial 10", wrap=250)
        self.export_text.grid(row=1)

        # warning text (label, row 2)
        self.export_text = Label(self.export_frame,
                                 text="If the filename you entered below "
                                      "already exists, its contents will be "
                                      "replaced with your quiz results.",
                                 justify=LEFT, width=40, font="arial 10",
                                 bg="#52A8E5", wrap=250)   # bg colour blue

        self.export_text.grid(row=2)

        # filename entry box (row 3)
        self.filename_entry = Entry(self.export_frame, width=20,
                                    font="Arial 12 bold", justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

        # error message labels (row 4)
        self.save_error_label = Label(self.export_frame, text="", fg="black",
                                      bg=bg_4, font="arial 12")
        self.save_error_label.grid(row=4)

        # Save/Cancel Frame (row 5)
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=5, pady=10)

        # Save & Cancel buttons (row 0 of save_cancel_frame)
        self.save_button = Button(self.save_cancel_frame, text="Save",
                                  command=partial(lambda: self.save_results(
                                      partner, data)))
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel",
                                    command=partial(self.close_export, partner))
        self.cancel_button.grid(row=0, column=1)

    def save_results(self, partner, data):
        # regular expression to check file name. Can be upper or lower case
        valid_char = "[A-Za-z0-9_]"     # letters, numbers or underscores
        has_error = "no"
        filename = self.filename_entry.get()

        for letter in filename:
            # if the letter is valid, goes back and checks the next...
            if re.match(valid_char, letter):    # ...otherwise find problem
                continue
            elif letter == " ":
                problem = "(no spaces allowed)"
            else:
                problem = ("(no {}'s allowed)".format(letter))
            has_error = "yes"
            break

        if filename == "":
            problem = "can't be blank"
            has_error = "yes"

        if has_error == "yes":  # describe problem
            self.save_error_label.config(text="Invalid Filename! - {}"
                                         .format(problem))
            # change entry box bg to pink
            self.filename_entry.config(bg="#ffafaf")
        else:
            # if there are no errors, generate text file and then close
            # dialogue. Add .txt suffix
            filename = filename + ".txt"

            # create file to hold data
            f = open(filename, "w+")

            # add new line at end of each item
            for item in data:
                f.write(item + "\n")
            # close file
            f.close()

            # close dialogue
            self.close_export(partner)

    def close_export(self, partner):
        # put export button back to normal
        partner.export_button.config(state="normal")
        self.export_box.destroy()


# variables and lists
ans_list = [[1, "Tahi"], [2, "Rua"], [3, "Toru"], [4, "Wha"], [5, "Rima"],
            [6, "Onu"], [7, "Whitu"], [8, "Waru"], [9, "Iwa"], [10, "Tekau"]]
user_ans_list = []
right = []
wrong = []
pie = False   # pie is a random place holder var to use try/except in check_fn

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Maori Numbers Quiz")
    something = Welcome()
    root.mainloop()
