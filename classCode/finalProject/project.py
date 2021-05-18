#!/usr/bin/env python3


from os import system, name  # for screen clearing
from time import sleep  # for typewriter effect
import json  # for saving the address book


def type(message):  # same as print, but does a cool typewriter effect
    for i in message:
        print(i, flush=True, end="")

        sleep(0.02)
    print("")  # newline


def clear():  # cleares the screen

    if name == "nt":
        _ = system("cls")

    else:
        _ = system("clear")


class format:  # class for colorized output
    reset = "\033[0m"
    bold = "\033[01m"
    disable = "\033[02m"
    underline = "\033[04m"
    reverse = "\033[07m"
    strikethrough = "\033[09m"
    invisible = "\033[08m"

    class fg:
        black = "\033[30m"
        red = "\033[31m"
        green = "\033[32m"
        orange = "\033[33m"
        blue = "\033[34m"
        purple = "\033[35m"
        cyan = "\033[36m"
        lightgrey = "\033[37m"
        darkgrey = "\033[90m"
        lightred = "\033[91m"
        lightgreen = "\033[92m"
        yellow = "\033[93m"
        lightblue = "\033[94m"
        pink = "\033[95m"
        lightcyan = "\033[96m"

    class bg:
        black = "\033[40m"
        red = "\033[41m"
        green = "\033[42m"
        orange = "\033[43m"
        blue = "\033[44m"
        purple = "\033[45m"
        cyan = "\033[46m"
        lightgrey = "\033[47m"


try:  # tries to save data
    data = open("database.json", "r")
    information = json.load(data)
    data.close()
except:  # returns empty dict if database.json is empty
    information = {}


def welcome():  # main menu

    type("Here is the menu:")
    type(format.fg.green + "1. " + format.reset + "View the address book")
    type(format.fg.green + "2. " + format.reset + "Insert a new entry")
    type(format.fg.green + "3. " + format.reset + "Delete an entry")
    type(format.fg.green + "4. " + format.reset + "Quit the program\n")

    type("Choose an option:")


def save():  # function to save the address book
    data = open("database.json", "w")
    json.dump(information, data)
    data.close()


def nicePrint():  # nicely prints menu
    for name, address in information.items():
        num = list(information.keys()).index(name)  # gets index of key
        type(
            str(
                format.fg.green
                + str(num + 1)
                + ". "
                + format.reset
                + name
                + " : "
                + address
            )
        )


def option1():  # view database
    if len(information) == 0:
        type(
            format.fg.red
            + "The address book is empty. Populate it with data first!"
            + format.reset
        )

    else:
        nicePrint()


def option2():  # add a new entry
    type("What is the new student's name?")
    studentname = input("> ")

    type("What is the new student's address?")
    address = input("> ")

    saved = True

    try:
        if studentname in information.keys():
            print(format.fg.red + "That student already exists!" + format.reset)
            saved = False

        if saved == True:
            information[studentname] = address
            save()
            print(
                format.fg.green + "The student was successfully added!" + format.reset
            )
    except:
        print(
            format.fg.red
            + "An unknown error occurred. Please try again later."
            + format.reset
        )


def option3():  # remove an entry
    nicePrint()

    type("\n\nType the name of the student you would like to remove:")
    studentname = input("> ")

    try:
        del information[studentname]
        save()
        type(format.fg.green + "The student was successfully removed!" + format.reset)
    except:
        type(format.fg.red + "That student doesn't exist!" + format.reset)


def returnMenu():  # return to the main menu with cooldown
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


type(
    format.bold
    + format.underline
    + "\nWelcome to a brand new address book!\n"
    + format.reset
)

while True:  # init loop
    clear()

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
        type(format.fg.red + "Thats not an option!" + format.reset)
        sleep(5)
