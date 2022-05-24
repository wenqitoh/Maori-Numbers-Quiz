"""Component 3 - quiz questions v1
come up with 10 quiz questions in a list
make function to .pop quiz questions in random order
Wen-Qi Toh
16/5/22"""

import random


def pop_out(num):
    for x in range(num):
        ans_list.pop(random.randint(0, int(num)-1))
        print(ans_list)


ans_list = [[1, "Tahi"], [2, "Rua"], [3, "Toru"], [4, "Wha"], [5, "Rima"],
            [6, "Onu"], [7, "Whitu"], [8, "Waru"], [9, "Iwa"], [10, "Tekau"]]

num_of_questions = 7
pop_out(num_of_questions)



