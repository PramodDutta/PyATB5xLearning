# Dictionary from Two Lists

keys = ["name", "role", "experience"]
values = ["Aman", "SDET", 3]

my_dict = dict(zip(keys, values))
print(my_dict)


# Merge Two Dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merged_dict = dict1 | dict2
print(merged_dict)
print(merged_dict.get("a"))