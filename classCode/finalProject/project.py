from os import system, name
from time import sleep
import json


def type(message):
    for i in message:
        print(i, flush=True, end="")

        sleep(0.02)
    print("")  # newline


def clear():

    if name == "nt":
        _ = system("cls")

    else:
        _ = system("clear")


try:
    data = open("database.json", "r")
    information = json.load(data)
    data.close()

except JSONDecodeError:
    information = {}


def welcome():

    type("Here is the menu:")
    type("1. View the address book")
    type("2. Insert a new entry")
    type("3. Delete an entry")
    type("4. Quit the program\n")

    type("Choose an option:")


def save():
    data = open("database.json", "w")
    json.dump(information, data)
    data.close()


def option1():
    if len(information) == 0:
        type("The address book is empty. Populate it with data first!")

    else:
        for key, person in information.items():
            type(str(key + ". " + person["Name"] + " : " + person["Address"]))


def option2():
    type("What is the new student's name?")
    name = input("> ")

    type("What is the new student's address?")
    address = input("> ")

    number = len(information.keys()) + 1
    student = {number: {"Name": name, "Address": address}}

    try:
        information.update(student)
        save()
        print("The student was successfully added!")
    except:
        print("An unknown error occurred. Please try again later.")


def option3():
    for key, person in information.items():
        type(str(key + ". " + person["Name"] + " : " + person["Address"]))

    type("\n\nType the number of the student you would like to remove:")
    num = input("> ")

    try:
        del information[num]
    except:
        type("That student doesn't exist!")


def returnMenu():
    while True:
        type("\n\nWould you like to go back to the main menu? (y/n)")
        choice = input("> ")
        choice = choice.lower()

        if choice == "y":
            print("\n\n")
            clear()
            break
        else:
            sleep(5)
            continue


# init


while True:
    clear()
    type("\nWelcome to a brand new address book!\n")
    welcome()
    welcomeMenu = input("> ")
    clear()
    if welcomeMenu == "1":
        option1()

        returnMenu()
        continue

    elif welcomeMenu == "2":
        option2()

        returnMenu()
        continue

    elif welcomeMenu == "3":
        option3()

        returnMenu()
        continue

    elif welcomeMenu == "4":
        exit()
    else:
        type("Thats not an option!")
