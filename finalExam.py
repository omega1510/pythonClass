#!/usr/bin/env python3

"""
Computer Science

Final Exam

Problem 1 (10 minutes)
dict1 = {'fruit': 'apple', 'type': 'fuji', ‘size’:’big’}

Create a function to print the list with this format

 Key: fruit    value: apple
 Key: type	value: fuji
 Key: size	value: big
"""
dict1 = {"fruit": "apple", "type": "fuji", "size": "big"}

for key, value in dict1.items():
    print("Key: ", key, "   ", "Value: ", value)


"""
Problem 2 (20 minutes)

Create a small program which consists of 2 functions. This program should ask for 3 numbers.  The program multiplies the first 2 numbers. That’s your product. The program then subtracts the 3rd number from the product of the first 2 numbers. Use numbers shown below to test your program.

Example:

Please enter your first number:
5
Please enter your second number:
7
Please enter your third number:
5

Answer:
Sum: ( 5*7) = 35
Product: 35/5 = 5

Please create 2 functions for calculating. One function is for calculating the product and another function to calculate the quotient or result of dividing.

If you don’t have 2 functions you will get 0. The point of this exercise is to make you practice using functions calling another function.

POST THE REPL SCREENSHOTS OF YOUR CODE AND RESULTS
NO SCREENSHOTS OF BOTH WILL GET YOU AND F
"""

# Your question said one thing, but the example answer said to do something else. I did what the questions said.

num1 = int(input("Please enter your first number:\n"))
num2 = int(input("Please enter your second number:\n"))
num3 = int(input("Please enter your third number:\n"))


def product(a, b):
    return a * b


def subtract(a, b, c):
    return product(a, b) - c


print("\nProduct: (%s*%d) = %f" % (num1, num2, product(num1, num2)))
print(
    "After Subtracting: (%s-%d) = %f"
    % (product(num1, num2), num3, subtract(num1, num2, num3))
)
