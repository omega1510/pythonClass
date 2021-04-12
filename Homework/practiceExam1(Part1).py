# Practice Exam Questions

# Create a normal non-lambda function which takes 4 numbers and add them up. Print the sum


def add(a, b, c, d):
    print(a + b + c + d)


add(1, 2, 3, 4)


# Convert this to a lambda function

addLambda = lambda a, b, c, d: print(a + b + c + d)

addLambda(1, 2, 3, 4)
# Create a normal non-lambda function which takes 3 numbers and multiply them up. Print the product


def multiply(a, b, c):
    print(a * b * c)


multiply(1, 2, 3)

# Convert this to a lambda function

multiplyLambda = lambda a, b, c: print(a * b * c)

multiplyLambda(1, 2, 3)

# Create 2  lists. One list is called keys. The other list is called values.

# In “keys” list, you should have these data: 'Ten', 'Twenty', 'Thirty',’Forty’
# In “values” list, you should have these data: 10, 20, 30,40

# Print the output of both lists

# Remember, this is a list, not dictionary!

keys = [
    "Ten",
    "Twenty",
    "Thirty",
    "Forty",
]
values = [
    10,
    20,
    30,
    40,
]

print(keys)
print(values)

# Using the 2 lists in question 1, convert them into a dictionary

# For example in the dictionary, key of ten should correspond to value ot 10 so {‘ten’:10}

combinedDictionary = dict(zip(keys, values))

# Print the dictionary

for key, value in combinedDictionary.items():
    print(key, ":", value)
