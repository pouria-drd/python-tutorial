# comparison operators ->  <  >  <= >=  == !=

if 3 < 2:
    print("yes")

print("asghar")

# If part 2: ----------------------------------------------------------------------

name: str = input("Please enter your name:")
age: int = int(input("Please enter your age:"))

if name.lower() != "amin":
    print("You are not allowed to enter in site")

else:
    print("Welcome !")

if name.lower() == "amin":
    print("You are not allowed to enter in site")

else:
    print("Welcome !")


#  and  or not

# and -->  all conditions must applied .

# or -->  any condition that can be done.

# not --> -1 none conditions not app applied .


# AND : ----------------------------------------------------------------------

if name.lower() == "amin" and age >= 18:
    print("Welcome")

else:
    print("You are g*y so You are not allowed to enter in site :)")


# OR : ----------------------------------------------------------------------

if name.lower() == "amin" or age >= 18:
    print("Welcome")

else:
    print("You are g*y so You are not allowed to enter in site :)")


# NOt : ----------------------------------------------------------------------

if not (name.lower() == "amin" or age >= 18):
    print("Welcome")

else:
    print("You are g*y so You are not allowed to enter in site :)")


x: bool = False

print(not x)


y: bool = True

print(not y)
