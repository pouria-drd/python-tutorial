# While --> تا وقتی که تا زمانی که
# loop حلقه
# While syntax :

# While condition :
#     code


# while True:
#     print("Hello, world")


# print("Not execute until while loop finished")


# while True:
#     my_input: str = input("Please enter something:")

#     if my_input.lower() == "exit":
#         break  # --> use break for exit the loop

#     else:
#         print(my_input)

# print("Not execute until while loop finished")


# We are trying to limit our while loop (run only 10 times).
# counter: int = 1

# while counter <= 10:
#     print(f"Running {counter} times")
#     # counter = counter + 1 use this
#     counter += 1  # or this


# We want to print every letter of our input.
# name: str = input("Please enter your name:")
# name_length: int = len(name)
# counter: int = 0

# while counter < name_length:
#     print(name[counter])
#     counter = counter + 1


# Combination of all above notes.
is_running: bool = True

while is_running:
    my_input: str = input("Please enter something:")

    if my_input.lower() == "exit":
        print("Exiting program...")
        # break  # --> use break for exit the loop
        is_running = False

    else:
        name_length: int = len(my_input)
        counter: int = 0

        print(f"Length of {my_input} : {name_length}")

        while counter < name_length:
            print(my_input[counter])
            counter = counter + 1
