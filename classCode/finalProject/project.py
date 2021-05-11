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
    type("Welcome to a brand new address book!\n")
    type("Here is the menu:")
    type("1. View the address book")
    type("2. Insert a new entry")
    type("3. Delete an entry")
    type("4. Quit the program\n")

    type("Choose an option:")
    welcomeMenu = input("> ")


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
