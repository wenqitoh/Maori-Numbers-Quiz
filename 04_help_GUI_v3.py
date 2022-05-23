"""Component 1 - Help GUI v3
creating Help class, setting up Help frame
Wen-Qi Toh
9/5/22"""

from tkinter import *


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

        # help button (row 1)
        self.help_button = Button(self.quiz_frame, text="HELP",
                                  font="arial 14", padx=10, pady=10,
                                  command=self.help)
        self.help_button.grid(row=1)

    def help(self):
        print("You asked for help")
        get_help = Help()
        get_help.help_text.configure(text="Help text goes here")


class Help:
    def __init__(self):
        background = "#AED49F"  # light green

        # set up child window (ie help box)
        self.help_box = Toplevel()

        # set up GUI frame
        self.help_frame = Frame(self.help_box, width=300, bg=background)
        self.help_frame.grid()

        # set up help heading(row 0)
        self.help_heading = Label(self.help_frame, text="Help/Instructions",
                                  font="arial 10 bold", bg=background)
        self.help_heading.grid(row=0)

        # help text (label, row 1)
        self.help_text = Label(self.help_frame, text="", justify=LEFT,
                               width=40, bg=background, wrap=250)
        self.help_text.grid(row=1)

        # dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss", width=10,
                                  bg="#CC5E25", font="arial 10 bold",   # rust bg
                                  command=self.close_help)
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self):
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Maori Numbers Quiz")
    something = Quiz()
    root.mainloop()
