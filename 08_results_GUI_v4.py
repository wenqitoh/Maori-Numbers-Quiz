"""Component 9 - Results GUI v4
Refining the code & making it look aesthetically pleasing
add an export button for Export GUI later
Wen-Qi Toh
2/6/22"""

from tkinter import *
from functools import partial   # to prevent unwanted windows


class Quiz:
    def __init__(self):

        # formatting variable...
        bg_colour = "#D7BDE2"   # lilac

        # Quiz main screen GUI
        self.quiz_frame = Frame(width=300, height=300, bg=bg_colour,
                                padx=10, pady=10)
        self.quiz_frame.grid()

        # Maori Numbers Quiz Heading (row 0)
        self.quiz_heading_label = Label(self.quiz_frame,
                                        text="Maori Numbers Quiz",
                                        font=("arial", "16", "bold"),
                                        bg=bg_colour, padx=10, pady=10)
        self.quiz_heading_label.grid(row=0)

        # results button (row 1)
        self.results_button = Button(self.quiz_frame, text="Results",
                                     font="arial 14", padx=10, pady=10,
                                     command=self.results)
        self.results_button.grid(row=1)

    # def results(self, calc_history):
    #     Results(self, calc_history)
    def results(self):
        print("You asked for results")
        get_results = Results(self)


class Results:
    def __init__(self, partner):

        background = "#AED49F"  # light green

        # disable results button
        partner.results_button.config(state=DISABLED)

        # set up child window (ie results box)
        self.results_box = Toplevel()

        self.results_box.protocol("WM_DELETE_WINDOW", partial(self.close_results,
                                                           partner))
        # set up GUI frame
        self.results_frame = Frame(self.results_box, width=300, bg=background)
        self.results_frame.grid()

        # set up results heading(row 0)
        self.results_heading = Label(self.results_frame, text="Results",
                                     font="arial 16 bold", bg=background,
                                     pady=10, padx=10)
        self.results_heading.grid(row=0)

        # results text (label, row 1)
        self.results_text = Label(self.results_frame, justify=LEFT,
                                  text=f"Number of Questions: {num_of_questions}"
                                       f"\nScore: {len(right)}/{num_of_questions}",
                                       width=40, bg=background, wrap=250,
                                       font="Arial 12 italic")
        self.results_text.grid(row=1)

        # user question & answers (label, row 2)
        self.user_q_a = Label(self.results_frame, justify=CENTER, text="",
                              bg=background, font="Arial 12", wrap=200)
        self.user_q_a.grid(row=2)

        # frame for the buttons (row 3)
        self.result_btns_frame = Frame(self.results_frame, bg=background)
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
        print(to_separate)


# fixed ans list for now
user_ans_list = ["1 in Maori is Tahi", "2 in Maori is Rua",
                 "3 in Maori is Toru", "4 in Maori is Wha",
                 "5 in Maori is Riiima", "6 in Maori is 00nu",
                 "7 in Maori is Whiu"]

right = ["1 in Maori is Tahi", "2 in Maori is Rua", "3 in Maori is Toru",
         "4 in Maori is Wha"]
wrong = ["5 in Maori is Riiima", "6 in Maori is 00nu", "7 in Maori is Whiu"]
num_of_questions = 7

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Maori Numbers Quiz")
    something = Quiz()
    root.mainloop()
