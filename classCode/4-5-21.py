companyProfile = {
    "name": "Tesla",
    "ticker": "TSLA",
    "number of employees": 45000,
    "founded": "July 1, 2003"
}
print("Getting value of founded:")
print(companyProfile["founded"])

print("Getting value of shareprice with get function:")
print(companyProfile.get("share price", "Info not available"))

print('Adding "type" key and printing:')
companyProfile["type"] = "Public"
print(companyProfile)

print('Changing "type" value to "Private" and printing:')
companyProfile["type"] = "Private"
print(companyProfile)

print("Creating new dictionary of revenue and adding with update function:")
newInfo = {"revenue in 2020": 3153600000}

companyProfile.update(newInfo)
print(companyProfile)

print('Popping "revenue in 2020":')
print(companyProfile.pop("revenue in 2020"))
print(companyProfile)
