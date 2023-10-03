# Exercise 1: Convert two lists into a dictionary
# Below are the two lists. Write a Python program to convert them into a dictionary in a way that item from list1 is the key and item from list2 is the value

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# Expected output:

# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

# keys = ["Ten", "Twenty", "Thirty"]
# values = [10, 20, 30]


# res_dict = dict(zip(keys, values))
# print(res_dict)


# keys = ["Ten", "Twenty", "Thirty"]
# values = [10, 20, 30]

# # empty dictionary
# res_dict = dict()

# for i in range(len(keys)):
#     res_dict.update({keys[i]: values[i]})

# print(res_dict)


# Make your own zip function


# Exercise 2: Merge two Python dictionaries into one
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# Expected output:

# {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# dict1 = {"Ten": 10, "Twenty": 20, "Thirty": 30}
# dict2 = {"Thirty": 30, "Fourty": 40, "Fifty": 50}

# dict3 = {**dict1, **dict2}
# print(dict3)

# dict1 = {"Ten": 10, "Twenty": 20, "Thirty": 30}
# dict2 = {"Thirty": 30, "Fourty": 40, "Fifty": 50}

# dict3 = dict1.copy()
# dict3.update(dict2)
# print(dict3)
