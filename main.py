# Imports
import math
import sys
import datetime
import currentaccount
import savingsaccount

# Define global variables
x = datetime.datetime.now()

#####
#####

# LOGIN SYSTEM

#####
#####

logged = False

# Username, Password
accounts = [
    ["admin", "1234"]
]

# Store logged in users details
loggedUser = []

# Take inputs for the user to login to the system
username = input("Enter your username: ")
password = input("Enter your password: ")

# Search through the rows in the 2D lists, to find a matching username and password in the same row
for row in accounts:
    if row[0] == username and row[1] == password:
        print("Details correct - logged in!")
        logged = True

    else:
        print("Details incorrect, try again")

        # We require this section to create a single list, rather than a 2D list
        for column in row:
            loggedUser.append(column)
        break

# Menu system - this does not activate until the user is confirmed to have matching credentials
while logged:

# END 0F LOGIN FORM


# START OF BANKING APP


    print("\n\n\nTHIS IS A BANKING APP PROTOTYPE")



    def account():
        print("\n\n\nWould you like to make a changes to your current account or savings account? \n curr=Current save=Savings q=QUIT\n")
        transact = str(input())
        transact = transact.lower()
        startup(transact)

    def startup(confirm):
        run = True
        while run:
            if confirm == "curr" or confirm == "current":
                currentaccount.prompt()
            elif confirm == "save" or confirm == "savings":
                savingsaccount.prompt()
            elif confirm == "q" or confirm == "quit":
                print("Exiting...")
                sys.exit()
            else:
                print("Input invalid")
                account()


    def main():
        account()
        

    main()