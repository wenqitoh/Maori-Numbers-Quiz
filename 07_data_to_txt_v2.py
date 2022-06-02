"""Component 7 - Output Results to Text File v2
Incorporates REGEX to check filename is valid (A-Z a-z 0-9 and underscores)
Source: https://www.quru99.com/reading-and-writing-files-in-python.html
THIS CODE DOES NOT WORK!
Wen-Qi Toh
1/6/22"""

# data to be outputted
import re

data = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh"]

# get filename, can't be blank / invalid
# assume valid data for now
filename = input("Enter a Filename (leave off the extension): ")

valid_file = "[A-Zaz]"
if re.Match(valid_file, filename):
    # add .txt suffix!
    filename = filename + ".txt"
    # create file to hold data
    f = open(filename, "w+")

    # add new line at end of each item
    for item in data:
        f.write(item + "\n")

    # close file
    f.close()
else:
    print("oops!")

