#  1. Name:
#      Calvin Bullock
# 2. Assignment Name:
#      Lab 06: Advanced Search
# 3. Assignment Description:
#      This program searches a list for the content that the user inputs.
# 4. Algorithmic Efficiency
#      TODO whitch and why?
#      TODO whitch and why?


#      TODO whitch and why?
#      TODO whitch and why?
# 5. What was the hardest part? Be as specific as possible.
#      It wasn't to bad once I re-figured out the json file
#      Syntax and interactions.
# 6. How long did it take for you to complete the assignment?
#      2 hours


import json


def main():

    # # TODO uncoment for production
    # file_name = input("PLease enter file name: ")
    # # Gets user input then calls search function on it
    # target_word = input(f"Enter the langwage your looking for: ")
    # search(dict.array, target_word)

    # For testing
    word = search(open_file("Lab06.empty.json"), "'")
    print(word == "", "''")

    word = search(open_file("Lab06.trivial.json"), "'trivial'")
    print(word == "trivial", "'trivial'")

    word = search(open_file("Lab06.trivial.json"), "")
    print(word == "", "''")

    word = search(open_file("Lab06.languages.json"), "C++")
    print(word == "C++", "'C++'")

    word = search(open_file("Lab06.languages.json"), "Lisp")
    print(word == "Lisp", "'Lisp'")

    word = search(open_file("Lab06.countries.json"), "United States of America")
    print(word == "United States of America", "'United States of America'")

    word = search(open_file("Lab06.countries.json"), "United States")
    print(word == "United States", "'United States'")

    # # Test cases key
    # Empty list	        Lab06.empty.json	    Empty	                    No
    # Single item found	    Lab06.trivial.json	    trivial	                    Yes
    # Single item not found	Lab06.trivial.json	    missing	                    No
    # Small list found	    Lab06.languages.json	C++	                        Yes
    # Small list not found	Lab06.languages.json	Lisp	                    No
    # Big list found	    Lab06.countries.json	United States of America	Yes
    # Big list not found	Lab06.countries.json	United States	            No


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
        mid_word = array[mid_index]

        # Check if mid_word is more then target
        if mid_word < target_word:
            list_start = mid_index + 1

        # Check if mid_word is less then target
        elif mid_word > target_word:
            list_end = mid_index - 1

    return mid_word


main()