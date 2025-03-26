# function annotation
def func(x:"java", b:"python"=70) -> int:
    total_marks = x+y
    return total_marks

# result = func()
print(func.__annotations__)