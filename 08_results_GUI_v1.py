"""Component 9 - Results GUI v1
creating the frame and set up for results GUI
copying C4 help GUI format
Wen-Qi Toh
31/5/22"""

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
        get_results.results_text.configure(text="results text goes here")


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
        self.results_heading = Label(self.results_frame, text="Results/Instructions",
                                  font="arial 10 bold", bg=background)
        self.results_heading.grid(row=0)

        # results text (label, row 1)
        self.results_text = Label(self.results_frame, text="", justify=LEFT,
                               width=40, bg=background, wrap=250)
        self.results_text.grid(row=1)

        # dismiss button (row 2)
        self.dismiss_btn = Button(self.results_frame, text="Dismiss", width=10,
                                  bg="#CC5E25", font="arial 10 bold",   # rust bg
                                  command=partial(self.close_results, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_results(self, partner):
        # put results button back to normal...
        partner.results_button.config(state=NORMAL)
        self.results_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Maori Numbers Quiz")
    something = Quiz()
    root.mainloop()
