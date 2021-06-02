"""
Final Exam Review HW 3

Create a small program which asks for 3 numbers, The program adds the first 2 numbers and multiplies the 3rd number with the sum of the 2 numbers

Example:

Please enter your first number:
22
Please enter your second number:
3
Please enter your third number:
5

Answer:
Sum: ( 22 +3) = 25
Product: 25 * 5 = 125

Please create 2 functions for calculating. One function is for calculating the sum and another function to calculate the product. The sum function will call the product function.

If you don’t have 2 functions you will get 0. The point of this exercise is to make you practice using functions calling another function.

"""

num1 = int(input("What is the first number?"))
num2 = int(input("What is the second number?"))
num3 = int(input("What is the third number?"))


def add(a, b):
    return a + b


def multiply(x, y, z):
    return add(x, y) * z


print(multiply(num1, num2, num3))
