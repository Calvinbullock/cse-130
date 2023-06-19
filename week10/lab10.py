# 1. Name:
#      Calvin Bullock
# 2. Assignment Name:
#      Lab 10: Numeric Sequence
# 3. Assignment Description:
#      This program computes the nth François number.
# 4. What was the hardest part? Be as specific as possible.
#      -TODO a paragraph or two about how the assignment went for you-
# 5. How long did it take for you to complete the assignment?
#      -TODO total time in hours including reading the assignment and submitting the program-


def main():
    # TRUE RUN
    if __debug__ == False:
        target_i = input("for target index: ")
        target_i = int(target_i)
        francois_number(target_i)

    # DEBUG TEST cases
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

    # if the target is less then 2 term.
    if target_i < 2:
        print(francois_array[target_i])
        print()

    # if the target is further then the 3rd term.
    else:
        while count < target_i:
            # Take the two values stored in teh array and add them together
            temp_value = francois_array[0] + francois_array[1]
            # Move the array values back with the temp becomeing the 2nd value
            francois_array[0] = francois_array[1]
            francois_array[1] = temp_value

            count += 1

        print(francois_array[1])
        print()

main()
