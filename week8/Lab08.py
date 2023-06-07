# 1. Name:
#      Calvin Bullock
# 2. Assignment Name:
#      Lab 08: Sort
# 3. Assignment Description:
#      This program will sort a list pulled from a json file
# 4. What was the hardest part? Be as specific as possible.
#      Figuring out what you ment with your sudo code and translating it 
#      into python code 
# 5. How long did it take for you to complete the assignment?
#      2 Hours

import json


def main():
    # ------------ -------------------------- ------------ #
    # ------------ ----- For production ----- ------------ #
    # ------------ -------------------------- ------------ #
    # file_name = input("please input file name: ")
    # array = open_file(file_name)
    # sort(array)
    # print(array)

    # ------------ -------------------------- ------------ #
    # ------------- Comment out in Production ------------ #
    # ------------ -------------------------- ------------ #
    # I call my sort then the built in sort and compare them for testing

    # ---------------------- test 1 ---------------------- # 
    array1 = open_file("Lab08.empty.json")
    array1_test = open_file("Lab08.empty.json")
    
    sort(array1)
    array1_test.sort()

    print(array1 == array1_test)
    print(array1)
    print()

    # ---------------------- test 2 ---------------------- # 
    array1 = open_file("Lab08.trivial.json")
    array1_test = open_file("Lab08.trivial.json")

    sort(array1)
    array1_test.sort()

    print(array1 == array1_test)
    print()

    # ---------------------- test 3 ---------------------- # 
    array1 = open_file("Lab08.languages.json")
    array1_test = open_file("Lab08.languages.json")

    sort(array1)
    array1_test.sort()

    print(array1 == array1_test)
    print(array1)
    print()

    # ---------------------- test 4 ---------------------- # 
    array1 = open_file("Lab08.states.json")
    array1_test = open_file("Lab08.states.json")

    sort(array1)
    array1_test.sort()

    print(array1 == array1_test)
    print(array1)
    print()

    # ---------------------- test 5 ---------------------- # 
    array1 = open_file("Lab08.cities.json")
    array1_test = open_file("Lab08.cities.json")

    sort(array1)
    array1_test.sort()

    print(array1 == array1_test)
    print(array1)
    print()

    # ------------------- Assert test 6 ------------------- # 
    # num = 0
    # sort(num)


def open_file(file_name):
    # Opens a json file and returns an array from it
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
    assert type(array) == type([])

    # Loops throught the array backwards
    for i_pivot in range(len(array) - 1, 0, -1):
        i_largest = 0

        assert 0 <= i_pivot < len(array)

        # Loops to find highest value ___ in array
        for i_check in range(0, i_pivot):
            assert 0 <= i_check < len(array)

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
