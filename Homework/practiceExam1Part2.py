# Practice Exam Questions Part 2

# Watch this video again to refresh your memory
# https://youtu.be/IpbYrguvai0

# studentDictionary = {
#      'student1': {'name': 'Ali', 'score': 75},
#      'student2': {'name': 'Mary', 'score': 80},
#      'student3': {'name': 'Abbas', 'score': 65}
# }

# Show a way to check if a value of 85 exists in the dictionary.

studentDictionary = {
    "student1": {"name": "Ali", "score": 75},
    "student2": {"name": "Mary", "score": 80},
    "student3": {"name": "Abbas", "score": 65},
}

print(85 in studentDictionary.values())

# Show a way in on how to change Abbas’ grade from 65 to 78 and print out the final dictionary.

studentDictionary = {
    "student1": {"name": "Ali", "score": 75},
    "student2": {"name": "Mary", "score": 80},
    "student3": {"name": "Abbas", "score": 65},
}

studentDictionary["student3"]["score"] = 78

for key, value in studentDictionary.items():
    print(key, ":", value)

# Remove key student3 from the dictionary and print the final dictionary.

studentDictionary = {
    "student1": {"name": "Ali", "score": 75},
    "student2": {"name": "Mary", "score": 80},
    "student3": {"name": "Abbas", "score": 65},
}

del studentDictionary["student3"]

for key, value in studentDictionary.items():
    print(key, ":", value)
