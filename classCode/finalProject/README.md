# Welcome to a brand new address book!
## By Hayaan Rizvi  


A great way to store the address of any student you want! The feature that sets this project apart from the others is that it will store and save you changes in an external database. If you add, edit, or delete a student you can close the program and come back later to continue your work.

_Make sure to include both `project.py` and `database.json` in the same directory before running the script. I have preloaded some data on there for you :)_

First we can write a shebang:


```python
#!/usr/bin/env python3
```

Then import packages:


```python
from os import system, name
from IPython.display import clear_output # to work in Jupyter
from time import sleep
import json
```

Create a function for a cool typewriter effect:


```python
def type(message):
    for i in message:
        print(i, flush=True, end="")

        sleep(0.02)
    print("")  # newline
```

Create a function to clear the screen:


```python
def clear():

    if name == "nt":
        _ = system("cls")

    else:
        _ = system("clear")

    clear_output(wait=True) # for Jupyter, returns nothing in python@3.9
```

A class of Ascii color codes can be used in place of an external module to get colorized and formatted text in terminals that support it. If a terminal doesn't support it, then it just prints normal text because of the `\` escape character. Usage is `print (format.fg.red + format.bold + "Message" + format.reset)`.


```python
class format:
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
```

We can try to read a `database.json` (the file where we save our address book) and return an empty dictionary if the file is empty or doesn't exist. The reason we use `json` is because the `json.load` method dynamicaly evaluates whatever data is passed to it. This way we can load a dictionary and not the raw bytes of the file.


```python
try:
    data = open("database.json", "r")
    information = json.load(data)
    data.close()
except:
    information = {}
```

Finally, we can start the actual menu (this will be called in an initialization loop later):


```python
def welcome():

    clear()

    type(
        format.bold
        + format.underline
        + "\nWelcome to a brand new address book!\n\n"
        + format.reset
    )

    type("Here is the menu:")
    type(format.fg.green + "1. " + format.reset + "View the address book")
    type(format.fg.green + "2. " + format.reset + "Insert a new entry")
    type(format.fg.green + "3. " + format.reset + "Delete an entry")
    type(format.fg.green + "4. " + format.reset + "Edit an entry")
    type(format.fg.green + "5. " + format.reset + "Quit the program\n")

    type("Choose an option:")
```

A save function can be created to save our changes to the address book. The file is opened as `write-only` to make sure we overwrite old data and not just append.


```python
def save():
    try:
        data = open("database.json", "w")
        json.dump(information, data)
        data.close()
    except:
        type(
            format.fg.red
            + "Saving your changes failed in the background! Make sure a file called "
            + format.reset + format.fg.yellow
            + "database.json "
            + format.reset + format.fg.red
            + "exists in the same directory as the main program."
            + format.reset
        )
```

And also create a function to nicely print the dictionary:


```python
def nicePrint():
    for name, address in information.items():
        num = list(information.keys()).index(name)  # gets index of
        type(                                       # key by converting
            str(                                    # to list, horrible way
                format.fg.green                     # do this.
                + str(num + 1)
                + ". "
                + format.reset
                + name
                + " : "
                + address
            )
        )
```

At last, we start coding our options. First option 1, which lets you view the database:


```python
def option1():
    if len(information) == 0:
        type(
            format.fg.red
            + "The address book is empty. Populate it with data first!"
            + format.reset
        )

    else:
        nicePrint()
```

Then option 2 to add an entry. First it checks if the student already exists and then adds it if it doesn't. It then runs `save()` to save your changes automatically. Because we are dealing with an external file, there is a general exception to catch errors.


```python
def option2():
    type("What is the new student's name?")
    studentname = input("> ")

    type("What is the new student's address?")
    address = input("> ")

    try:
        if studentname in information.keys():
            print(format.fg.red + "That student already exists!" + format.reset)

        else:
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

```

We can also give the user the option to remove an entry. Nothing special in this:


```python
def option3():
    nicePrint()

    type("\n\nType the name of the student you would like to remove:")
    studentname = input("> ")

    try:
        del information[studentname]
        save()
        type(format.fg.green + "The student was successfully removed!" + format.reset)
    except:
        type(format.fg.red + "That student doesn't exist!" + format.reset)
```

Option 4 is for editing the data that is already in the dictionary. It is the same code as adding a student but with a different UI. It also checks if the student doesn't exist.


```python
def option4():
    nicePrint()

    type("\n\nType the name of the student you would like to edit:")
    studentname = input("> ")

    if studentname in information.keys():
        type("\n\nType the new address:")
        newAddress = input("> ")
        information[studentname] = newAddress
        save()
        type(format.fg.green + "The student was successfully edited!" + format.reset)
    else:
        type(format.fg.red + "That student doesn't exist!" + format.reset)
```

The last function we define is one to send the user back to the main menu at the end of the loop. If the user chooses not to return, then the program waits 5 seconds and prompts them again.


```python
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
```

Finally, the last part of the code is the initialization loop.


```python
while True:

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

        option4()

        returnMenu()
        continue

    elif welcomeMenu == "5":

        break

    else:
        type(format.fg.red + "Thats not an option!" + format.reset)
        sleep(5)

```

I hope you enjoyed the program!
