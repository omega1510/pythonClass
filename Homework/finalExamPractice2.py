"""
FInal Exam Review HW 2

You’re given a dictionary

spam = {'color': 'red', 'age': '42','planet of origin': 'mars'}

Create a program to ask the user if he/she wants to print the dictionary. If he/she says yes, print it in a very nice format like the following way:

Key: color   value: red
Key: age     value: 42
Key: planet of origin    value: mars

Don’t simply print the whole list!!!! You should look at the for loop example in the example/notes (hint, with the k,v thingy….)

If he/she says no, just exit the program.

Make the print into a function.

Should be a 10 minute HW problem.
"""

#!/usr/bin/env python3

spam = {
    "color": "red",
    "age": "42",
    "planet of origin": "mars",
}


def nicePrint(dic):

    for key, value in dic.items():
        print(key, ":", value)


choice = input("Would you like to print the dictionary?\n> ")[0].lower()

if choice == "y":
    nicePrint(spam)
else:
    exit()
