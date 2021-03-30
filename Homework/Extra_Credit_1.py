# Create a program to print “Hello World!”

print("Hello World!")

# Create a program to ask the user what is their age.
# AFTER they’ve entered their name  print “Thank you”
# Example:
# “How old are you?”
# Ali
# “Thank you”

age = input("What is your age?\n> ")
print("Thank you")

# Create a program to ask the user the time
# Example:
# “What time is it now?”

input("What time is it now?\n> ")

# Create a program to ask the user what is their math score. If it’s 90 or
# above, print “You got an A”. If the user enters 89 or lower,
# print “You got a B”
# Example:
# “What time is your math score?”
# 95
# “You got an A”
# “What time is your math score?”
# 85
# “You got an B”

score = int(input("What is your score in math?\n> "))
if score >= 90:
    print("You got an A")
else:
    print("You got a B")

# Output:

# Hello World!

# What is your age?
# > 15
# Thank you

# What time is it now?
# > 10:08

# What is your score in math?
# > 80
# You got a B
