# Types : string, int, float, bool, tuple, list

# 7 : Set

# Set
# Sets are used to store multiple items in a single variable.

# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
# A set is a collection which is unordered, unchangeable*, and unindexed.

# _list = [1, 2, 3, 4, 5]
# print(_list)

# fruit_list = ["apple", "banana", "cherry"]
# print(fruit_list)

# _tuple = (1, 2, 3, 4, 5)

# _set = {1, 2, 3, 4, 5}

# fruit_set = {"apple", "banana", "cherry"}

# print(fruit_set)
# print(type(fruit_set))


# for item in fruit_set:
#     print(item)


# Unordered
# Unordered means that the items in a set do not have a defined order.

# Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

fruit_list = ["apple", "banana", "cherry"]
fruit_list.append("orange")
print(fruit_list)

fruits = {"apple", "banana", "cherry"}

fruits.add("orange")
print(fruits)


# Duplicates Not Allowed
# Sets cannot have two items with the same value.

this_set = {"apple", "banana", "cherry", "apple"}

print(this_set)


# Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:
this_set = {"apple", "banana", "cherry", True, 1, 2}

print(this_set)

# False = 0
this_set = {"apple", "banana", "cherry", False, 0, 2}

print(this_set)
print(len(this_set))


thisset = set(("apple", "banana", "cherry", "apple"))  # note the double round-brackets
print(thisset)

# ExampleGet your own Python Server
# Remove a random item from the set:
thisset.pop()
print(thisset)

# Remove all elements from the fruits set:
thisset.clear()
print(thisset)


# Remove "banana" from the set:
fruits = {"apple", "banana", "cherry"}

fruits.remove("banana")

print(fruits)


# Python Set difference() Method
# Return a set that contains the items that only exist in set x, and not in set y:
# The difference() method returns a set that contains the difference between two sets.

# Meaning: The returned set contains items that exist only in the first set, and not in both sets.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.difference(y)

print(z)


b = y.difference(x)
print(b)


# Set union() Method
# Return a set that contains all items from both sets, duplicates are excluded:
# The union() method returns a set that contains all items from the original set, and all items from the specified set(s).

# You can specify as many sets you want, separated by commas.

# It does not have to be a set, it can be any iterable object.

# If an item is present in more than one set, the result will contain only one appearance of this item.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.union(y)

print(z)


x = {"a", "b", "c"}
y = {"f", "d", "a"}
z = {"c", "d", "e"}

result = x.union(y, z)

print(result)


# Set symmetric_difference() Method
# Return a set that contains all items from both sets, except items that are present in both sets:

# The symmetric_difference() method returns a set that contains all items from both set, but not the items that are present in both sets.

# Meaning: The returned set contains a mix of items that are not present in both sets.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)


# Set intersection() Method

# Return a set that contains the items that exist in both set x, and set y:

# The intersection() method returns a set that contains the similarity between two or more sets.

# Meaning: The returned set contains only items that exist in both sets, or in all sets if the comparison is done with more than two sets.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)


x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}

result = x.intersection(y, z)

print(result)


# Set issubset() Method
# Return True if all items in set x are present in set y:
# The issubset() method returns True if all items in the set exists in the specified set, otherwise it returns False.
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y)

print(z)


x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b"}

z = x.issubset(y)

print(z)
