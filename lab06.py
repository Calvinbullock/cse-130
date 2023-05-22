#  1. Name:
#      Calvin Bullock
# 2. Assignment Name:
#      Lab 06: Advanced Search
# 3. Assignment Description:
#      This program searches a list for the content that the user inputs.
# 4. Algorithmic Efficiency
#      -Identify the algorithmic efficiency and tell why it is as you say it is-
#
# 5. What was the hardest part? Be as specific as possible.
#      -a paragraph or two about how the assignment went for you-
#
# 6. How long did it take for you to complete the assignment?
#      -total time in hours including reading the assignment and submitting the program-


import json
import itertools


def main():
    # file_name = input("PLease enter file name: ")
    file_name = "languages.json"  # TODO quick tesing use

def open_file(file_name):
    # Opens the file Lab02,json
    try:
        file = open(file_name)
        data = file.read()
        dict = json.loads(data)

        # Closes file.
        file.close()

    except:
        print("Could not find the file, please check file and try again ")

    return dict["array"]

def search(array, target_word):
    """ """
    # Declare for scope
    list_start = 0
    list_end = len(array)
    mid_word = "null"

    # Loops until word matches mid_word or until end is grater then start
    while (mid_word != target_word) and (list_end > list_start):

        # Calc mid_index
        mid_index = round((list_end + list_start) / 2)

        #  Calc list_length, mid_index, mid_word
        mid_word = array[mid_index - 1]

        # Check if mid_word is more then target
        if mid_word < target_word:
            list_start = mid_index + 1

        # Check if mid_word is less then target
        elif mid_word > target_word:
            list_end = mid_index - 1

    print(f"target word {target_word}, found index {mid_word}")

main()