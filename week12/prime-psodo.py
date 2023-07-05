# Calvin Bullock

# -- Promgram --
# Compute prime numbs to the nth term with out modulo

import math

# Quick visuwal test
# n = 20 { 2, 3, 5, 7, 11, 13, 17, 19 }
# n = 100 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97.

# # TODO Quick Testing
# target_value = 25
# target_value = 100

# Take user input
target_value = input("Enter your nth number you would like to compute until: ")
target_value = int(target_value)

count_list = []

# Create array until target Num
for num in range(0, target_value):
    count_list.append(num)

# Iterate count list
for index, value in enumerate(count_list):
    # Prime but special and hard to compute as so
    if value == 2 or value == 3 or value == 5 or value == 7:
        pass

    # Not prime but special and hard to compute as so
    elif value == 0 or value == 1:
        count_list[index] = 0

    else:
        # Find the max int to multiplication table
        max_count_by = int(math.sqrt(target_value))

        # Count by x to check if value is divisable by x
        for count_by in range(2, max_count_by):
            count = 0

            # If count < value has not reached value yet, keep going
            # if count != value keep going
            while count < value and count != value:
                count += count_by

                # If count == value, value is not prime
                if count == value:
                    count_list[index] = 0

# Final print out
for value in count_list:
    if value != 0:
        print(f"{value}, ", end="")

print()
