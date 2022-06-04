"""Component 9 - Export GUI v1
based off 04_help_GUI_v5 - repurposing code
Wen-Qi Toh
2/06/22"""

from tkinter import *
from functools import partial   # to prevent unwanted windows


class Results:
    def __init__(self):

        # formatting variable...
        bg_colour = "light blue"

        # results main screen GUI
        self.results_frame = Frame(width=300, height=300, bg=bg_colour,
                                     padx=10, pady=10)
        self.results_frame.grid()

        # Quiz Results Heading (row 0)
        self.results_label = Label(self.results_frame,
                                        text="Quiz results",
                                        font=("Arial", 16, "bold"),
                                        bg=bg_colour, padx=10, pady=10)
        self.results_label.grid(row=0)

        # export button (row 1)
        self.export_button = Button(self.results_frame, text="Export",
                                    font=("Arial", 14), padx=10, pady=10,
                                    command=self.export)
        self.export_button.grid(row=1)

    def export(self):
        get_export = Export(self)


class Export:
    def __init__(self, partner):
        background = "#a93f99"  # pale green

        # disable export button
        partner.export_button.config(state=DISABLED)

        # set up child window (ie export box)
        self.export_box = Toplevel()

        # if users press cross at top, closes export and 'releases' export button
        self.export_box.protocol("WM_DELETE_WINDOW", partial(self.close_export,
                                                           partner))
        # set up GUI frame
        self.export_frame = Frame(self.export_box, width=300, bg=background)
        self.export_frame.grid()

        # set up export heading(row 0)
        self.how_heading = Label(self.export_frame, text="Export Instructions",
                                 font="arial 19 bold", bg=background)
        self.how_heading.grid(row=0)

        # export text (label, row 1)
        self.export_text = Label(self.export_frame,
                                 text="Enter a file name in the box below and"
                                      " press the Save button to save your "
                                      "quiz results to a text file.",
                                 justify=LEFT, width=40, bg=background,
                                 wrap=250)
        self.export_text.grid(row=1)

        # warning text (label, row 2)
        self.export_text = Label(self.export_frame,
                                 text="If the filename you entered below "
                                      "already exists, its contents will be "
                                      "replaced with your quiz results",
                                      justify=LEFT, width=40,
                                 bg="#ffafaf", fg="maroon", wrap=250)   # bg colour pink

        self.export_text.grid(row=1)

        # filename entry box (row 3)
        self.filename_entry = Entry(self.export_frame, width=20,
                                    font="Arial 12 bold", justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

        # Save/Cancel Frame (row 4)
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=4, pady=10)

        # Save & Cancel buttons (row 0 of save_cancel_frame)
        self.save_button = Button(self.save_cancel_frame, text="Save")
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel",
                                    command=partial(self.close_export, partner))
        self.cancel_button.grid(row=0, column=1)

    def close_export(self, partner):
        # put export button back to normal...
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Quiz results")
    something = Results()
    root.mainloop()
