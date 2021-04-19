# Test Questions

# Create 3  lists:

# In “student_name” list, you should have these data: 'Ahmad', 'James', 'Zainab'
# In “subject” list, you should have these data: ‘engineering’, philosophy’, ‘mathematics’
# In “age” list, you should have these data: ‘20’,’21’,’19’

# Print the output of all 3 lists

# Remember, this is a list, not dictionary!

student_name = [
    "Ahmad",
    "James",
    "Zainab",
]
subject = [
    "engineering",
    "philosophy",
    "mathematics",
]
age = ["20", "21", "19"]

print(student_name)
print(subject)
print(age)

# Using the 3 lists in question 1, convert it into a nested dictionary

# Hint:
# your_dictionary={‘name’:{‘subject’:’actual_subject_name’,’student_age’:’actual_age’}}

# Print the dictionary

student_name = [
    "Ahmad",
    "James",
    "Zainab",
]
subject = [
    "engineering",
    "philosophy",
    "mathematics",
]
age = [
    "20",
    "21",
    "19",
]

students = {}

for i in range(len(student_name)):
    name = student_name[i]
    studentSubject = subject[i]
    studentAge = age[i]

    students[name] = {studentSubject, studentAge}


for keys, values in students.items():
    print(keys, ":", values)

# Create a normal non-lambda function which takes 5 numbers and multiply them up. Print the product


def multiply(a, b, c, d, e):
    return a * b * c * d * e


print(multiply(1, 2, 3, 4, 5))

# Convert this to a lambda function

multiply = lambda a, b, c, d, e: a * b * c * d * e

print(multiply(1, 2, 3, 4, 5))

# Create a normal non-lambda function which takes 6 letters and print them all together as a word


def concat(a, b, c, d, e, f):
    return str(a) + str(b) + str(c) + str(d) + str(e) + str(f)


print(concat("c", "o", "d", "i", "n", "g"))

# Convert this to a lambda function

concat = lambda a, b, c, d, e, f: str(a) + str(b) + str(c) + str(d) + str(e) + str(f)

print(concat("c", "o", "d", "i", "n", "g"))

# studentDictionary = {
#   'student1': {'name': 'James', 'age': 23},
#   'student2': {'name': 'Haydar', 'age': 21},
#   'student3': {'name': 'Asiah', 'age': 18}
# }

# Show a way to check if a key Asiah in the dictionary.
# Print the dictionary

studentDictionary = {
    "student1": {
        "name": "James",
        "age": 23,
    },
    "student2": {
        "name": "Haydar",
        "age": 21,
    },
    "student3": {
        "name": "Asiah",
        "age": 18,
    },
}

if studentDictionary.get("Asiah") == "Asiah":
    print("Asiah is a key in the dictionary.")

else:
    print("Asiah is not a key in the dictionary.")

for keys, values in studentDictionary.items():
    print(keys, ":", values)
