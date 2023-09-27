# Python Functions
# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.
# Creating a Function
# In Python a function is defined using the def keyword:

# def my_function():
#     pass


def my_function():
    print("Hello from a function")


# Call a function
my_function()


def my_function2(message="hello from a function"):
    print(message)


my_function2()  # if not give input --> default value
my_function2(10000000000000)


def sum_input(input: list):
    sum = 0
    for i in input:
        sum += i

    print(f"The sum is: {sum}")


my_list = [1, 2, 3, 4, 5]

sum_input(my_list)

sum_input(range(1000000))


my_function2(sum(range(1000000)))


# Keyword Arguments
# You can also send arguments with the key = value syntax.

# This way the order of the arguments does not matter.


def my_function3(child1, child2, child3):
    print("The  child 1 is " + child1)
    print("The  child 2 is " + child2)
    print("The  child 3 is " + child3)


my_function3("Emil", "Tobias", "Linus")
print("****************************************************************")
my_function3(child3="Emil", child1="Tobias", child2="Linus")


# Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

# This way the function will receive a tuple of arguments, and can access the items accordingly:


# Example
# If the number of arguments is unknown, add a * before the parameter name:
def my_function_args(*kids):
    print(kids)


my_function_args("Emil", "Tobias", "Linus")


# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

# This way the function will receive a dictionary of arguments, and can access the items accordingly:


# Example
# If the number of keyword arguments is unknown, add a double ** before the parameter name:


def my_function4(**kid):
    print(kid)
    print("His last name is " + kid["last_name"])


my_function4(first_name="najm", last_name="tajik")


def my_power(number):
    print(number**number)


my_power(4)


def my_power(number):
    result = number**number
    return result


result = my_power(40)

print(result)


# A Python program to return multiple
# values from a method using tuple


# This function returns a tuple
def fun():
    str = "test"
    x = 20
    return str, x
    # Return tuple, we could also
    # write (str, x)


# Driver code to test above method
str, x = fun()  # Assign returned tuple
print(str)
print(x)


res = fun()
print(res)


def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1

    else:
        return n * factorial_recursive(n - 1)


print(factorial_recursive(3))


import time

# get the start time
st = time.time()

my_number = 999

result: int = 1


while my_number > 0:
    result *= my_number
    my_number -= 1

# get the end time
et = time.time()

print(result)

# get the execution time
elapsed_time = et - st
print("Execution time:", elapsed_time, "seconds")
