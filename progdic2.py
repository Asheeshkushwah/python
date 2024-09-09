# Creating a dictionary
product = {"name": "Laptop", "price": 1200}

# Checking if a key exists
if "price" in product:
    print("Price:", product["price"])
else:
    print("Price key not found.")


    #22
    # Creating a dictionary
person = {"name": "Charlie", "age": 30, "city": "San Francisco"}

# Iterating through key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")

    #33

    fruit = {"name": "Apple", "color": "Red", "price": 0.5}

# Getting keys
keys = fruit.keys()
print("Keys:", list(keys))

# Getting values
values = fruit.values()
print("Values:", list(values))

#44
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

# Merging dictionaries
merged_dict = {**dict1, **dict2}

# Printing the merged dictionary
print("Merged dictionary:", merged_dict)

#555

company = {
    "name": "TechCorp",
    "employees": {
        "John": {"role": "Developer", "age": 28},
        "Sara": {"role": "Designer", "age": 32}
    }
}

# Accessing nested values
print("Company name:", company["name"])
print("John's role:", company["employees"]["John"]["role"])
print("Sara's age:", company["employees"]["Sara"]["age"])