# Calvin Bullock

# TODO 2, 3 are being flaged -- this is bad
# TODO set the invaled int to something we can flag ex. 0

target_value = input("Enter your nth number you would like to compute until: ")
target_value = int(target_value)

count_list = []
white_index_list = []

for num in range(0, target_value):
    count_list.append(num)

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
