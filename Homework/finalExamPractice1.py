"""
Final Exam Review HW1

You are given this dictionary. It has print commands to print certain keys.

-----------------
# Nested dictionary having same keys
Dict = { 'Dict1': {'name': 'Ali', 'age': '19'},
        'Dict2': {'name': 'Bob', 'age': '25'}}
 # Prints value corresponding to key 'name' in Dict1

#Using string
print(Dict['Dict1']['name']) #prints Ali

# Prints value corresponding to key 'age' in Dict2
print(Dict['Dict1'][name])
-------------------

Change those print commands into functions which accept user inputs. For example instead of printing [‘Dict1’][‘name’] you will ask the user to enter the dictionary to print from and the key to print from

Example:
Please enter dictionary name: Dict1
Please enter key: ‘age’

Output: ‘19’
"""

Dict = {
    "Dict1": {"name": "Ali", "age": "19"},
    "Dict2": {"name": "Bob", "age": "25"},
}


def dic():
    return input("Enter the dictionary to print from (Dict1 or Dict2): ")


def key():
    return input("Enter the key to print from (name or age): ")


print("\n" + Dict[dic()][key()])
