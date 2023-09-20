# Strings :

# Use case of back slash
# print("Hello,\n world")
# print("Hello,\t world")
# print("Hello, world from \"Iran\"")
# print("Hello, world from 'Iran'")

greetings: str = "Hello "
first_name = "Mohammad Amin Tajik"

print(greetings + first_name)

print(f"{greetings} {first_name}")

print(first_name.lower())
print(first_name.upper())


print(first_name[2])

print(first_name.replace("M", "m"))

print(len(first_name))

print(first_name.index("M"))
