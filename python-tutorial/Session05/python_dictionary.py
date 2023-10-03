# Types : string, int, float, bool, tuple, list, set

# 8 : Dictionary

# Python Dictionaries

my_dict = {
    #  Key   value
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
}

# Dictionaries are used to store data values in key:value pairs.

# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
print(my_dict)

print(my_dict["brand"])
print(my_dict["model"])
print(my_dict["year"])

# Ordered or Unordered?
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
# When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.

# Unordered means that the items does not have a defined order, you cannot refer to an item by using an index.


# Duplicates Not Allowed
# Dictionaries cannot have two items with the same key:
this_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020,
}

print(this_dict)
print(len(this_dict))


this_dict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": [
        "red",
        "white",
        "blue",
    ],
}

print(this_dict)


# The dict() Constructor
# It is also possible to use the dict() constructor to make a dictionary.
# Using the dict() method to make a dictionary:

this_dict = dict(
    name="John",
    age=36,
    country="Norway",
)
print(this_dict)


m_list = [
    ("name", "John"),
    {"age", "36"},
    ["country", "Norway"],
]

this_dict = dict(m_list)
print(this_dict)


# Removes all the elements from the dictionary
# this_dict.clear()
# print(this_dict)

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
}

x = car.get("model")
# x = car["model"]
print(x)


car = {"brand": "Ford", "model": "Mustang", "year": 1964}
# Try to return the value of an item that do not exist:
x = car.get("price", 15000)

print(x)


# Return the dictionary's key-value pairs:

car = {"brand": "Ford", "model": "Mustang", "year": 1964}

x = car.items()

print(x)


# Return the keys:

car = {"brand": "Ford", "model": "Mustang", "year": 1964}

x = car.keys()

print(x)

# Return the values:
x = car.values()

print(x)


# Insert an item to the dictionary:

car = {"brand": "Ford", "model": "Mustang", "year": 1964}

car.update({"color": "White"})

print(car)

# Removes the element with the specified key

car.pop("brand")
print(car)

car = {"brand": "Ford", "model": "Mustang", "year": 1964}

x = car.pop("model")

print(x)
