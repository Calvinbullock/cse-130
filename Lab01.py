# 1. Name: 
#    Calvin Bullock

# 2. Assignment Name: 

#    Lab 01: Python Review
# 3. Assignment Description:

#    This program will select a random number after prompting the user for a range.
#    It will then have them try to guess that random number. At teh end it will
#    tell the user how many guess it took them.

# 4. What was the hardest part? Be as specific as possible.
#    The hardest part was figuring out how to propmt the user for the guess, 
#    then enter the loop with out reasking the user to guess. The loop uses the guess 
#    to deturmin if the game is over. So I had to ask before teh loop starts but then 
#    ask again in the loop. To solve this I used an if stamant to skip the inner prompt
#    on the first loop iteration. 

# 5. How long did it take for you to complete the assignment?
#    -1.40 

import random

# from stack overflow - https://stackoverflow.com/questions/8924173/how-can-i-print-bold-text-in-python
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
END = '\033[0m'

# Game introduction.
print("This is the \"guess a number\" game.")
print("You try to guess a random number in the smallest number of attempts.\n")

# Prompt the user for how difficult the game will be. Ask for an integer.
value_max = input(f"How difficult do you want the game to be?\n(Give a max value as an intager): {BOLD}{UNDERLINE}")

# Generate a random number between 1 and the chosen value.
value_random = random.randint(1, int(value_max))

# Give the user instructions as to what he or she will be doing.
print(f"{END}Guess a number between 1 and {value_max}.")

# Initialize the sentinal and the array of guesses.
guess_list = []
guess_list.append(int(input(f"> {BOLD}{UNDERLINE}")))
i = 0

# Play the guessing game.
while guess_list[len(guess_list)-1] != value_random:
    i+=1

    # Prompt the user for a number.
    if i > 1:
        guess = input(f"{END}> {BOLD}{UNDERLINE}")

    # Store the number in an array so it can be displayed later.
        guess_list.append(int(guess))

    # Make a decision: was the guess too high, too low, or just right.
    if guess_list[len(guess_list)-1] > value_random:
        print(f"{END}\t Too High!")
    
    elif guess_list[len(guess_list)-1] < value_random:
        print(f"{END}\t Too Low!")
    
# Give the user a report: How many guesses and what the guesses where.
guess_num = len(guess_list)
guess_list_out = f"{END}["

for i in guess_list:
    if i != guess_list[len(guess_list)-1]:
        guess_list_out = guess_list_out + str(i) + ", "
    else:
        guess_list_out = guess_list_out + str(i) + "]"

print(f"{END}You were able to find the number in {guess_num} guesses.")
print(f"The numbers you guessed were: {guess_list_out}")



""" Test cases
At the first prompt, select the value 1. Guess 1 on your first attempt.
At the first prompt, select the value 1. Guess 0, then 2, then 1.
At the first prompt, select the value 10 and play the game the best you can.
At the first prompt, select the value 50 and play the game the best you can.
"""