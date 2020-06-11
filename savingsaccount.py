import math
import sys
import datetime

x = datetime.datetime.now()

def prompt():
    print("\n\n\nWould you like to make a transaction, view your statement or check balance? \n t=transaction s=statement b=balance q=QUIT\n")
    transact = str(input())
    transact = transact.lower()
    startup(transact)

def startup(confirm):
    run = True
    while run:
        if confirm == "transaction" or confirm == "t":
            transaction_option()
        elif confirm == "statement" or confirm == "s":
            checkLog()
            prompt()
        elif confirm == "balance" or confirm == "b":
            checkBalance()
            prompt()
        elif confirm == "no" or confirm == "n" or confirm == "quit" or confirm == "q":
            print("Exiting...")
            sys.exit()
        else:
            print("Input invalid")
            prompt()

def transaction_option():
    print("\nWould you like to make a deposit or a withdrawal? \n d=Deposit w=Withdrawal q=QUIT\n")
    change = str(input(""))
    change = change.lower()
    if change == "deposit" or change == "d":
        deposit_money()
    elif change == "withdrawal" or change == "w":
        withdrawMoney()
    elif change == "quit" or change == "exit":
        print("Exiting...")
        sys.exit()
    else:
        print("Invalid input")
        
def checkBalance():
    file = open("Savings-BankData.txt", "r")
    print("Current balance")
    print(file.read())
    current = open("Savings-BankData.txt", "r").read()
    floatCurrent = float(current)
    file.close()
    

def checkLog():
    file = open("Savings-TransactionLog.txt", "r")
    print("Full transaction log")
    print(file.read())
    current = open("Savings-TransactionLog.txt", "r").read()
    file.close()

def deposit_money():
    checkBalance()
    depositAction()

def depositAction():
    try:
        file = open("Savings-BankData.txt", "r")
        current = open("Savings-BankData.txt", "r").read()
        floatCurrent = float(current)
        file.close()
    
        print("How much would you like to deposit?")
        addedAmount = input()
        floatAddedAmount = float(addedAmount)
        file = open("Savings-BankData.txt", "w")
        newAmount = floatCurrent + floatAddedAmount
        newAmount = str(newAmount)
        file.write(newAmount)
        file.close()
        file = open("Savings-BankData.txt", "r")
        print("New Amount is: ")
        print(file.read())
        file.close()
        transactionOccured = "+"
        transactionLogs(floatCurrent, transactionOccured, floatAddedAmount, newAmount)
    except ValueError:
        print("You provided an invalid input.")


def withdrawMoney():
    checkBalance()
    withdrawalAction()

def withdrawalAction():
    try:
        file = open("Savings-BankData.txt", "r")
        current = open("Savings-BankData.txt", "r").read()
        floatCurrent = float(current)
        file.close()
    
        print("How much would you like to withdraw?")
        addedAmount = input()
        floatAddedAmount = float(addedAmount)
        file = open("Savings-BankData.txt", "w")
        newAmount = floatCurrent - floatAddedAmount
        newAmount = str(newAmount)
        file.write(newAmount)
        file.close()
        file = open("Savings-BankData.txt", "r")
        print("New Amount is: ")
        print(file.read())
        file.close()
        transactionOccured = "-"
        transactionLogs(floatCurrent, transactionOccured, floatAddedAmount, newAmount)
    except ValueError:
        print("You provided an invalid input.")


def transactionLogs(floatCurrent, transactionOccured, floatAddedAmount,newAmount):
    LOG = open("Savings-TransactionLog.txt", "a")
    oldAmount = floatCurrent
    oldAmount = str(floatCurrent)
    transactionType = transactionOccured
    transactionAmount = floatAddedAmount
    transactionAmount = str(transactionAmount)
    updatedAmount = newAmount
    updatedAmount = str(newAmount)
    LOG.write("\n\nOld Balance: " + oldAmount)
    LOG.write("\nTransaction Amount: " + transactionType + transactionAmount)
    LOG.write("\nTransaction Date and time")
    LOG.write(x.strftime(' %c'))
    LOG.write("\nNew Balance: " + updatedAmount)
    
