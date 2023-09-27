# Tuple
# Tuples are used to store multiple items in a single variable.

# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

# A tuple is a collection which is ordered and unchangeable.

# Tuples are written with round brackets.

# list ["apple", "banana", "cherry"]

thistuple = ("apple", "banana", "cherry")
print(thistuple)
print(len(thistuple))
print(type(thistuple))
print(thistuple[1])
print(thistuple[-1])


# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new tuple with the specified items.
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])


# This example returns the items from the beginning to, but NOT included, "kiwi":
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])


# This example returns the items from "cherry" and to the end:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])


# This example returns the items from index -4 (included) to index -1 (excluded)
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])


thistuple = ("apple", "banana", "cherry")

if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")

for fruit in thistuple:
    if fruit == "apple":
        print("Yes, 'apple' is in the fruits tuple")


thistuple = ("apple", "banana", "cherry")
y = ("orange",)  #  ("orange",)  , this should be in tuple with len of 1
thistuple += y

print(thistuple)


thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)


thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i])


thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1


tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)


fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)
