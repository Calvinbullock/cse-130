# 1. Name:
#      Calvin Bullock
# 2. Assignment Name:
#      Lab 08: Sort
# 3. Assignment Description:
#      -describe what this program is meant to do-
# 4. What was the hardest part? Be as specific as possible.
#      -a paragraph or two about how the assignment went for you-
# 5. How long did it take for you to complete the assignment?
#      -total time in hours including reading the assignment and submitting the program-

import json


def main():
    # file_name = input("please input file name: ")
    # array = open_file(file_name)
    # sort(array)
    # print(array)

    # test 1
    array1 = open_file("Lab08.empty.json")
    array1_test = open_file("Lab06.empty.json")
    sort(array1)
    print(array1 == array1_test)
    print(array1)
    print()

    # test 2
    array1 = open_file("Lab08.trivial.json")
    sort(array1)
    print(array1)
    print()

    # test 3
    array1 = open_file("Lab08.languages.json")
    array1_test = open_file("Lab06.languages.json")
    sort(array1)
    print(array1 == array1_test)
    print(array1)
    print()

    # test 4
    array1 = open_file("Lab08.states.json")
    sort(array1)
    print(array1)
    print()

    # test 5
    array1 = open_file("Lab08.cities.json")
    sort(array1)
    print(array1)
    print()


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


def sort(array):
    """
    This takes an array and sorts it.
    """
    # loops throught the array backwards
    for i_pivot in range(len(array) - 1, 0, -1):
        i_largest = 0

        for i_check in range(0, i_pivot):
            if array[i_check] > array[i_largest]:
                i_largest = i_check

        # Checks if the value at i_largest is larger then i_pivot
        # If yes swaps the values
        if array[i_largest] > array[i_pivot]:
            large_temp = array[i_largest]
            small_temp = array[i_pivot]

            array[i_largest] = small_temp
            array[i_pivot] = large_temp


main()
