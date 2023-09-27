# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

# This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

# For loop syntax :

my_list: list = [1, 2, 3, 4, 5, 6, 7, 8]

for item in my_list:
    if item == 3:
        pass

    if item == 4:
        continue

    print(item)

print("------------------------------------------------")
for letter in "banana":
    print(letter)


fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

    if fruit == "banana":
        break

print("------------------------------------------------")
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    if fruit == "banana":
        continue

    print(fruit)
print("------------------------------------------------")
# Range function ----------------------------------------------------------------
print("********************************")
for num in range(6):
    print(num)
print("********************************")
# [1, 2, 3, 4, 5, 6, 7, 8, 9) -> math
for num in range(1, 9):  # starts from 1
    print(num)

print("********************************")

# use of range() to define a range of values
values = range(4)

# iterate from i = 0 to i = 3
for i in values:
    print(i)
print("********************************")
print("------------------------------------------------")
# The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):

for num in range(2, 30, 3):  # 3n - 1 math formula
    print(num)

print("------------------------------------------------")

# Nested Loops ----------------------------------------------------------------
# A nested loop is a loop inside a loop.

# The "inner loop" will be executed one time for each iteration of the "outer loop":
colors = ["red", "blue", "white"]
fruits = ["apple", "banana", "cherry"]

for color in colors:  # loop 1: red
    for fruit in fruits:  # loop : apple
        print(color, fruit)  # --> red, apple

print("------------------------------------------------")


# Often, when dealing with iterators, we also need to keep a count of iterations. Python eases the programmers’ task by providing a built-in function enumerate() for this task. The enumerate () method adds a counter to an iterable and returns it in the form of an enumerating object. This enumerated object can then be used directly for loops or converted into a list of tuples using the list() function.

my_list = ["apple", "banana", "cherry", 1, 2, 3]

# output of  enumerate --> index then item in list
for index, item in enumerate(my_list):
    print(f"item: {item} --> index: {index}")


for item in enumerate(my_list):
    print(f"item: {item}")
