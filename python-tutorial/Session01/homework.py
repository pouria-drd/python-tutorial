# P1 : ----------------------------------------------------------------------
# Write a program to check whether a number entered by user is odd or even
num: float = float(input("please enter any number:"))

if num % 2 == 0:
    print("even")
else:
    print("odd")


# P2 : ----------------------------------------------------------------------
# Write a program to display the last digit of a number
num: int = int(input("please enter any number:"))

print(f"the last digit is  {num % 10}")

#  P3 : ----------------------------------------------------------------------
# برنامه ای بنویسید که عددی از کاربر بگیرد اگر بر 21 بخش پذیر بود نشاد دهد 21
# اگر بر 3 یا 7 بخش پذیر بود نشان دهد 3 یا 7
# در غیر این صورت نشان دهد bad input
num: float = float(input("enter the number:"))

if num % 7 == 0 and num % 3 == 0:
    print("21")
elif num % 3 == 0:
    print("3")
elif num % 7 == 0:
    print("7")
else:
    print("bad input")

# P 4: ----------------------------------------------------------------------
# برنامه ای بنویسی که نمره کاربر را دریافت کرده
# A اگر بالای 17 بود نشان دهد
# B بالای 14
# C بالای 12
# D بقیه نمرات هم
grade: float = float(input("What is your grade?"))

if grade >= 17:
    print("A!\nWellDone")

elif grade >= 14:
    print("B!\nnot bad")

elif grade >= 12:
    print("C!\ntry better")

else:
    print("D!\nWhy are you g*y?")
