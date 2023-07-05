# Calvin Bullock

# TODO set the invaled int to something we can flag ex. 0

# Quick visuwal test
# { 2, 3, 5, 7, 11, 13, 17, 19 }
# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97.

# BUG remove and reinstate input
# BUG remove and reinstate input
# BUG remove and reinstate input
# BUG remove and reinstate input
# target_value = 25
target_value = 100 # 49 - 7

# Take user input
# target_value = input("Enter your nth number you would like to compute until: ")
# target_value = int(target_value)

count_list = []
white_index_list = [] # stores index of prime numbers

# Create array until target Num
for num in range(0, target_value):
    count_list.append(num)

# Iterate count list
for index, value in enumerate(count_list):
    prime = True

    # Prime but special and hard to compute as so
    if value == 2 or value == 3 or value == 5:
        white_index_list.append(index)

    # Prime but special and hard to compute as so
    elif value == 0 or value == 1:
        prime = False

    else:
        # Count by x to check if value is divisable by x
        for count_by in range(2, target_value): # BUG this needs to be more dynamic ------- BUG
            count = 0

            # If count < value has not reached value yet, keep going
            # if count != value keep going
            while count < value and count != value:
                count += count_by

                # If count == value, value is not prime
                if count == value:
                    prime = False
                    count_list[index] = 0 # will set values to 0 for quick exsecution

        if prime:
            white_index_list.append(index)

# Final print out
for value in white_index_list:
    print(f"{count_list[value]}, ", end="")

print()
