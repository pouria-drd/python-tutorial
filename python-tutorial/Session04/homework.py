# Exercise 1: Print the following pattern
# Write a program to print the following number pattern using a loop.

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# print("Number Pattern", end="    ")
# print("Number Pattern")

# Decide the row count. (above pattern contains 5 rows)
# row = 5
# # start: 1
# # stop: row+1 (range never include stop number in result)
# # step: 1
# # run loop 5 times
# for i in range(1, row + 1, 1):
#     # Run inner loop i+1 times
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     # empty line after each row
#     print("")


# def print_pattern(row=5):
#     for i in range(1, row + 1, 1):
#         # Run inner loop i+1 times
#         for j in range(1, i + 1):
#             print(j, end=" ")
#         # empty line after each row
#         print("")


# print_pattern(7)


# Exercise 2: Write a program to print multiplication table of a given number
# For example, num = 2 so the output should be
# print("****************************************************************")
# n = 2
# # stop: 11 (because range never include stop number in result)
# # run loop 10 times
# for i in range(1, 11, 1):
#     # 2 *i (current number)
#     product = n * i
#     print(product)


# print("****************************************************************")

# Exercise 3: Print the following pattern
# Write a program to use for loop to print the following reverse number pattern
# n = 5
# k = 5
# for i in range(0, n + 1):
#     for j in range(k - i, 0, -1):
#         print(j, end=" ")
#     print()


# Exercise 4: Print the following pattern
# Write a program to print the following start pattern using the for loop
# Expected Output:
# shape=*
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *


# def print_pattern(length: int = 6, shape: str = "*"):
#     for i in range(1, length):
#         print(shape * i)

#     for i in range(length, 0, -1):
#         print(shape * i)


# # or
# # current_index = length
# # while current_index > 0:
# #     current_index -= 1
# #     print(shape * current_index)


# pattern_length = input("Please enter pattern length: (default=6)")
# pattern_shape = input("Please enter pattern shape: (default=*)")

# if pattern_length and pattern_shape:
#     print_pattern(shape=pattern_shape, length=int(pattern_length))

# else:
#     print_pattern()


# Exercise 5: Write a Python program to construct the following pattern, using a nested loop number.
# Expected Output:

# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999


# def print_number_pattern(max_num: int = 9):
#     for i in range(1, max_num + 1):
#         print(str(i) * i)


# max_num = input("Please enter length: (default=9)")

# if max_num:
#     print_number_pattern(int(max_num))
# else:
#     print_number_pattern()


# Exercise 6: Write a Python program to create the multiplication table (from 1 to 10) of a number.
# Expected Output:

# Input a number: 6
# 6 x 1 = 6
# 6 x 2 = 12
# 6 x 3 = 18
# 6 x 4 = 24
# 6 x 5 = 30
# 6 x 6 = 36
# 6 x 7 = 42
# 6 x 8 = 48
# 6 x 9 = 54
# 6 x 10 = 60


# def print_multiple(number: int = 6, max_multiple: int = 10):
#     for i in range(1, max_multiple + 1):
#         print(f"{number} X {i} = {number * i}")


# num = input("Please enter a number:(default=6)")
# max_multiple = input("Please enter a number:(default=10)")

# if num and max_multiple:
#     print_multiple(int(num), int(max_multiple))
# else:
#     print_multiple()


# Optional
# Exercise 7: Write a Python program to print the alphabet pattern 'Z'.
# Expected Output:
# *******
#      *
#     *
#    *
#   *
#  *
# *******


# def print_letter_z(length: int = 6, shape: str = "*"):
#     print(shape * length)

#     for i in range(length - 2, 0, -1):
#         print(" " * i + shape)

#     print(shape * length)


# num = input("Please enter a number:(default=6)")
# my_letter = input("Please enter a letter:(default=*)")

# if num and my_letter:
#     print_letter_z(int(num), my_letter)
# else:
#     print_letter_z()


# Optional
# Exercise 8: Write a Python program to print the alphabet pattern 'M'.
# Expected Output:
#   *       *
#   *       *
#   * *   * *
#   *   *   *
#   *       *
#   *       *
#   *       *


def print_letter_m(length: int = 7, shape: str = "*"):
    for i in range(length):
        if i == 2:
            print(shape + " " + shape + " " * 3 + shape + " " + shape)

        elif i == 3:
            print(shape + " " * 3 + shape + " " * 3 + shape)

        else:
            print(shape + " " * length + shape)


print_letter_m()
