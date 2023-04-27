# 1. Name: 
#    Calvin Bullock
# 
# 2. Assignment Name: 
#    Lab 02: Python Review
# 
# 3. Assignment Description:
#    This program will take input for a password and user name and compare it
#    the usernames and passwords stored in a json. If the password matches the 
#    password stored for that user name it will allow acsses.
# 
# 4. What was the hardest part? Be as specific as possible.
#    Working out how to interact with the json file. Both getting the file to 
#    parse and also getting the lists to work in comparing agenst the input.
#    It was hard finding the syntax to correctly format the json then use the 
#    parsed json to interact with the stored lists.
# 
# 5. How long did it take for you to complete the assignment?
#    2 Hours

import json

def Authentication(user_name_in, password_in):
    """
    This functions check if the password matches the user.
    It takes two strings and returns a bool.

    user_name_in (string)
    password_in  (String)

    returns:
    A bool
    """

    # Double loop from:
    # https://stackoverflow.com/questions/18648626/for-loop-with-two-variables 
    # This will look to see that the index of the username and password match.
    for i, j in zip(dict['username'], dict['password']):
        if i == user_name_in and j == password_in:
            return True
        
    return False

def Login_Log(authorized):
    """
    This functions check if the password matches the user.
    It takes a bool and returns nothing.
    Makes a print statment.
    """
    if authorized:
        print("You are authenticated!.")
    else:
        print("You are not authorized to use the system.")

# checks if the the file opens and if the dictinary can be used.
try:
    # Opens the file Lab02,json and converts it to python dictinary.
    file = open("Lab02.json")
    data = file.read()
    dict = json.loads(data)

    #Normal input code
    """ 
    # Takes input from the user for password and username.
    user_name_in = input("Username: ")
    password_in = input("Password: ")

    # Passes the username and password input by the user and checks them. 
    Login_Log(Authentication(user_name_in, password_in))
    """

    # Auto test cases
    print("Username: John Cheese, Password: None shall pass")
    Login_Log(Authentication("John Cheese", "None shall pass"))
    print()

    print("Username: Black Knight, Password: Tis but a scratch.")
    Login_Log(Authentication("Black Knight", "Tis but a scratch"))
    print()

    print("Username: Black Knight, Password: None shall pass.")
    Login_Log(Authentication("Black Knight", "None shall pass"))

    file.close()

except:
    print("Data unreachable")
