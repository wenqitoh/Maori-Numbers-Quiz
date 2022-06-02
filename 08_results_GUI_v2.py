"""Component 9 - Results GUI v2
make a function to apply to a 'see results' button, that will output all the
users answers on the GUI.
includes lists from C6 working quiz GUI - user_ans_list, right, wrong,
variable - num_of_questions
This version doesn't really work properly! v3 works
Wen-Qi Toh
1/6/22"""

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
                                       f"\nScore: {right}/{num_of_questions}",
                                       width=40, bg=background, wrap=250,
                                       font="Arial 12 italic")
        self.results_text.grid(row=1)

        # user question & answers (label, row 2)
        self.user_q_a = Label(self.results_frame, justify=CENTER, text="",
                              bg=background, font="Arial 12")
        self.user_q_a.grid(row=2)
        # dismiss button (row 3)
        self.dismiss_btn = Button(self.results_frame, text="Dismiss", width=10,
                                  bg="#CC5E25", font="arial 10 bold",   # rust bg
                                  command=partial(self.close_results, partner))
        self.dismiss_btn.grid(row=3, pady=10)

    def close_results(self, partner):
        # put results button back to normal...
        partner.results_button.config(state=NORMAL)
        self.results_box.destroy()

    def output_q_a(self):
        for x in user_ans_list:
            self.user_q_a.config(text=f"{x[0]} in Maori is {x[1]}")


# fixed ans list for now
user_ans_list = [[1, "Tahi"], [2, "Rua"], [3, "Toru"], [4, "Wha"], [5, "Rima"],
            [6, "Onu"], [7, "Whitu"], [8, "Waru"], [9, "Iwa"], [10, "Tekau"]]
right = []
wrong = []
num_of_questions = 7
output = Results.output_q_a
# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Maori Numbers Quiz")
    something = Quiz()
    root.mainloop()
