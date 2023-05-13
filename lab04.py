# 1. Name:
#      Calvin Bullock
# 2. Assignment Name:
#      Lab 04: Monopoly
# 3. Assignment Description:
#      This program determines if you can or how to put a hotel on
#      Pennsylvania Avenue in the game of monopoly.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was finding meaningful places to put comments and
#      makeing the comments meaningful.
# 5. How long did it take for you to complete the assignment?
#      4 hours


def number_lot(num):
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


# Asks if you have all the green colour properties.
colour_prompt = input("Do you own all the green properties? (y/n): ")

# Checks if you have all the green colour properties
# Converts prompt to lower case for consistancey.
if colour_prompt.lower() == "y":
    prompt_PA = input(
        "What is on Pennsylvania Avenue? (0:nothing, 1:one house, ... 5:a hotel) "
    )
    prompt_PA = int(prompt_PA)

    # Ends if hotel is on Pennsylvania Avenue ends program if prompt_pa = 5
    if prompt_PA != 5:
        prompt_NC = input(
            "What is on North Carolina Avenue? (0:nothing, 1:one house, ... 5:a hotel) "
        )
        prompt_NC = int(prompt_NC)

        # Ends if hotel is on Carolina Avenue ends program if prompt_NC = 5
        if prompt_NC != 5:
            prompt_pc = input(
                "What is on Pacific Avenue? (0:nothing, 1:one house, ... 5:a hotel) "
            )
            prompt_pc = int(prompt_pc)

            # Ends if hotel is on Pacific Avenue? ends program if prompt_PC = 5
            if prompt_pc != 5:
                num_hotels = input("How many hotels are there to purchase? ")
                num_hotels = int(num_hotels)

                if num_hotels > 0:
                    # Sets the number of houses needed, total cost needed
                    # total amount of money you have (wallet).
                    num_house_PC_need = number_lot(prompt_pc)
                    num_house_NC_need = number_lot(prompt_NC)
                    num_house_total_need = (
                        number_lot(prompt_PA) + num_house_PC_need + num_house_NC_need
                    )

                    # The number of house tokkens needed and pluse 200 for a hotel
                    total_money_need = 200 * num_house_total_need + 200
                    wallet_size = input("How much cash do you have to spend? ")
                    wallet_size = int(wallet_size)

                    # If the cost is grater then the users wallet program ends
                    if total_money_need < wallet_size:
                        houses = input("How many houses are there to purchase? ")
                        num_houses = int(houses)

                        if num_houses >= num_house_total_need:
                            if num_house_NC_need > 0:
                                print(
                                    f"This will cost ${total_money_need}."
                                    f"\nPurchase 1 hotel and {num_house_total_need} house(s)."
                                    "\nPut 1 hotel on Pennsylvania and return any houses to the bank."
                                    f"\nPut {num_house_NC_need} house(s) on North Carolina."
                                    f"\nPut {num_house_PC_need} house(s) on Pacific.\n"
                                )
                                print(
                                    f"This will cost ${total_money_need}."
                                    "\nPurchase 1 hotel and [number of houses] house(s)."
                                    "\nPut 1 hotel on Pennsylvania and return any houses to the bank."
                                    f"\nPut {num_house_NC_need} house(s) on North Carolina.\n"
                                )

                            if num_house_PC_need > 0:
                                print(
                                    f"This will cost ${total_money_need}."
                                    f"\nPurchase 1 hotel and {num_house_total_need} house(s)."
                                    "\nPut 1 hotel on Pennsylvania and return any houses to the bank."
                                    f"\nPut {num_house_NC_need} house(s) on North Carolina."
                                    f"\nPut {num_house_PC_need} house(s) on Pacific.\n"
                                )
                                print(
                                    f"This will cost ${total_money_need}."
                                    "\nPurchase 1 hotel and [number of houses] house(s)."
                                    "\nPut 1 hotel on Pennsylvania and return any houses to the bank."
                                    f"\nPut {num_house_PC_need} house(s) on Pacific.\n"
                                )
                        else:
                            print(
                                "There are not enough houses available for purchase at this time."
                            )
                    else:
                        print(
                            "You do not have sufficient funds to purchase a hotel at this time."
                        )

                else:
                    print(
                        "There are not enough hotels available for purchase at this time."
                    )

            else:
                print("Swap Pacific's hotel with Pennsylvania's 4 houses.")

        else:
            print("Swap North Carolina's hotel with Pennsylvania's 4 houses.")

    else:
        print("You cannot purchase a hotel if the property already has one.")

else:
    print(
        "You cannot purchase a hotel until you own all the properties of a given color group."
    )
