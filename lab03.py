# 1. Name:
#      Calvin Bullock
# 2. Assignment Name:
#      Lab 04: Monopoly
# 3. Assignment Description:
#      -describe what this program is meant to do-
# 4. What was the hardest part? Be as specific as possible.
#      Was it the syntax of Python?
#      Was it an aspect of the problem you are to solve?
#      Was it the instructions or any part of the problem definition?
#      Was it the submission process?
# 5. How long did it take for you to complete the assignment?
#      -total time in hours including reading the assignment and
#       submitting the program-


def number_flop(num):
    # This functions translates the users input of constructed buildings
    # on a propertie to how many houses need to be built.
    # 0 = 4, 1 = 3, 2 = 2, 3 = 1, 4 = 0, 5 = 0

    # paramiters
    # (int)

    # returns
    # (int)
    if num == 0:
        return 4
    elif num == 1:
        return 3
    elif num == 2:
        return 2
    elif num == 3:
        return 1
    elif num == (4 or 5):
        return 0


colour_prompt = input("Do you own all the green properties? (y/n): ")

if colour_prompt.lower() == "y":
    prompt_PA = input(
        "What is on Pennsylvania Avenue? (0:nothing, 1:one house, ... 5:a hotel) "
    )
    prompt_PA = int(prompt_PA)

    print("line 23")
    if prompt_PA != 5:
        prompt_NC = input(
            "What is on North Carolina Avenue? (0:nothing, 1:one house, ... 5:a hotel) "
        )
        prompt_NC = int(prompt_NC)
        print("line 27")

        if prompt_NC != 5:
            prompt_pc = input(
                "What is on Pacific Avenue? (0:nothing, 1:one house, ... 5:a hotel) "
            )
            prompt_pc = int(prompt_pc)

            if prompt_pc != 5:
                num_hotels = input("How many hotels are there to purchase? ")
                num_hotels = int(num_hotels)

                if num_hotels > 0:
                    num_house_PC_need = number_flop(prompt_pc)
                    num_house_NC_need = number_flop(prompt_NC)
                    num_house_total_need = (
                        number_flop(prompt_PA) + num_house_PC_need + num_house_NC_need
                    )
                    total_money_need = 200 * num_house_total_need

                    wallet_size = input("How much cash do you have to spend? ")
                    wallet_size = int(wallet_size)

                    if total_money_need < wallet_size:
                        houses = input("How many houses are there to purchase?")
                        num_houses = int(houses)

                        if num_houses < num_house_total_need:
                            if num_house_NC_need > 0:
                                print(
                                    "This will cost $[price].\
                                        Purchase 1 hotel and [number of houses] house(s).\
                                        Put 1 hotel on Pennsylvania and return any houses to the bank.\
                                        Put [number of houses] house(s) on North Carolina.\
                                        Put [number of houses] house(s) on Pacific."
                                )
                                print(
                                    "This will cost $[price].\
                                        Purchase 1 hotel and [number of houses] house(s).\
                                        Put 1 hotel on Pennsylvania and return any houses to the bank.\
                                        Put [number of houses] house(s) on North Carolina."
                                )

                            elif num_house_PC_need > 0:
                                print(
                                    "This will cost $[price].\
                                        Purchase 1 hotel and [number of houses] house(s).\
                                        Put 1 hotel on Pennsylvania and return any houses to the bank.\
                                        Put [number of houses] house(s) on North Carolina.\
                                        Put [number of houses] house(s) on Pacific."
                                )
                                print(
                                    "This will cost $[price].\
                                         Purchase 1 hotel and [number of houses] house(s).\
                                         Put 1 hotel on Pennsylvania and return any houses to the bank.\
                                         Put [number of houses] house(s) on Pacific."
                                )


# print("You do not have sufficient funds to purchase a hotel at this time.")

# print("There are not enough houses available for purchase at this time.")
# print("There are not enough hotels available for purchase at this time.")
# print(
#     "You cannot purchase a hotel until you own all the properties of a given color group."
# )

# print("You cannot purchase a hotel if the property already has one.")
# print("Swap North Carolina's hotel with Pennsylvania's 4 houses.")
# print("Swap Pacific's hotel with Pennsylvania's 4 houses.")

# A
# print(
#     "This will cost $[price].\
#          Purchase 1 hotel and [number of houses] house(s).\
#          Put 1 hotel on Pennsylvania and return any houses to the bank.\
#          Put [number of houses] house(s) on North Carolina.\
#          Put [number of houses] house(s) on Pacific."
# )

# B
# print(
#     "This will cost $[price].\
#          Purchase 1 hotel and [number of houses] house(s).\
#          Put 1 hotel on Pennsylvania and return any houses to the bank.\
#          Put [number of houses] house(s) on North Carolina."
# )

# C
# print(
#     "This will cost $[price].\
#          Purchase 1 hotel and [number of houses] house(s).\
#          Put 1 hotel on Pennsylvania and return any houses to the bank.\
#          Put [number of houses] house(s) on Pacific."
# )

# D
# print(
#     "This will cost $[price].\
#          Purchase 1 hotel and [number of houses] house(s).\
#          Put 1 hotel on Pennsylvania and return any houses to the bank."
# )
