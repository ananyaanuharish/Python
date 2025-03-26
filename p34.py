def primeNumber(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
    
num=int(input("enter a number:"))
if primeNumber(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")  