from time import sleep
import json


def type(message):
    for i in message:
        print(i, flush=True, end="")
        sleep(0.02)
    print("")  # newline


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
        for person in information.values():
            type(str(person["Name"] + " : " + person["Address"]))


def option2():
    type("What is the new student's name?")
    name = input("> ")

    type("What is the new student's address?")
    address = input("> ")

    number = len(information.keys()) + 1
    student = {number: {"Name": name, "Address": address}}

    information.update(student)
    save()


# init
type("\nWelcome to a brand new address book!\n")
while True:

    welcome()
    welcomeMenu = input("> ")
    if welcomeMenu == "1":
        option1()

        while True:
            type("\n\nWould you like to go back to the main menu? (y/n)")
            choice = input("> ")
            choice = choice.lower()

            if choice == "y":
                print("\n\n")
                break
            else:
                sleep(5)
                continue
        continue

    elif welcomeMenu == "2":
        option2()

        while True:
            type("\n\nWould you like to go back to the main menu? (y/n)")
            choice = input("> ")
            choice = choice.lower()

            if choice == "y":
                print("\n\n")
                break
            else:
                sleep(5)
                continue
        continue

    elif welcomeMenu == "3":
        pass

        while True:
            type("\n\nWould you like to go back to the main menu? (y/n)")
            choice = input("> ")
            choice = choice.lower()

            if choice == "y":
                print("\n\n")
                break
            else:
                sleep(5)
                continue
        continue

    elif welcomeMenu == "4":
        exit()
    else:
        type("Thats not an option!")
