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

    # Opens the file Lab02,json and converts it to python dictinary.
    try:
        # Opens the file Lab02,json and converts it to python dictinary.
        file = open(file_name)
    except:
        print("Could not find the file, please check file and try again ")

    data = file.read()
    dict = json.loads(data)
    file.close()  # TODO might close to soon

    # TODO uncoment for production
    # Gets user input then calls search function on it
    # target_word = input(f"Enter the langwage your looking for: ")
    # search(dict.array, target_word)

    # for testing
    search(dict["array"], "c#")


def search(array, target_word):
    """ """

    # Declare for scope
    list_start = 0
    list_end = len(array)
    found_target = ""

    # Loops until word matches target_word & end is grater then start
    while (found_target != target_word) and (list_end > list_start):
        # Reset sum, but keep it in scope
        sum = 0

        # Calc sum
        # Found this loop method here:
        # https://stackoverflow.com/questions/8671280/pythonic-way-to-iterate-over-part-of-a-list
        for line in itertools.islice(array, list_start, list_end):
            mid_index = round((list_end + list_end) / 2)

        #  Calc list_length, mid_index, mid_word
        print(f"L74- '{mid_index}', len- '{len(array)}'")
        mid_word = array[mid_index - 1]

        #
        if mid_word < target_word:
            print(f"79")
            list_start = mid_index + 1
            list_length = list_length - list_start

        elif mid_word > target_word:
            print(f"84")
            list_end = mid_index - 1
            list_length = list_length - list_end

    print(f"target word {target_word}, found index {mid_word}")


main()
