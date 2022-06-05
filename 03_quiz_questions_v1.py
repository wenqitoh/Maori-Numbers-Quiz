""" Component 3 - Quiz Questions v1, USED FOR TRIALLING!!
using regex code to check that answer is correct
Wen-Qi Toh
16/5/22"""

import re

ans_list = [[1, "Tahi"], [2, "Rua"], [3, "Toru"], [4, "Wha"], [5, "Rima"],
            [6, "Onu"], [7, "Whitu"], [8, "Waru"], [9, "Iwa"], [10, "Tekau"]]

error_msg = "Error!"
has_error = "yes"

while has_error == "yes":
    has_error = "no"
    answer = str(input("enter an answer: ")).capitalize()

    valid_char = "[A-Za-z]"     # only letters allowed
    for letter in answer:   # checking that answer is made up of letters, valid
        if re.match(valid_char, letter):
            has_error = "no"

        else:
            print(error_msg)
            has_error = "yes"
            break

    if has_error == "no":   # checking that valid answer is on ans_list
        for x in ans_list:
            if answer == x[1]:
                print(f"{answer} is in answer list")
                break

    if has_error == "yes":  # describe problem
        print("Invalid answer. Answer can only have letters of the alphabet.")
        print()




