"""component 1 - number checking function
does not accept numbers below 1 and above 10
Wen-Qi Toh
16/5/22"""


# code to check that a number is valid
def int_check(question):
    valid = False
    error_msg = "Error! Number must be between 1-10!."
    while not valid:
        try:
            num = int(input(question))

            if 1 <= num <= 10:
                print("good job")
                return num

            else:
                print(error_msg)

        except ValueError:
            print(error_msg)


num_of_questions = int_check("Enter a num between 1-10: ")
# int_check(num_of_questions)
