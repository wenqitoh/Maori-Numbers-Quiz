"""Component 3 - quiz questions v3
print questions followed by their answers in random order, only num_of_questions
number of questions.
Wen-Qi Toh
24/5/22"""

import random


# function to randomly remove values in a list, [num_of_questions] times
def pop_out(num):
    for x in range(num):
        print(num)
        print(x)
        ans_list.pop(random.randint(0, int(num)-1))
        # set(random.sample(range(len(ans_list)), num))
        print(ans_list)
        for i in ans_list:
            maori = str(input(f"What is {i[0]} in Maori?")).capitalize()
            if maori == i[1]:
                print("correct")


ans_list = [[1, "Tahi"], [2, "Rua"], [3, "Toru"], [4, "Wha"], [5, "Rima"],
            [6, "Onu"], [7, "Whitu"], [8, "Waru"], [9, "Iwa"], [10, "Tekau"]]

num_of_questions = 7
pop_out(num_of_questions)





