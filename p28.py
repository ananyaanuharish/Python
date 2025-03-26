# match case
person = {"name":"Alice", "age":15}

match person:
    case{"name":name , "age":age} if age >=18:
        print(f"{name} is an adult.")
    case{"name":name, "age":age}:
        print(f"{name} is a minor.")
    case _:
        print("Unknown data")
