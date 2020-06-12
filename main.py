# Imports
import math
import sys
import datetime
import currentaccount
import savingsaccount
import csv

# tkinter imports
# import tkinter as tk
# from tkinter import ttk

# Define global variables
x = datetime.datetime.now()

#####
#####


#####
#####


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
            # line below for tkinter, however, it runs auto and skips the login step
            # savingsaccount.mainloop()
        elif confirm == "q" or confirm == "quit":
            print("Exiting...")
            sys.exit()
        else:
            print("Input invalid")
            account()

# LOGIN SYSTEM

def read_data():
    data = []
    # open and read data from csv file
    with open('users.csv') as csv_file:
        read_csv = csv.reader(csv_file, delimiter=',')
        # read and store data
        for row in read_csv:
            data.append(row)
    # return list of elements
    return data


def check_login(username, password, users):
    # cycle through rows to find username and password match
    for row in users:
        # check for match
        if username == row[1] and password == row[2]:
            # return true if match is found
            return row
    # return false if no match is found
    return False


def login(username, password, user_data):
    # call check_login function to validate
    check = check_login(username, password, user_data)
    # if check_login returns False:
    if not check:
        print("Invalid Login!")
    # if check_login does not return False:
    else:
        print("Welcome,", check[3])
        account()

def question():
    # request username and password
    username = input("Please enter Username: ")
    password = input("Please enter Password: ")
    # call login function with user input + read_data() return
    login(username, password, read_data())

# Comment line below out to use tkinter gui
question()

# END 0F LOGIN FORM






# TKINTER

# Cannot get GUI to work with login form, it instantly outputs invalid login


# root = tk.Tk()

# username = tk.StringVar()
# password = tk.IntVar()

# lblUsername = ttk.Label(root, text="Enter username: ", padding=(10, 10))
# lblUsername.pack()

# username = ttk.Entry(root, textvariable=username)
# username.pack()

# lblUserpass = ttk.Label(root, text="Enter password:", padding=(10, 10))
# lblUserpass.pack()

# password = ttk.Entry(root, textvariable=password)
# password.pack()

# btnSubmit = ttk.Button(root, text="Submit", command=login(username, password, read_data()))
# btnSubmit.pack()


# root.mainloop()