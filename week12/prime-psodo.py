# this        {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}
# to this     {2, 3, 5, 7, 11, 13, 17, 19}

# count by 1, 2,3,4 ect
# add indexs that are croseed out to an array

target_value = 25
count_list = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}
list_2s = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24}
list_3s = {3, 6, 9, 12, 15, 18, 21, 24}
list_5s = {5, 10, 15, 20, 25}

black_index_list = []

count_2s = 0
count_3s = 0
count_5s = 0

for index, value in enumerate(count_list): # iterate count list
    current_i = 0

    count_by = 2
    count = 0

    while count < target_value:
        if count == value:
            black_index_list.append(index)


    # while list_2s[current_i] != count_list[index] and current_i < len(list_2s) : # iterate coutn_2s


    
    black_index_list.append(index) # hits this if not in any other list



# for index in range(0, len(black_index_list)):
    # print(index)

print(black_index_list)