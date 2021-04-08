# 1. Create a dictionary with the following key-value pair
# and print the output on repl:

# car, bmw
# color, brown
# number, 5

dictionary1 = {
    "car": "bmw",
    "color": "brown",
    "number": 5,
}

for key, value in dictionary1.items():
    print(key, ":", value)


# 2. For the dictionary above, delete the key-value pair {‘number’:5}

del dictionary1["number"]

# 3. Create a dictionary with the following key-value
# pair and print the output it on repl

# subjects, [‘math’,’english’]
# students, {‘Name’: ‘Ahmad’,’Age’:5}

dictionary2 = {
    "subjects": ["math", "english"],
    "students": {
        "Name": "Ahmad",
        "Age": 5,
    },
}

for key, value in dictionary2.items():
    print(key, ":", value)

# For the dictionary above, add the key-value pair {‘word’:’hello’}

dictionary2["word"] = "hello"
