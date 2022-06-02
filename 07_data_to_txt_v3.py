"""Component 7 - Output Results to Text File v3
Incorporates REGEX to check filename is valid (A-Z a-z 0-9 and underscores)
Source: https://www.quru99.com/reading-and-writing-files-in-python.html
Wen-Qi Toh
1/6/22"""

# data to be outputted
import re

# using regex - check if file name is valid
has_error = "yes"
while has_error == "yes":
    print()
    filename = input("Enter a filename: ")
    has_error = "no"

    valid_char = "[A-Za-z0-9_]"
    for letter in filename:
        if re.match(valid_char, letter):
            continue

        elif letter == " ":
            problem = "(no spaces allowed)"
        else:
            problem = ("(no {}'s allowed)".format(letter))
        has_error = "yes"

    if filename == "":
        problem = "can't be blank"
        has_error = "yes"

    if has_error == "yes":
        print("Invalid filename - {}".format(problem))
    # valid
    else:
        print("You entered a valid filename")
