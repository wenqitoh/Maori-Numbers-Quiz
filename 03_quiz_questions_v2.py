"""Component 6 - quiz questions v2
print questions followed by their answers in random order for num_of_questions
Wen-Qi Toh
17/5/22"""

import random


# function to randomly remove values in a list, [num_of_questions] times
def pop_out(num):
    for x in range(num):
        ans_list.pop(random.randint(0, int(num)-1))
        print(ans_list)
        for i in ans_list:
            print(f"What is {i[0]} in Maori?")
            print(f"It is {i[1]}")


ans_list = [[1, "Tahi"], [2, "Rua"], [3, "Toru"], [4, "Wha"], [5, "Rima"],
            [6, "Onu"], [7, "Whitu"], [8, "Waru"], [9, "Iwa"], [10, "Tekau"]]

num_of_questions = 7
pop_out(num_of_questions)



