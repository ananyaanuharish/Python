# arithmetic exception
try:
    num = int(input("enter the number:"))
    result = num/2
    print(f"Result :{result}")
except ZeroDivisionError:
    print("Error: cannot divide by zero")
except ValueError:
    print("Error: Invalid input please enter the number")
else:
    print("Division successful")
finally:
    print("Execution completed")

# Multiple execution handling
try:
    list = [1,2,3]
    index = int(input("enter an index:"))
    print(list[index])
except IndexError:
    print("error:index out of range")
except ValueError:
    print("errpr:enter the valid numeric number")
finally:
    print("execution completed")

# custom exception
class AgeTooSmallError(Exception):
    pass
try:
    age=int(input("enter the age:"))
    if age <18:
        raise AgeTooSmallError("age must be 18 or above")
    print("you are eligible")
except AgeTooSmallError as e:
    print(f"Error:{e}")
except ValueError:
    print("error:please enter a value input")