# 1. Name:
#      -your name-
# 2. Assignment Name:
#      Lab 10: Numeric Sequence
# 3. Assignment Description:
#      -describe what this program is meant to do-
# 4. What was the hardest part? Be as specific as possible.
#      -a paragraph or two about how the assignment went for you-
# 5. How long did it take for you to complete the assignment?
#      -total time in hours including reading the assignment and submitting the program-

def main():
    if __debug__ == False:
        target_i = input("for target index: ")
        target_i = int(target_i)
        francois_number(target_i)

    if __debug__:
        francois_number(-1)
        francois_number(0)
        francois_number(1)
        francois_number(2)
        francois_number(9)
        francois_number(100)
        francois_number(200)


def francois_number(target_i):
    assert target_i > -1

    count = 1
    francois_array = [2, 1]

    if target_i < 2:
        print(francois_array[target_i])
        print()

    else:
        while count < target_i:
            temp_value = francois_array[0] + francois_array[1]
            francois_array[0] = francois_array[1]
            francois_array[1] = temp_value

            count += 1

        print(francois_array[1])
        print()


main()