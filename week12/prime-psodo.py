# Calvin Bullock

target_value = 25

count_list = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    23,
    24,
    25,
]
# { 2, 3, 5, 7, 11, 13, 17, 19 } -- primes

white_index_list = []

for index, value in enumerate(count_list):  # iterate count list
    # set prime defualt
    prime = True

    for count_by in range(2, 6):  # count by x
        count = 0

        # If count < value has not reached value yet, keep going
        # if count != value keep going
        while count < value and count != value:
            count += count_by

            # If count == value, value is not prime
            if count == value:
                prime = False

    # If count < value then the while termanated before reaching vlaue and
    if prime:
        white_index_list.append(index)

# Final print out
for value in white_index_list:
    print(f"{count_list[value]}, ", end="")

print()
