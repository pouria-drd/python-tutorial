# continue  :
# Python Continue Statement skips the execution of the program block after the continue statement and forces the control to start the next iteration.

# while True:
#     x = int(input("Enter the number :"))
#     if x == 10:
#         continue
#     else:
#         print(x)


print("--" * 10)

shape: str = "*"
my_length: int = 5
helper_length: int = my_length
counter: int = 0

while counter < my_length:
    print(shape * (counter + 1))
    counter += 1


while my_length >= 0:
    print(shape * (my_length + 1))
    my_length -= 1


print("--" * 10)
