import math

# numbers = [True, True]
# numbers[0] = numbers[1] = False

# for factor = 2 .... math.sqrt(number+1):
#     if numbers[factor]:
#         for multiple = factor * 2 ... number + 1 by factor
#             numbers[multiple] = False

# for index = 2 ... number
#     if numbers[index]
#         primes.push_back(index)

numbers = []

# target_num = input("Enter nth term to check")
# target_num = int(target_num)

target_num = 20

# Build list
for num in range(0, target_num):
    numbers.append(True)

# Initially false
numbers[0] = False
numbers[1] = False

# First loop check every value
for factor in range(2, int(math.sqrt(target_num) + 1)):
    # If value is true, check it
    if numbers[factor]:
        #
        for multiple in range(factor * 2, target_num, factor):  # by factor
            numbers[multiple] = False  # falls out of range...

for index in range(2, target_num):
    if numbers[index]:
        print(index)
