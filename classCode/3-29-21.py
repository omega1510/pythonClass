apples = {
    "cox": 17,
    "braeburn": 21,
    "pink lady": 7,
    "royal garla": 17,
    "fuji": 1
}

cox_stock = apples["cox"]
print("We have " + str(cox_stock) + " cox apples.")

for apple in apples.keys():
    print(apple)

for apple, stock_count in apples.items():
    print("We have " + str(stock_count) + " " + apple + " apples.")

mac_apples = apples.get("macintosh", 1)
print(mac_apples)
