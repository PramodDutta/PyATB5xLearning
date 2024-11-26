dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"a": 1, "b": 2}

missing_keys = set(dict1.keys()) - set(dict2.keys())
print(missing_keys)


# Sort a dictionary by its values in descending order
my_dict = {"a": 3, "b": 1, "c": 2}

# {b: 1 , c: 2 , a :3}