# python function

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n* factorial(n-1)
    
while True:
    try:
        number = int(input("enter the number:"))
        if number < 0:
            print("please enter the positive number")
        else:
            break
    except ValueError:
        print("Invalid input")
    
# number = 5
print(f"factorial of {number} is {factorial(number)}")