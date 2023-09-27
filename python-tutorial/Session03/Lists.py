# List :
# name:list = [item1, item2, ....]

my_list: list = [
    "a",
    "b",
    "c",
    "d",
    "e",
    0,
    1,
    2,
    3,
    4,
    5,
    True,
    False,
    False,
    False,
    0.2,
    0.3,
    0.4,
    0.5,
]


my_list2: int = [[1, 2], [3, 4], [5, 6]]

#                 0,  1,   2
my_list3: list = [12, 17, 23]

print(f"list 3 : {my_list3}")
print(f"3rd member of list 3: {my_list3[2]}")
print(f"length : {len(my_list3)}")


len_list3: int = len(my_list3)
counter_list3: int = 0
maximum_number: int = 999999999.9999

while counter_list3 < len_list3:
    # scope of while loop
    print(f"counter : {counter_list3} ------ my_list3 : {my_list3[counter_list3]}")
    counter_list3 += 1


# MINIMUM NUMBER OF A LIST ----------------------------------------------------------

#                 0,  1,  2,  3 ,4
my_list4: list = [17, 12, 23, 5, 3]  # len = 5

len_list4: int = len(my_list4)
counter_list4: int = 0
minimum_number: int = 999999999.9999

# loop 1 :
# counter = 0, len list = 5, minimum number = 999999999.9999
while counter_list4 < len_list4:
    # loop 1 :
    # my_list4[0] = ? -> 17, smaller than minimum number ? -> true

    # loop 2 :  counter = 1, minimum = 17

    # loop 3 : counter = 2 , minimum = 12

    # loop 4 : counter = 3, minimum = 12

    # loop 5 : counter = 4, minimum = 5

    # loop 6 : counter = 5, minimum = 3

    if my_list4[counter_list4] < minimum_number:
        # loop 1 :
        # minimum_number = 17

        # loop 2 :
        # minimum_number = 12

        # loop 4 : minimum_number = 5

        # loop 4 : minimum_number = 3
        minimum_number = my_list4[counter_list4]

    counter_list4 += 1

print(f"min : {minimum_number}")  #  minimum_number = 3


# Maximum NUMBER OF A LIST ----------------------------------------------------------


#                 0,  1,  2,  3 ,4
my_list5: list = [17, 12, -23, -5, -3, 53]  # len = 5

len_list5: int = len(my_list5)
counter_list5: int = 0
maximum_number: int = -9999999999

while counter_list5 < len_list5:
    if my_list5[counter_list5] > maximum_number:
        maximum_number = my_list5[counter_list5]

    counter_list5 += 1

print(f"max : {maximum_number}")  #  minimum_number = 3


# Sorting a list :
my_list5.sort(reverse=True)
print(f"sort list 5 : {my_list5}")


# Count  :
# از این چیزی که من بهت میدم چند تا وجود داره
print(my_list5.count(17))

my_list6 = [
    1,
    2,
    5,
    6,
    7,
    8,
    8,
    8,
    8,
    8,
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "a",
]
print(my_list6.count(8))
print(my_list6.count("a"))

# reverse entire list items
print(f"my_list6 : {my_list6}")
my_list6.reverse()
print(f"my_list6 reversed : {my_list6}")

# index
print(my_list6.index("a"))


# add a new item to the list by using append
my_list6.append("apple")
print(f"my_list6 append apple : {my_list6}")

new_list = ["orange", "banana", "pineapple"]
my_list6.append(new_list)
print(f"my_list6 append new_list : {my_list6}")


# remove an item of a list with its name :
my_list6.remove("apple")
print(f"my_list6 removed new_list : {my_list6}")


# The pop() method removes the specified index.


my_list6.pop(1)
print(f"my_list6 pop index 1 : {my_list6}")


my_list6.pop()  # last index
print(f"my_list6 pop index last : {my_list6}")

popped_item = my_list6.pop()

print(f"popped_item: {popped_item}")

# The clear() method empties the list.
# The list still remains, but it has no content.
this_list = ["apple", "banana", "cherry"]
print(f"before clear: {this_list}")
this_list.clear()
print(f"after clear: {this_list}")
