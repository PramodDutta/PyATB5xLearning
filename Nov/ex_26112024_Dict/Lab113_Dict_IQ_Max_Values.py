# function that returns the maximum value from a dictionary.
# {"a": 10, "b": 20, "c": 30}

def max_value_dict(dictionary):
    #return max(dictionary.values())
    return min(dictionary.values()) # list of values

print(max_value_dict({"a": 10, "b": 20, "c": 30}))
