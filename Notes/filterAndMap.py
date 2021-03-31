a = [100, 2, 8, 60, 5, 4, 3, 31, 10, 11]

# creates lambda function and accepts items that are
# multiples of 2. Assigns returned tuple to var filtered.
filtered = filter(lambda x: x % 2 == 0, a)

# prints filtered as a list
print(list(filtered))

# creates lambda function and applies to every item in list.
# returns a tuple
maped = map(lambda x: x % 2 == 0, a)

# prints maped as a list
print(list(maped))
