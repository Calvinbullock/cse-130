# 1. Name:
#      Calvin Bullock
# 2. Assignment Name:
#      Lab 10: Numeric Sequence
# 3. Assignment Description:
#      This program computes the nth François number.
# 4. What was the hardest part? Be as specific as possible.
#      Finding meaningful places to put asserts and decideing where to start my function, at 0 or 1
# 5. How long did it take for you to complete the assignment?
#      2 hours


def main():
    # Production RUN
    if __debug__ == False:
        exit = 1

        # Loops until the user gives a proper number
        while exit == 1:
            target_i = input("for target index: ")
            target_i = int(target_i)

            # Protects the exit until user enters a tartget grater then 1
            if target_i < 1:
                print(f"Error: number is to small, try again {target_i}.")
                print()
            else:
                exit = 0

        francois_number(target_i)

    # DEBUG TEST cases
    if __debug__:
        # this will crash
        # francois_number(-1)

        # this will crash
        # print(f"key = 2")
        # francois_number(0)

        print(f"key = 1")
        francois_number(1)

        print(f"key = 3")
        francois_number(2)

        print(f"key = 29")
        francois_number(7)

        print(f"key = 76")
        francois_number(9)

        print(f"key = ?")
        francois_number(100)

        print(f"key = ?")
        francois_number(200)

        # francois_number sequance
        # 1  2  3  4  5  6   7   8   9   10
        # 2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123


def francois_number(target):
    # This function takes an int and caculates the francois number at that
    # place in francois number sequence.
    #
    # Paramiters
    #   target: int the target term of francois number sequence, should be grater then 0

    assert target > 0
    assert type(target) == type(1)

    # take one off of the input to match array indexs
    target_i = target - 1 

    count = 0
    francois_array = [2, 1]

    # if the target is less then 2 term.
    if target_i < 2:
        print(f"Francois number {target} is {francois_array[target_i]}")
        print()

    # if the target is further then the 3rd term.
    else:
        while count < target_i - 1:
            # Take the two values stored in teh array and add them together
            temp_value = francois_array[0] + francois_array[1]

            # Move the array values back with the temp becomeing the 2nd value
            francois_array[0] = francois_array[1]
            francois_array[1] = temp_value

            count += 1

        print(f"Francois number {target} is {francois_array[1]}")
        print()

    assert type(target_i) == type(1)


main()
