import json

def main():
    # file_name = input("please input file name: ")
    file_name = "Lab08.languages.json"
    array = open_file(file_name)
    sort(array)
    print(array)


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
    for i_pivot in range(array.length - 1, 0, -1):
        i_largest = 0

        for i_check in range(0, i_pivot-1):

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