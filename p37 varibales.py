# local variable(inside the function)

def myfunction():
    a=10
    b=20
    print("----Local varibles----")
    print(f"varible a:{a}")
    print(f"varible b:{b}")
    return a+b

print(myfunction())

# global variable(above the function)

dept="IT"
city="Chennai"
def func():
    print("=============================")
    print("----global varibles----")
    print(f"department:{dept}")
    print(f"city:{city}")

func()

# nonlocal variable
var1=50
var2=60
def function11(var1,var2):
    total=var1+var2
    print("total variable is local:",total)

function11(var1,var2)