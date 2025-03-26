def get_valid_marks():
    while True:
        try:
            mark = float(input("enter the mark:"))

            if mark < 0:
                print("error:marks cannot be negative")

            elif mark > 100:
                print("error:marks cannot be greater than 100")

            else:
                return mark
        except ValueError:
            print("error:invalid input. please enter the valid input")

def grade(mark):
    if mark>=90:
        return "A+"
    elif mark>=80:
        return "A"
    elif mark>=70:
        return "B"
    elif mark>=60:
        return "B+"
    elif mark>=50:
        return "D (pass)"
    else:
        return "F (fail)"
    
mark=get_valid_marks()
gra=grade(mark)
print(f"your grade:{gra}")