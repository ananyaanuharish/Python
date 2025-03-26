# if - else statement
name = input("enter the  name:")
age = int(input("enter the age:"))
citizen = input("enter the citizenship:")

if citizen in ["indian","Indian","INDIAN"]:
    if age >=18:
        print(f"{name}, You are eligible for vote.")
    else:
        print(f"{name}, You are not eligible for vote.")

else:
    print(f"{name}, you are not eligible for vote.")