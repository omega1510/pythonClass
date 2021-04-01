def factorial(a):

    if a == 0 or a == 1:
        return 1

    elif a < 0:
        return ArithmeticError

    else:
        return a * (factorial(a - 1))


num = 4

print(factorial(num))
