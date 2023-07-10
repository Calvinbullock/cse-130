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

target_num = input("Enter nth term to check")
target_num += int(target_num)

for num in range(0, target_num):
    numbers.append(True)

# Initially false
numbers[0] = False
numbers[1] = False


for factor in range (2, math.sqrt(target_num + 1)):
    if numbers[factor]:
        for multiple in range(factor * 2, target_num + 1 by factor):
            numbers[multiple] = False
        
for index in range(2, target_num):
    if numbers[index]:
        primes.push_back(index)