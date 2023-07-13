# 1. Name:
#      Calvin BUllock-
# 2. Assignment Name:
#      Lab 13: Prime Numbers
# 3. Assignment Description:
#      This Program will calculate prime to the nth number.
# 4. What was the hardest part? Be as specific as possible.
#      -a paragraph or two about how the assignment went for you-
# 5. How long did it take for you to complete the assignment?
#      2 Hours

import math


def main():
    # Testing
    # prime_iterater(-1)
    # print()
    # prime_iterater(0)
    print()
    prime_iterater(1)
    print()
    prime_iterater(2)
    print()
    prime_iterater(10)
    print()
    prime_iterater(53)
    print()
    prime_iterater(100)
    print()
    prime_iterater(200)
    print()

    # User Run
    exit = True
    target_num = 0

    # Run until valid target entered
    while exit:
        target_num = input("Enter nth term to check: ")
        target_num = int(target_num)

        if target_num > 0:
            exit = False

        else:
            print("Please enter number greater then zero")

    prime_iterater(target_num)


def prime_iterater(target_num):
    # This function computes prime numbers up to the target_num.
    #
    # Paramiters:
    #    [Target_num: int] - the nth term to cumpute prime up to
    #
    numbers = []

    # Build list
    for num in range(0, target_num + 1):
        numbers.append(True)

    # Initially false
    numbers[0] = False
    numbers[1] = False

    # First loop check every value
    for factor in range(2, int(math.sqrt(target_num) + 1)):
        # If value is true, check it
        if numbers[factor]:
            # Iterate along factore
            for multiple in range(factor * 2, target_num, factor):  # by factor
                numbers[multiple] = False  # falls out of range...

    # Print out primes in list
    for index in range(2, target_num):
        if numbers[index]:
            print(f"{index}, ", end="")

    print()


main()


# Visuwal checking
# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
# 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127,
# 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191,
# 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257,
# 263, 269, 271, 277, 281, 283, 293.
