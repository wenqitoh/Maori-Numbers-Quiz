"""Component 1 - Help GUI v1
Create main quiz frame for 'help' frame to go into
Wen-Qi Toh
9/5/22"""

from tkinter import *


class Quiz:
    def __init__(self):
        print("Hello world")

        # formatting variable...
        bg_colour = "#D7BDE2"   # lilac

        # Quiz main screen GUI
        self.quiz_frame = Frame(width=300, height=300, bg=bg_colour)
        self.quiz_frame.grid()

        # Maori Numbers Quiz Heading (row 0)
        self.quiz_heading_label = Label(text="Maori Numbers Quiz",
                                   font=("Abadi", "16", "bold"),
                                   bg=bg_colour, padx=10, pady=10)
        self.quiz_heading_label.grid(row=0)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Maori Numbers Quiz")
    something = Quiz()
    root.mainloop()
