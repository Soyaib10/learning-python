# Using curly braces
my_dict = {
    "name": "Zihad",
    "age": 25,
    "city": "Silicon Vally"
}

# Using the dict() constructor
my_dict2 = dict(name="Soyaib", age=25, city="Dhaka")

# print
print(my_dict2)
print(my_dict["name"])
print()

# Modify Dictionary
my_dict["year"] = "2026"
my_dict["age"] = 27
print(my_dict)
print()

# Methods
print(my_dict.keys())
print(my_dict.values())
if "name" in my_dict: print("exists")
print()

# iteration
# Iterating over keys
for i in my_dict: print(i)
print()

# Iterating over values
for i in my_dict.values(): print(i)
print()

# Iterating over key-value pairs
for i, j in my_dict.items(): print(i, j)
print()




