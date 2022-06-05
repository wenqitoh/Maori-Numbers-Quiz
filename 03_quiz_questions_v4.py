"""Component 3 - quiz questions v4, USED FOR TRIALLING!!
ask user the question, get their input, say whether it's correct/incorrect.
only output as many questions as num_of_questions

Wen-Qi Toh
17/5/22"""

import random


def pop_out(num, list):
    print("Number of questions =", num)
    for x in range(num):
        print("x =", x)
        number = random.choice(list)
        user_entered = input(f"What is the Maori word for {number[0]}? ").capitalize()

        if user_entered == number[1]:
            print("correct!")
        else:
            print("incorrect :(")

        print("removed", number)
        list.remove(number)
        print(list)


ans_list = [[1, "Tahi"], [2, "Rua"], [3, "Toru"], [4, "Wha"], [5, "Rima"],
            [6, "Onu"], [7, "Whitu"], [8, "Waru"], [9, "Iwa"], [10, "Tekau"]]

num_of_questions = 7
pop_out(num_of_questions, ans_list)




