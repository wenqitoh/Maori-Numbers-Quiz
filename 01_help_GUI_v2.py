"""Component 1 - Help GUI v2
Adding in Help frame and button
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
                                        font=("Abadi", "16", "bold"),
                                        bg=bg_colour, padx=10, pady=10)
        self.quiz_heading_label.grid(row=0)

        # help button (row 1)
        self.help_button = Button(self.quiz_frame, text="HELP",
                                  font="Abadi 14", padx=10, pady=10)
        self.help_button.grid(row=1)

    def help(self):
        print("You asked for help")
        get_help = Help()
        get_help.help_text.configure(text="Help text goes here")


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Maori Numbers Quiz")
    something = Quiz()
    root.mainloop()
